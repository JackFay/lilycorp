#!/usr/bin/env python3
"""
Lily Corp Autonomous Diligence & Recursive Business Plan Loop.
Runs continuous, grounded research cycles with Gemini Flash and deterministic validation tools.
"""

import os
import sys
import json
import time
import subprocess
from datetime import datetime
from pathlib import Path
from google import genai
from google.genai import types

BASE_DIR = Path(__file__).resolve().parent.parent
PLAN_DIR = BASE_DIR / "plan"
STATE_DIR = BASE_DIR / "state"
STEERING_DIR = BASE_DIR / "steering"
EVIDENCE_DIR = BASE_DIR / "evidence"
FRONTIER_FILE = STATE_DIR / "frontier.json"
INBOX_FILE = STEERING_DIR / "inbox.md"
DIGEST_FILE = STEERING_DIR / "digest.md"
REJECTIONS_LOG = STATE_DIR / "rejections.log"


def load_env():
    """Load simple key=value pairs from .env if present."""
    env_file = BASE_DIR / ".env"
    if env_file.exists():
        with open(env_file, "r") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    os.environ[k.strip()] = v.strip()


def get_genai_client():
    """Initialize Google GenAI client via GEMINI_API_KEY or Vertex AI."""
    load_env()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key:
        return genai.Client(api_key=api_key)
    
    project = os.environ.get("GCP_PROJECT", "dulcet-voyager-496719-e3")
    location = os.environ.get("GCP_LOCATION", "us-central1")
    return genai.Client(vertexai=True, project=project, location=location)


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_text(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def check_steering_inbox() -> str:
    """Read any new notes in inbox.md and archive them."""
    if not INBOX_FILE.exists():
        return ""
    content = read_text(INBOX_FILE)
    # Check if there is actual user input beyond comments and headers
    lines = [line.strip() for line in content.splitlines()]
    user_notes = [l for l in lines if l and not l.startswith("#") and not l.startswith(">") and not l.startswith("<!--")]
    if not user_notes:
        return ""
    
    archive_file = STEERING_DIR / "archive.md"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"\n\n### Processed Note [{timestamp}]:\n" + "\n".join(user_notes) + "\n"
    
    existing_archive = read_text(archive_file)
    write_text(archive_file, existing_archive + entry)
    
    # Reset inbox with default header
    default_header = (
        "# Steering Inbox\n\n"
        "> **Instructions for Jack:**\n"
        "> Drop any real-world updates, notes from calls with Bob or bankers, new thoughts, or constraints here as bullet points.\n"
        "> The recursive loop reads this file at the start of every cycle, ripples the new facts across affected plan modules and financial models, updates the frontier, and archives your processed notes to `steering/archive.md`.\n\n"
        "---\n\n<!-- Add your notes below this line -->\n"
    )
    write_text(INBOX_FILE, default_header)
    return "\n".join(user_notes)


def load_frontier() -> dict:
    if not FRONTIER_FILE.exists():
        return {"frontier": [], "active_cycle": 0}
    with open(FRONTIER_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_frontier(data: dict):
    with open(FRONTIER_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def git_commit(message: str):
    try:
        subprocess.run(["git", "add", "plan/", "state/", "steering/"], cwd=BASE_DIR, check=True)
        subprocess.run(["git", "commit", "-m", message], cwd=BASE_DIR, check=True)
        print(f"Git commit successful: {message}")
    except Exception as e:
        print(f"Git commit warning: {e}")


def spawn_stress_test_scenario(client: genai.Client, model_name: str, frontier_data: dict) -> dict:
    prompt = """
You are the Chief Risk Officer and Hostile Competitor / Economic Stress-Tester for the acquisition of Lily Corporation (Aurora, IL).
All baseline diligence questions have been addressed.

Generate ONE severe, realistic real-world stress scenario to attack the acquisition plan.
Examples:
- "A major chemical resin partner (e.g. Sika, Euclid, MAPEI) changes nozzle or viscosity specifications, rendering current Lily dispenser mix ratios incompatible."
- "Dave Jepsen experiences health emergency in Month 3; contractor support and quoting knowledge is unbacked."
- "Raw nylon/polypropylene resin and aluminum prices surge 30% due to supply chain disruption, shrinking gross margins."
- "First American Bank requires a Phase I Environmental Site Assessment (ESA) due to chemical flushing on the Aurora shop floor, risking deal delay."

OUTPUT JSON ONLY:
{
  "category": "Risk Register & Stress Testing",
  "title": "Short title",
  "question": "Specific stress-test question examining downside cash flow and mitigation",
  "priority": "CRITICAL",
  "target_plan_file": "plan/06_risk_register_and_kill_switches.md"
}
"""
    try:
        resp = client.models.generate_content(
            model=model_name,
            contents=prompt,
            config=types.GenerateContentConfig(response_mime_type="application/json")
        )
        data = json.loads(resp.text.strip())
        spawn_id = f"STRESS_{len(frontier_data.get('frontier', [])) + 1:02d}"
        new_item = {
            "id": spawn_id,
            "category": data.get("category", "Risk Register & Stress Testing"),
            "title": data.get("title", "Adversarial Stress Test"),
            "question": data.get("question"),
            "known_facts": ["Autonomous stress test generated to probe downside limits of acquisition plan."],
            "open_uncertainties": [data.get("question")],
            "target_plan_file": data.get("target_plan_file", "plan/06_risk_register_and_kill_switches.md"),
            "confidence_score": 2,
            "status": "OPEN",
            "priority": "CRITICAL"
        }
        frontier_data.setdefault("frontier", []).append(new_item)
        save_frontier(frontier_data)
        print(f"[!] Autonomous Stress Test Spawned: [{spawn_id}] {new_item['title']}")
        return new_item
    except Exception as e:
        print(f"Error generating stress test: {e}")
        return None


def execute_cycle(client: genai.Client, model_name: str = None):
    if not model_name:
        model_name = os.environ.get("GEMINI_MODEL", "gemini-3.8-flash")
    frontier_data = load_frontier()
    cycle_num = frontier_data.get("active_cycle", 0) + 1
    frontier_data["active_cycle"] = cycle_num

    print(f"\n=======================================================")
    print(f"Starting Diligence Cycle #{cycle_num} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"=======================================================")

    # 1. Process steering inbox if any
    inbox_notes = check_steering_inbox()
    if inbox_notes:
        print(f"Found new steering notes from Jack:\n{inbox_notes}")

    # 2. Pick target frontier item (or spawn stress test if all resolved)
    open_items = [item for item in frontier_data.get("frontier", []) if item.get("status") in ["OPEN", "IN_PROGRESS"]]
    if not open_items:
        print("All existing frontier items resolved! Entering Autonomous Stress-Testing Mode...")
        stress_item = spawn_stress_test_scenario(client, model_name, frontier_data)
        if stress_item:
            open_items = [stress_item]
        else:
            print("No new stress tests generated. Plan is at peak convergence.")
            return

    # Prioritize CRITICAL then HIGH
    priority_order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}
    open_items.sort(key=lambda x: (priority_order.get(x.get("priority", "MEDIUM"), 2), x.get("confidence_score", 5)))
    target = open_items[0]

    print(f"Selected Target: [{target['id']}] {target['title']}")
    print(f"Question: {target['question']}")

    # 3. Assemble relevant empirical evidence
    evidence_context = []
    
    # Financial data
    pl_csv = read_text(EVIDENCE_DIR / "financials" / "pl.csv")
    if pl_csv:
        evidence_context.append(f"--- EVIDENCE: pl.csv (First 50 lines) ---\n" + "\n".join(pl_csv.splitlines()[:50]))
    
    # Diligence interview notes
    diligence_notes = read_text(EVIDENCE_DIR / "diligence" / "lilycorp_site_visit_notes_2026-09-09.md")
    if diligence_notes:
        evidence_context.append(f"--- EVIDENCE: Site Visit Diligence Notes ---\n" + diligence_notes[:4000])

    # Communications
    sba_mail = read_text(EVIDENCE_DIR / "communications" / "bob_financing_reply.txt")
    if sba_mail:
        evidence_context.append(f"--- EVIDENCE: Bob Financing Reply ---\n" + sba_mail)
    
    marcelo_mail = read_text(EVIDENCE_DIR / "communications" / "marcelo_email_reply.txt")
    if marcelo_mail:
        evidence_context.append(f"--- EVIDENCE: Marcelo Add-Back Schedule Reply ---\n" + marcelo_mail)

    # Add assumed capital baseline and graveyard context
    capital_baseline = read_text(PLAN_DIR / "00_assumed_capital_baseline.md")
    if capital_baseline:
        evidence_context.append(f"--- FIXED OPERATING BASELINE: 00_assumed_capital_baseline.md ---\n" + capital_baseline)

    graveyard_content = read_text(PLAN_DIR / "graveyard_rejected_ideas.md")
    if graveyard_content:
        evidence_context.append(f"--- REJECTED STRATEGIES & AUTOPSIES ---\n" + graveyard_content)

    target_plan_path = BASE_DIR / target["target_plan_file"]
    existing_plan_content = read_text(target_plan_path)

    # 4. Draft refinement with Gemini 3.8 Flash & Google Search Grounding
    prompt_draft = f"""
You are the Turnaround Operator, Chief Product Officer, and Growth Architect for Jack Fay, who is acquiring and taking over Lily Corporation (Aurora, IL), a 44-year-old manufacturer of heavy-duty chemical injection equipment and custom molded accessories.

CONTEXT:
The acquisition capital structure is FIXED and ASSUMED (see 00_assumed_capital_baseline.md). Do NOT spend time debating pre-deal senior debt sizing or financing structures. 

YOUR MISSION:
Focus 100% on TAKING OVER, OPERATING, AND TRANSFORMING LILY CORP into a high-margin, scalable manufacturing and distribution powerhouse.
Research markets, invent/validate new product lines, build operational automations, establish commercial distribution channels (e.g. Sika, Euclid, White Cap, IDOT), and author Jack Fay's concrete operator playbook.

YOUR IMMEDIATE TASK:
Draft or rigorously update the plan module: `{target['target_plan_file']}` to solve this specific frontier item:
ITEM ID: {target['id']}
TITLE: {target['title']}
QUESTION: {target['question']}
KNOWN FACTS: {json.dumps(target.get('known_facts', []))}
OPEN UNCERTAINTIES: {json.dumps(target.get('open_uncertainties', []))}

USER STEERING NOTES (From Jack Fay):
{inbox_notes if inbox_notes else "None"}

EXISTING PLAN MODULE CONTENT:
{existing_plan_content if existing_plan_content else "[EMPTY - CREATE INITIAL DRAFT]"}

AVAILABLE EVIDENCE & BASELINE:
{chr(10).join(evidence_context)}

CRITICAL OPERATING CONSTRAINTS:
1. Grounded in Lily's Physical Reality: Lily has 4 shop staff (Dave J, Dave K, Julian, Maggie) and 10 proprietary injection molds in Aurora, IL. Respect shop floor throughput and do not assume unrealistic capex.
2. Civil Contractor Truth: Civil bridge and concrete contractors buy on Net 30/60 against purchase orders. They hate forced web logins. Meet them through Dave J's phone desk, jobsite QR codes, and distributor branches.
3. High Gross Margins: Protect and expand Lily's core profit engine (~65-70%+ on molded ports, caps, and mixers).
4. Ruthless Rejection: If an adjacent market or product line is evaluated and found unviable (excessive capex, hazmat freight liability, contractor rejection), explicitly document why it should be REJECTED and propose the grounded alternative.
5. Output the COMPLETE markdown content for `{target['target_plan_file']}`.
"""

    print("Generating grounded growth plan & market research with Google Search...")
    response_draft = client.models.generate_content(
        model=model_name,
        contents=prompt_draft,
        config={"tools": [{"google_search": {}}]}
    )
    draft_content = response_draft.text.strip()
    if draft_content.startswith("```markdown"):
        draft_content = draft_content[11:]
    if draft_content.startswith("```"):
        draft_content = draft_content[3:]
    if draft_content.endswith("```"):
        draft_content = draft_content[:-3]
    draft_content = draft_content.strip()

    # 5. Adversarial Red-Team Committee Review & Frontier Expansion
    print("Running Product & Operations Review Committee...")
    prompt_critique = f"""
You are the Executive Operating & Product Committee for Lily Corporation, consisting of:
1. Shop Floor & Manufacturing Feasibility (Dave Kling & Bob Trout): Can our 4-person shop in Aurora fabricate/assemble this with our existing CNC, welding, and 10 injection molds without a massive capex spend? Does it cause shop floor chaos?
2. Contractor & Customer Adoption Realist (Dave Jepsen): Will civil bridge and concrete contractors actually buy and spec this? Does it fit how general contractors procure equipment and consumables?
3. Unit Economics & Margin Specialist: Does this protect Lily's ~65-70% gross margins on accessories and drive real incremental EBITDA?
4. Competitive Moat vs Graco & ChemCo: Is this truly differentiated, or are we walking into a commodity trap?

Review the proposed draft for `{target['target_plan_file']}`:

PROPOSED DRAFT:
{draft_content}

FRONTIER EXPANSION TASK:
Identify 1 to 2 NEW, high-leverage market research questions, product line extensions, or operational automations that this investigation exposed.

OUTPUT FORMAT (JSON ONLY):
{{
  "approved": true / false,
  "confidence_score": 1-10,
  "shop_floor_critique": "...",
  "contractor_adoption_critique": "...",
  "unit_economics_critique": "...",
  "competitive_moat_critique": "...",
  "required_revisions": ["..."],
  "summary_verdict": "...",
  "spawned_frontier_items": [
    {{
      "category": "Market Expansion | Product Innovation | Operations | Commercial Strategy | Operator Guide",
      "title": "Short descriptive title",
      "question": "Precise, falsifiable market or operational question",
      "priority": "CRITICAL" | "HIGH" | "MEDIUM",
      "target_plan_file": "plan/01_market_expansion_and_adjacent_verticals.md | plan/02_product_lines_and_rd_pipeline.md | plan/03_commercial_distribution_and_partnerships.md | plan/04_shop_floor_modernization_and_capacity.md | plan/05_jack_fay_operator_guide.md | plan/06_risk_register_and_kill_switches.md"
    }}
  ]
}}
"""

    response_critique = client.models.generate_content(
        model=model_name,
        contents=prompt_critique,
        config=types.GenerateContentConfig(
            response_mime_type="application/json"
        )
    )

    try:
        critique_result = json.loads(response_critique.text.strip())
    except Exception as e:
        print(f"Error parsing critique JSON: {e}\nRaw output: {response_critique.text}")
        critique_result = {"approved": True, "confidence_score": 6, "summary_verdict": "Auto-accepted with warning", "spawned_frontier_items": []}

    print(f"Verdict: Approved={critique_result.get('approved')}, Score={critique_result.get('confidence_score')}/10")
    print(f"Summary: {critique_result.get('summary_verdict')}")

    # 6. Dynamically Expand Frontier with newly spawned second-order questions
    spawned = critique_result.get("spawned_frontier_items", [])
    existing_questions = {item.get("question", "").strip().lower() for item in frontier_data.get("frontier", [])}
    existing_titles = {item.get("title", "").strip().lower() for item in frontier_data.get("frontier", [])}
    
    new_spawns_count = 0
    for s in spawned:
        q_text = s.get("question", "").strip()
        t_text = s.get("title", "").strip()
        if not q_text or q_text.lower() in existing_questions or t_text.lower() in existing_titles:
            continue
        
        # Generate clean ID
        cat_prefix = s.get("category", "DEAL")[:4].upper().replace(" ", "_")
        spawn_id = f"{cat_prefix}_{len(frontier_data.get('frontier', [])) + 1:02d}"
        
        new_frontier_item = {
            "id": spawn_id,
            "category": s.get("category", "Diligence & Operations"),
            "title": t_text,
            "question": q_text,
            "known_facts": [f"Uncovered during Cycle #{cycle_num} investigation of [{target['id']}]."],
            "open_uncertainties": [q_text],
            "target_plan_file": s.get("target_plan_file", target["target_plan_file"]),
            "confidence_score": 3,
            "status": "OPEN",
            "priority": s.get("priority", "HIGH")
        }
        frontier_data.setdefault("frontier", []).append(new_frontier_item)
        existing_questions.add(q_text.lower())
        existing_titles.add(t_text.lower())
        new_spawns_count += 1
        print(f"  [+] Spawned New Frontier Item: [{spawn_id}] {t_text}")

    # 7. Apply verdict
    if critique_result.get("approved"):
        # Write to plan file
        write_text(target_plan_path, draft_content)
        print(f"Updated plan module: {target['target_plan_file']}")

        # Update target frontier status
        target["confidence_score"] = critique_result.get("confidence_score", target.get("confidence_score", 5) + 1)
        if target["confidence_score"] >= 8:
            target["status"] = "RESOLVED"
        else:
            target["status"] = "REFINED"
        save_frontier(frontier_data)

        # Update steering digest
        digest_content = (
            f"# Autonomous Diligence & Business Plan Digest\n"
            f"*Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n\n"
            f"## Status Overview\n"
            f"- **Active Cycle:** {cycle_num}\n"
            f"- **Latest Refined Module:** `{target['target_plan_file']}`\n"
            f"- **Confidence Score:** {critique_result.get('confidence_score')}/10\n"
            f"- **Total Backlog Items:** {len(frontier_data['frontier'])} ({new_spawns_count} newly spawned)\n"
            f"- **Committee Verdict:** {critique_result.get('summary_verdict')}\n\n"
            f"## Product & Operating Committee Perspectives\n"
            f"* **Shop Floor Feasibility (Dave K/Bob):** {critique_result.get('shop_floor_critique', 'N/A')}\n"
            f"* **Contractor Adoption (Dave J):** {critique_result.get('contractor_adoption_critique', 'N/A')}\n"
            f"* **Unit Economics & Margin:** {critique_result.get('unit_economics_critique', 'N/A')}\n"
            f"* **Competitive Moat:** {critique_result.get('competitive_moat_critique', 'N/A')}\n"
        )
        write_text(DIGEST_FILE, digest_content)

        # Commit changes
        git_commit(f"Auto-Plan Cycle #{cycle_num}: Refined [{target['id']}] in {target['target_plan_file']}")
    else:
        # Log rejection
        rejection_entry = (
            f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Cycle #{cycle_num} REJECTED for {target['id']}:\n"
            f"Verdict: {critique_result.get('summary_verdict')}\n"
            f"Revisions: {critique_result.get('required_revisions')}\n\n"
        )
        existing_rejections = read_text(REJECTIONS_LOG)
        write_text(REJECTIONS_LOG, existing_rejections + rejection_entry)
        target["status"] = "OPEN"
        save_frontier(frontier_data)
        print(f"Cycle #{cycle_num} proposed changes rejected by committee and logged to state/rejections.log.")


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Lily Corp Recursive Business Plan Engine")
    parser.add_argument("--once", action="store_true", help="Run a single cycle and exit")
    parser.add_argument("--interval", type=int, default=600, help="Loop interval in seconds (default: 600s / 10m)")
    args = parser.parse_args()

    client = get_genai_client()

    if args.once:
        execute_cycle(client)
    else:
        print(f"Starting continuous recursive engine (Interval: {args.interval}s)...")
        while True:
            try:
                execute_cycle(client)
            except Exception as e:
                print(f"Error during cycle execution: {e}")
            print(f"Sleeping for {args.interval} seconds until next cycle...\n")
            time.sleep(args.interval)


if __name__ == "__main__":
    main()
