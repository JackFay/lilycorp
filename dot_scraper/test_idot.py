import requests
from bs4 import BeautifulSoup

BASE_URL = "https://webapps1.dot.illinois.gov"
session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
})

# 1. Get Home page to discover lettings
print("Fetching WCTB Home...")
r = session.get(f"{BASE_URL}/WCTB/LBHome")
soup = BeautifulSoup(r.text, "html.parser")

prior_select = soup.find("select", {"id": "PriorLettingDate"})
lettings = []
if prior_select:
    for opt in prior_select.find_all("option"):
        val = opt.get("value", "")
        text = opt.text.strip()
        if "/WCTB/LbLettingDetail/Index/" in val:
            letting_id = val.split("/")[-1]
            lettings.append((text, letting_id, val))

print(f"Found {len(lettings)} archived lettings.")
for text, lid, val in lettings[:5]:
    print(f" - {text}: {lid}")

# Pick the most recent completed letting (e.g. July 31, 2026)
target_letting_date, target_letting_id, target_letting_url = lettings[0]
print(f"\nTesting Letting: {target_letting_date} ({target_letting_id})")

detail_res = session.get(f"{BASE_URL}{target_letting_url}")
detail_soup = BeautifulSoup(detail_res.text, "html.parser")

# Find verification token
token_input = detail_soup.find("input", {"name": "__RequestVerificationToken"})
token = token_input.get("value") if token_input else ""
print(f"RequestVerificationToken found: {bool(token)}")

# Try search for PayItem 59000200 (Epoxy Crack Injection)
search_url = f"{BASE_URL}/WCTB/LbLettingDetail/Search"
payload = {
    "__RequestVerificationToken": token,
    "UserFilters.LettingDateId": target_letting_id,
    "UserFilters.ProjectType": "0",
    "UserFilters.Region": "-1",
    "UserFilters.DistrictCodeId": "00000000-0000-0000-0000-000000000000",
    "UserFilters.CountyCodeId": "00000000-0000-0000-0000-000000000000",
    "UserFilters.PayItem": "59000200",
    "UserFilters.PayItemDescription": "",
}

print("Posting search for Pay Item 59000200...")
search_res = session.post(search_url, data=payload)
print(f"Response status: {search_res.status_code}")

search_soup = BeautifulSoup(search_res.text, "html.parser")
table = search_soup.find("table")
if table:
    rows = table.find_all("tr")
    print(f"Table found with {len(rows)} rows!")
    for row in rows[1:10]:
        cols = [td.text.strip() for td in row.find_all("td")]
        if cols:
            print("Row:", cols[:5])
else:
    print("No table found in search response. Checking page text length:", len(search_res.text))
