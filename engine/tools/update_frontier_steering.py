import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
FRONTIER_FILE = BASE_DIR / "state" / "frontier.json"

with open(FRONTIER_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

new_items = [
    {
        "id": "DEAL_FIN_GAP_01",
        "category": "Deal & Capital Structure",
        "title": "Closing the $297k Sources & Uses Deficit: Purchase Price Adjustment vs Earnout vs Inventory True-Up",
        "question": "How will the $296,692 unfunded gap between $1,300,000 in uses (purchase price + working capital) and $1,003,308 in identified sources (SBA loan + buyer equity + standby seller note) be definitively resolved prior to closing?",
        "known_facts": [
            "Senior SBA loan is hard-capped at $437.9k-$443.3k based on 2024 CFADS of $85k.",
            "Buyer cash equity is capped at $60,000.",
            "Uses require $1.25M purchase price + $50,000 working capital buffer = $1.30M."
        ],
        "open_uncertainties": [
            "Will Bob accept a purchase price reduction to $953k, or convert $297k into a gross-margin-tied earnout?",
            "How much will the pre-closing physical inventory count write down the asset value dollar-for-dollar?"
        ],
        "target_plan_file": "plan/01_deal_and_capital_structure.md",
        "confidence_score": 3,
        "status": "OPEN",
        "priority": "CRITICAL"
    },
    {
        "id": "DEAL_NOTE_CLIFF_02",
        "category": "Deal & Capital Structure",
        "title": "Modeling & Negotiating the Month 25 Seller Note Debt Cliff ($570k Accrued Principal vs $85k CFADS)",
        "question": "What contractual amortization and restructuring terms must be established for Bob Trout's $500,000 seller note compounding to ~$570k after 24 months of 7% standby to prevent corporate insolvency at Month 25?",
        "known_facts": [
            "At Month 25, 10-year amortization adds ~$79.8k/yr ($6,647/mo); 5-year amortization adds ~$136.0k/yr ($11,335/mo).",
            "Baseline historical CFADS is only $85k (2024 bank basis) or $169k (2025 best case).",
            "Senior debt ($68.8k) + Lease ($68k) already consume $136.8k/yr."
        ],
        "open_uncertainties": [
            "Can Jack negotiate a 10-to-15 year post-standby amortization, interest-only extensions in Years 3-4, or an earnout conversion?"
        ],
        "target_plan_file": "plan/01_deal_and_capital_structure.md",
        "confidence_score": 2,
        "status": "OPEN",
        "priority": "CRITICAL"
    },
    {
        "id": "DILIGENCE_QOE_03",
        "category": "Due Diligence & Quality of Earnings",
        "title": "Quality of Earnings & Inventory Double-Count Reconciliation",
        "question": "How will the $108,218 in 2024 duplicate inventory entry errors and the 2025 $200,387 write-down be reconciled through an independent physical inventory count to avoid double-counting historical earnings?",
        "known_facts": [
            "Marcelo email confirms 2025 write-down included $108,218 of 2024 duplicate receipt debits and $92,169 in 40-year dead stock.",
            "Correcting 2024 for the inventory overstatement drives 2024 CFADS to negative -$33k.",
            "SBA underwriting adopted $85k CFADS for 2024 without applying this correction."
        ],
        "open_uncertainties": [
            "What is the verified liquidation value of current on-shelf inventory older than 24 months?",
            "What is the exact net working capital target in the purchase agreement?"
        ],
        "target_plan_file": "plan/01_deal_and_capital_structure.md",
        "confidence_score": 3,
        "status": "OPEN",
        "priority": "CRITICAL"
    },
    {
        "id": "OPER_ROSTER_RETENTION_04",
        "category": "Operator Takeover & Leadership",
        "title": "Shop Floor Retention Architecture for Dave Kling (Machining/Purchasing) and Greg (Press Operator)",
        "question": "What concrete retention agreements, stay bonuses, and operational incentives will secure Dave Kling (lead fabricator/purchasing) and Greg (sole in-house injection press operator) alongside Dave Jepsen?",
        "known_facts": [
            "Greg is the only person at Lily who operates the injection molding press and runs hydrostatic rebuild testing.",
            "Dave Kling is the only master machinist, TIG welder, and handles all vendor purchasing and equipment repairs.",
            "The current operator guide gives Dave Jepsen synthetic equity and margin bonuses, but provides zero retention terms for Kling or Greg."
        ],
        "open_uncertainties": [
            "What stay bonus structure and press uptime bonus will align Dave K and Greg without destabilizing shop culture?"
        ],
        "target_plan_file": "plan/05_jack_fay_operator_guide.md",
        "confidence_score": 4,
        "status": "OPEN",
        "priority": "CRITICAL"
    },
    {
        "id": "FIN_CASHFLOW_36M_05",
        "category": "Financial Modeling & Cash Flow",
        "title": "36-Month Grounded Cash Flow Forecast: Seasonality, Fixed $11.4k Monthly Floor, and Downside Breakeven",
        "question": "What does a monthly 36-month cash-flow forecast show across Midwest civil construction seasonality (Q1 winter troughs) against the mandatory $11,400/month debt and lease floor, $8,333/month GM salary, and a 15% revenue drop downside scenario?",
        "known_facts": [
            "Civil bridge and concrete repair is heavily seasonal in Illinois/Midwest; winter cash flow dips sharply.",
            "Discretionary working capital is only $50,000.",
            "Fixed monthly cash requirements sit at $19.7k/month before any material or direct shop labor costs."
        ],
        "open_uncertainties": [
            "How many months of winter cash burn can the $50k buffer withstand without an operating line of credit?"
        ],
        "target_plan_file": "plan/00_assumed_capital_baseline.md",
        "confidence_score": 3,
        "status": "OPEN",
        "priority": "CRITICAL"
    },
    {
        "id": "COMM_PRICING_06",
        "category": "Commercial Strategy & Pricing",
        "title": "Day-1 Consumables List Price Increase: Capturing $30k-$50k Gross Margin with Zero Capex",
        "question": "How will a targeted 5-8% list price increase across Lily's proprietary molded consumables (surface ports, caps, static mixers) be deployed across direct contractor accounts and distributors on Day 1 without customer churn?",
        "known_facts": [
            "Molded consumables represent Lily's highest gross margin segment (~65-70%+).",
            "Contractors buy ports against emergency jobsite needs where port cost is <1% of total job contract value.",
            "Price increases require zero tooling capex, zero shop labor, and flow 100% to gross profit."
        ],
        "open_uncertainties": [
            "When was the last time Bob Trout raised list prices on molded accessories?"
        ],
        "target_plan_file": "plan/03_commercial_distribution_and_partnerships.md",
        "confidence_score": 4,
        "status": "OPEN",
        "priority": "HIGH"
    }
]

existing_ids = {x.get("id") for x in data.get("frontier", [])}
to_add = [item for item in new_items if item["id"] not in existing_ids]

data["frontier"] = to_add + data.get("frontier", [])
data["last_updated"] = "2026-10-11T18:00:00Z"

with open(FRONTIER_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print(f"Successfully injected {len(to_add)} critical steering items into frontier.json. Total items now: {len(data['frontier'])}")
