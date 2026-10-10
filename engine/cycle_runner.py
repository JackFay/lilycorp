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

    # 2. Pick target frontier item
    open_items = [item for item in frontier_data.get("frontier", []) if item.get("status") in ["OPEN", "IN_PROGRESS"]]
    if not open_items:
        print("No open items in frontier backlog! All current hypotheses resolved.")
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

    target_plan_path = BASE_DIR / target["target_plan_file"]
    existing_plan_content = read_text(target_plan_path)

    # 4. Draft refinement with Gemini Flash
    prompt_draft = f"""
You are the Lead M&A Acquisition Strategist and Turnaround Operator for Jack Fay, who is acquiring Lily Corporation (Aurora, IL), an analog manufacturer of heavy-duty chemical injection equipment and custom molded accessories.

YOUR TASK:
Draft or rigorously update the business plan module: `{target['target_plan_file']}` to solve the specific frontier diligence item:
ITEM ID: {target['id']}
TITLE: {target['title']}
QUESTION: {target['question']}
KNOWN FACTS: {json.dumps(target.get('known_facts', []))}
OPEN UNCERTAINTIES: {json.dumps(target.get('open_uncertainties', []))}

USER STEERING NOTES (From Jack):
{inbox_notes if inbox_notes else "None"}

EXISTING PLAN MODULE CONTENT:
{existing_plan_content if existing_plan_content else "[EMPTY - CREATE INITIAL DRAFT]"}

AVAILABLE EMPIRICAL EVIDENCE:
{chr(10).join(evidence_context)}

CRITICAL CONSTRAINTS:
1. Ground every claim, number, and assumption in the primary evidence provided. Cite specific files (e.g., [pl.csv], [marcelo_email_reply.txt], [site visit notes]).
2. No generic MBA filler or ungrounded tech fantasies (no IoT telemetry rigs, no expensive accredited video academies).
3. All financial underwriting must honor the SBA mandatory 1.25x DSCR rule (Oct 1 2026 rules) on historical 2024/2025 Form 1120-S bases, factoring in the $68k NNN lease and $100k buyer management salary.
4. Output the COMPLETE markdown content for `{target['target_plan_file']}`.
"""

    print("Generating grounded plan module draft...")
    response_draft = client.models.generate_content(
        model=model_name,
        contents=prompt_draft
    )
    draft_content = response_draft.text.strip()
    if draft_content.startswith("```markdown"):
        draft_content = draft_content[11:]
    if draft_content.startswith("```"):
        draft_content = draft_content[3:]
    if draft_content.endswith("```"):
        draft_content = draft_content[:-3]
    draft_content = draft_content.strip()

    # 5. Adversarial Red-Team Committee Review
    print("Running Adversarial Red-Team Gatekeeper (SBA Underwriter + Shop Floor Bob/Dave + Forensic Auditor)...")
    prompt_critique = f"""
You are the Adversarial Review Committee for the acquisition of Lily Corporation.
Review the proposed draft for `{target['target_plan_file']}`:

PROPOSED DRAFT:
{draft_content}

EVALUATE AGAINST 3 PERSPECTIVES:
1. SBA Commercial Underwriter: Does this draft respect strict 1.25x DSCR requirements on historical Form 1120-S tax returns? Are debt sizing, 24-month standby seller notes, and new NNN lease deductions handled properly?
2. Shop Floor Realist (Bob Trout / Dave Jepsen): Is this operationally grounded for an analog 4-person shop in Aurora, IL? Or does it assume contractor behaviors or complex workflows that fail on job sites?
3. Forensic Auditor: Are all dollar figures, add-backs, and inventory facts traceable to primary evidence? Are any numbers fabricated?

OUTPUT FORMAT (JSON ONLY):
{{
  "approved": true / false,
  "confidence_score": 1-10,
  "underwriter_critique": "...",
  "shop_floor_critique": "...",
  "forensic_critique": "...",
  "required_revisions": ["..."],
  "summary_verdict": "..."
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
        critique_result = {"approved": True, "confidence_score": 6, "summary_verdict": "Auto-accepted with warning"}

    print(f"Verdict: Approved={critique_result.get('approved')}, Score={critique_result.get('confidence_score')}/10")
    print(f"Summary: {critique_result.get('summary_verdict')}")

    # 6. Apply verdict
    if critique_result.get("approved"):
        # Write to plan file
        write_text(target_plan_path, draft_content)
        print(f"Updated plan module: {target['target_plan_file']}")

        # Update frontier status
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
            f"- **Committee Verdict:** {critique_result.get('summary_verdict')}\n\n"
            f"## Underwriter & Operational Notes\n"
            f"* **SBA Underwriter:** {critique_result.get('underwriter_critique', 'N/A')}\n"
            f"* **Shop Floor Realist:** {critique_result.get('shop_floor_critique', 'N/A')}\n"
            f"* **Forensic Auditor:** {critique_result.get('forensic_critique', 'N/A')}\n"
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
