"""
IDOT Concrete Injection Bid & Letting Scanner
Scans IDOT WCTB for contracts specifying Pay Item 59000200 (Epoxy Crack Injection).
Works for both upcoming lettings (Authorized Bidders) and past lettings (Awarded Contractors).
"""

import re
import csv
import io
import json
import argparse
from typing import List, Dict, Any, Optional
import requests
from bs4 import BeautifulSoup
import pypdf

BASE_URL = "https://webapps1.dot.illinois.gov"

class IDOTScanner:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
        })

    def get_token(self, html_content: str) -> str:
        soup = BeautifulSoup(html_content, "html.parser")
        token_elem = soup.find("input", {"name": "__RequestVerificationToken"})
        return token_elem.get("value", "") if token_elem else ""

    def get_available_lettings(self) -> List[Dict[str, str]]:
        """Fetch upcoming and archived lettings from WCTB homepage."""
        res = self.session.get(f"{BASE_URL}/WCTB/LBHome")
        soup = BeautifulSoup(res.text, "html.parser")
        lettings = []

        # Check upcoming letting
        notice_label = soup.find("label", {"for": "Notice_of_Letting"})
        if notice_label:
            notice_a = notice_label.find_next("a", class_="largeFont")
            if notice_a and "/WCTB/LbLettingDetail/Index/" in notice_a.get("href", ""):
                href = notice_a.get("href", "")
                lettings.append({
                    "type": "Upcoming",
                    "date": notice_a.text.strip(),
                    "id": href.split("/")[-1],
                    "url": href
                })

        # Check archived lettings
        prior_select = soup.find("select", {"id": "PriorLettingDate"})
        if prior_select:
            for opt in prior_select.find_all("option"):
                val = opt.get("value", "")
                text = opt.text.strip()
                if "/WCTB/LbLettingDetail/Index/" in val:
                    lettings.append({
                        "type": "Archived",
                        "date": text,
                        "id": val.split("/")[-1],
                        "url": val
                    })
        return lettings

    def search_contracts_by_pay_item(self, letting_id: str, pay_item: str = "59000200") -> List[Dict[str, Any]]:
        """Search a specific letting for contracts containing a pay item."""
        detail_url = f"{BASE_URL}/WCTB/LbLettingDetail/Index/{letting_id}"
        res = self.session.get(detail_url)
        token = self.get_token(res.text)

        search_url = f"{BASE_URL}/WCTB/LbLettingDetail/Search"
        payload = {
            "__RequestVerificationToken": token,
            "UserFilters.LettingDateId": letting_id,
            "UserFilters.ProjectType": "0",
            "UserFilters.Region": "-1",
            "UserFilters.DistrictCodeId": "00000000-0000-0000-0000-000000000000",
            "UserFilters.CountyCodeId": "00000000-0000-0000-0000-000000000000",
            "UserFilters.PayItem": pay_item,
            "UserFilters.PayItemDescription": "",
        }
        search_res = self.session.post(search_url, data=payload)
        search_soup = BeautifulSoup(search_res.text, "html.parser")

        matches = []
        table = search_soup.find("table")
        if not table:
            return matches

        for row in table.find_all("tr"):
            cols = row.find_all("td")
            if len(cols) >= 10:
                item_contract_a = cols[0].find("a")
                if not item_contract_a:
                    continue
                item_contract = item_contract_a.text.strip()
                href = item_contract_a.get("href", "")
                
                # Extract contractId from href
                contract_id = ""
                if "contractId=" in href:
                    contract_id = href.split("contractId=")[-1].split("&")[0]

                status = cols[1].text.strip()
                status_date = cols[2].text.strip()
                region = cols[5].text.strip()
                district = cols[6].text.strip()
                county = cols[7].text.strip()
                bulletin_desc = cols[9].text.strip()

                contract_num = item_contract.split("-")[-1] if "-" in item_contract else item_contract

                matches.append({
                    "item_contract": item_contract,
                    "contract_num": contract_num,
                    "contract_id": contract_id,
                    "status": status,
                    "status_date": status_date,
                    "region": region,
                    "district": district,
                    "county": county,
                    "description": bulletin_desc,
                    "detail_url": href,
                })
        return matches

    def get_pay_item_details(self, letting_id: str, contract_id: str, pay_item_code: str = "59000200") -> List[Dict[str, Any]]:
        """Download CSV of pay items for a contract and extract injection line items."""
        url = f"{BASE_URL}/WCTB/LbContractDetail/GetPayItemExcelFile/{letting_id}?contractId={contract_id}"
        res = self.session.get(url)
        if res.status_code != 200:
            return []

        matched_items = []
        try:
            reader = csv.reader(io.StringIO(res.text))
            for row in reader:
                if len(row) >= 5 and pay_item_code in str(row[0]):
                    matched_items.append({
                        "pay_item": row[0].strip(),
                        "uom": row[1].strip(),
                        "description": row[2].strip(),
                        "quantity": float(row[4].strip()) if row[4].strip() else 0.0,
                    })
        except Exception as e:
            print(f"Error parsing pay item CSV for contract {contract_id}: {e}")
        return matched_items

    def get_awarded_contractor(self, contract_num: str) -> Optional[Dict[str, str]]:
        """Query LbContractStatus for the winning contractor and bid amount."""
        url = f"{BASE_URL}/WCTB/LbContractStatus"
        res = self.session.get(url)
        token = self.get_token(res.text)

        post_res = self.session.post(f"{BASE_URL}/WCTB/LbContractStatus/Search", data={
            "__RequestVerificationToken": token,
            "UserFilters.FromStatusDate": "",
            "UserFilters.ToStatusDate": "",
            "UserFilters.ContractNumber": contract_num,
            "UserFilters.ContractorNumber": "",
            "UserFilters.ContractorName": "",
        })
        soup = BeautifulSoup(post_res.text, "html.parser")
        table = soup.find("table")
        if not table:
            return None

        for tr in table.find_all("tr")[1:]:
            cols = [td.text.strip() for td in tr.find_all("td")]
            if len(cols) >= 6:
                status = cols[1]
                status_date = cols[3]
                bid_amount = cols[4]
                contractor_raw = " ".join(cols[5].split())
                return {
                    "status": status,
                    "status_date": status_date,
                    "bid_amount": bid_amount,
                    "contractor": contractor_raw
                }
        return None

    def get_authorized_bidders(self, letting_id: str) -> Dict[str, List[Dict[str, str]]]:
        """Extract authorized bidders from the letting's PDF document."""
        detail_url = f"{BASE_URL}/WCTB/LbLettingDetail/Index/{letting_id}"
        res = self.session.get(detail_url)
        soup = BeautifulSoup(res.text, "html.parser")

        pdf_link = None
        for a in soup.find_all("a"):
            if "list of authorized bidders" in a.text.lower():
                pdf_link = a.get("href")
                break

        if not pdf_link:
            return {}

        pdf_url = f"{BASE_URL}{pdf_link}" if pdf_link.startswith("/") else pdf_link
        pdf_res = self.session.get(pdf_url)
        if pdf_res.status_code != 200:
            return {}

        reader = pypdf.PdfReader(io.BytesIO(pdf_res.content))
        full_text = "\n".join(p.extract_text() or "" for p in reader.pages)

        # Parse text into items by "Letting Item\n: " or "Contract Number\n: "
        items_map: Dict[str, List[Dict[str, str]]] = {}
        sections = full_text.split("Contract Number")
        for s in sections[1:]:
            lines = [l.strip() for l in s.split("\n") if l.strip()]
            if not lines:
                continue
            contract_match = re.search(r"[:\s]+([0-9A-Za-z]+)", lines[0])
            if not contract_match:
                continue
            cnum = contract_match.group(1)
            
            # Find bidder entries (look for Phone: or 4-digit ID)
            bidders = []
            # Extract contractors from section text
            contractor_blocks = re.findall(r"(\d{4})\s*\n([^\n]+)\s*\n([^\n]+)\s*\n([^\n]+)\s*\nPhone:\s*\(([\d\s]+)\)\s*([\d-]+)", s)
            for b_id, name, addr1, city_state, p1, p2 in contractor_blocks:
                phone = f"({p1.strip()}) {p2.strip()}"
                bidders.append({
                    "vendor_id": b_id.strip(),
                    "name": name.strip(),
                    "address": f"{addr1.strip()}, {city_state.strip()}",
                    "phone": phone
                })
            items_map[cnum] = bidders

        return items_map

    def run(self, letting_index: int = 0):
        print(f"[*] Connecting to IDOT WCTB Portal ({BASE_URL})...")
        lettings = self.get_available_lettings()
        if not lettings:
            print("[-] No lettings found.")
            return

        target_letting = lettings[letting_index]
        print(f"[+] Target Letting: {target_letting['type']} - {target_letting['date']} (ID: {target_letting['id']})")

        print(f"[*] Searching for Pay Item 59000200 (Epoxy Crack Injection)...")
        contracts = self.search_contracts_by_pay_item(target_letting["id"], "59000200")
        print(f"[+] Found {len(contracts)} contracts specifying epoxy crack injection!\n")

        # Load authorized bidders if upcoming or available
        bidders_by_contract = {}
        if target_letting["type"] == "Upcoming":
            print("[*] Fetching and parsing Authorized Bidders list...")
            bidders_by_contract = self.get_authorized_bidders(target_letting["id"])

        results = []
        for c in contracts:
            print(f"--> Processing Contract {c['item_contract']} ({c['county']} County)...")
            pay_items = self.get_pay_item_details(target_letting["id"], c["contract_id"], "59000200")
            total_lf = sum(item["quantity"] for item in pay_items)

            # Awarded info
            award_info = self.get_awarded_contractor(c["contract_num"])

            # Bidders info
            bidders = bidders_by_contract.get(c["contract_num"], [])

            record = {
                "letting_date": target_letting["date"],
                "letting_type": target_letting["type"],
                "item_contract": c["item_contract"],
                "contract_num": c["contract_num"],
                "county": c["county"],
                "district": c["district"],
                "status": c["status"],
                "description": c["description"],
                "total_linear_feet": total_lf,
                "pay_items": pay_items,
                "award_info": award_info,
                "authorized_bidders": bidders
            }
            results.append(record)

        # Print summary report
        print("\n" + "="*80)
        print(f" IDOT CONCRETE INJECTION LEAD SHEET — LETTING: {target_letting['date']}")
        print("="*80 + "\n")

        for r in results:
            print(f"CONTRACT: {r['item_contract']} | County: {r['county']} (District {r['district']})")
            print(f"  Description: {r['description'][:110]}...")
            print(f"  Total Epoxy Injection: {r['total_linear_feet']:,.1f} LINEAR FEET")
            
            if r['award_info']:
                aw = r['award_info']
                print(f"  STATUS: {aw['status']} on {aw['status_date']} | Bid Total: {aw['bid_amount']}")
                print(f"  WINNER: {aw['contractor']}")
            elif r['authorized_bidders']:
                print(f"  AUTHORIZED BIDDERS ({len(r['authorized_bidders'])} prospective contractors):")
                for b in r['authorized_bidders']:
                    print(f"    - {b['name']} (Phone: {b['phone']}) | {b['address']}")
            else:
                print(f"  Status: {r['status']} (Awaiting Bid Opening / Award)")
            print("-" * 80)

        # Save JSON output
        out_filename = f"dot_scraper/leads_{target_letting['date'].replace(' ', '_').replace(',', '')}.json"
        with open(out_filename, "w") as f:
            json.dump(results, f, indent=2)
        print(f"\n[+] Saved complete lead dataset to {out_filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scan IDOT lettings for concrete injection work.")
    parser.add_argument("--letting-index", type=int, default=0, help="0 for most recent/upcoming, 1 for previous, etc.")
    args = parser.parse_args()

    scanner = IDOTScanner()
    scanner.run(letting_index=args.letting_index)
