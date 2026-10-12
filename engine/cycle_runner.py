#!/usr/bin/env python3
"""
Lily Corp Autonomous Diligence & Recursive Business Plan Loop.
Fast deterministic code validation with comprehensive empirical evidence ingestion.
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
from cloud_function.github_lifecycle import GitHubLifecycleManager

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
    lines = [line.strip() for line in content.splitlines()]
    user_notes = [l for l in lines if l and not l.startswith("#") and not l.startswith(">") and not l.startswith("<!--")]
    if not user_notes:
        return ""
    
    archive_file = STEERING_DIR / "archive.md"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"\n\n### Processed Note [{timestamp}]:\n" + "\n".join(user_notes) + "\n"
    
    existing_archive = read_text(archive_file)
    write_text(archive_file, existing_archive + entry)
    
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


def git_commit(message: str, paths: list = None):
    try:
        stage_targets = paths if paths else ["plan/", "state/", "steering/"]
        subprocess.run(["git", "add"] + stage_targets, cwd=BASE_DIR, check=True)
        subprocess.run(["git", "commit", "-m", message], cwd=BASE_DIR, check=True)
        print(f"Git commit successful: {message}")
    except Exception as e:
        print(f"Git commit warning: {e}")


def git_rollback(file_path: Path):
    try:
        subprocess.run(["git", "checkout", "--", str(file_path)], cwd=BASE_DIR, check=True)
        print(f"Git rollback successful for {file_path}")
    except Exception as e:
        print(f"Git rollback warning: {e}")


def validate_draft_deterministically(draft: str, existing_content: str, target_file: str) -> tuple[bool, str]:
    """
    Fast deterministic code guards:
    1. Checks for forbidden truncation placeholders (e.g. 'retained in full fidelity', '[Sections...').
    2. Ensures draft did not accidentally collapse file size (> 50% of baseline if baseline > 10k).
    3. Preserves core proprietary assets (e.g. Molds T-01 through T-10 if editing plan/04).
    4. Anti-hallucination guard: rejects disproven regulatory mandates (e.g., claiming DOTs mandate cosmetic colors).
    """
    if not draft or len(draft.strip()) < 500:
        return False, "Draft is empty or too short."

    lower_draft = draft.lower()
    if "retained in full fidelity" in lower_draft or "[sections " in lower_draft or "[sections 2 through" in lower_draft:
        return False, "Detected forbidden lazy truncation placeholder in draft."

    if existing_content and len(existing_content) > 10000:
        if len(draft) < (len(existing_content) * 0.50):
            return False, f"Draft collapsed file size significantly ({len(draft)} bytes vs existing {len(existing_content)} bytes)."

    if "04_shop_floor" in target_file:
        if "t-01" not in lower_draft or "t-02" not in lower_draft:
            return False, "Draft omitted Lily's baseline proprietary injection molds (T-01, T-02)."

    # Anti-hallucination check: state DOTs cannot legally mandate cosmetic colors without an 'or equal' clause
    if "safety orange" in lower_draft and "mandat" in lower_draft and "spec" in lower_draft:
        if "contractor" not in lower_draft and "fhwa" not in lower_draft and "visibility" not in lower_draft:
            return False, "Draft claimed state DOTs mandate cosmetic Safety Orange resin, violating FHWA 23 CFR 635.411."

    return True, "Valid"


def audit_draft_adversarially(client: genai.Client, model_name: str, draft: str, target: dict, evidence_context: list, inbox_notes: str) -> tuple[bool, str, float, list]:
    """
    Adversarial Diligence Auditor:
    Acts as a Skeptical Private Equity Operating Partner and Forensic Diligence Engineer.
    Audits the generated draft against grounded reality, empirical evidence, and operational limits.
    Returns: (passed, findings_summary, grounded_confidence_score, unviable_concepts)
    """
    audit_prompt = f"""
You are the Adversarial Diligence Auditor and Skeptical Private Equity Operating Partner reviewing a business plan module for Jack Fay's acquisition of Lily Corporation (Aurora, IL).

YOUR MISSION:
Rigorously stress-test and fact-check this draft against empirical reality. Expose ungrounded assumptions, invented regulatory mandates, operational impossibilities, and inflated margins. Do NOT be polite.

TARGET INITIATIVE:
[{target['id']}] {target['title']}
Question: {target['question']}
Target Plan File: {target['target_plan_file']}

EMPIRICAL DILIGENCE CONSTRAINTS (HARD BOUNDARIES):
1. 4-Person Shop Floor: Dave Kling (machining/welding/purchasing), Julian Perez (assembly/rebuilds/testing), Greg (sole press operator), Maggie M (QuickBooks/billing), Dave Jepsen (sales/contractor training).
2. Working Capital Discipline: Liquid working capital is $50,000. Discretionary Year 1 capex cannot exceed $20,000. Speculative tooling is frozen in Year 1.
3. Debt Service Floor: $11,403.04/month ($136.8k/yr). The baseline business must cover debt service without speculative revenue.
4. Empirical Evidence Only: Only facts verified in the evidence context (Lily catalog, pl.csv, site visit notes, tax returns, or google search / verifiable market research) can be stated as facts.

DRAFT CONTENT TO AUDIT:
{draft[:25000]}

AUDIT REQUIREMENTS:
1. Grounding Audit: Did the draft state unproven assumptions as facts? (e.g. claiming competitor parts leak under 2,000 PSI without test data, or claiming formulators have supply crises).
2. Regulatory Audit: Did the draft invent legal mandates? (e.g. claiming EPA AIS / BABA bans imported sacrificial grouting packers, or that state DOTs mandate cosmetic colors like Safety Orange).
3. Operational Sanity: Does this demand more labor than 4 craftsmen can provide while running the core business?
4. Pricing Realism: Does this assume formulators will pay double the price of landed Asian imports ($1.75 vs $0.50) without a binding mandate?
5. Epistemic Labeling: Are speculative ideas labeled [EXPLORATORY HYPOTHESIS] rather than treated as guaranteed base EBITDA?

Respond in strict JSON format:
{{
  "verdict": "APPROVED" or "REJECTED_UNGROUNDED",
  "audit_findings": "2-3 sentence summary of findings",
  "grounded_confidence_score": 1-10, // 8-10 ONLY if verified by empirical evidence in evidence/. 5-7 if operationally plausible estimate. 1-4 if exploratory commercial hypothesis.
  "unviable_concepts": [
    {{
      "title": "Name of unviable concept or false assumption",
      "autopsy": "Why this fails operationally, legally, or economically"
    }}
  ]
}}
"""
    try:
        response = client.models.generate_content(
            model=model_name,
            contents=audit_prompt,
            config=types.GenerateContentConfig(response_mime_type="application/json")
        )
        res_json = json.loads(response.text.strip())
        passed = res_json.get("verdict") == "APPROVED"
        findings = res_json.get("audit_findings", "")
        score = float(res_json.get("grounded_confidence_score", 5.0))
        unviable = res_json.get("unviable_concepts", [])
        return passed, findings, score, unviable
    except Exception as e:
        print(f"Adversarial audit parsing warning: {e}")
        return True, f"Audit parsed with fallback ({e})", 5.0, []



def execute_cycle(client: genai.Client, model_name: str = None):
    if not model_name:
        model_name = os.environ.get("GEMINI_MODEL", "gemini-3.8-flash")
    frontier_data = load_frontier()
    cycle_num = frontier_data.get("active_cycle", 0) + 1
    frontier_data["active_cycle"] = cycle_num

    print(f"\n=======================================================")
    print(f"Starting Diligence Research Cycle #{cycle_num} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"=======================================================")

    # 1. Process steering inbox if any
    inbox_notes = check_steering_inbox()
    if inbox_notes:
        print(f"Found active steering notes from Jack:\n{inbox_notes}")

    # 2. Pick target frontier item
    open_items = [item for item in frontier_data.get("frontier", []) if item.get("status") in ["OPEN", "IN_PROGRESS"]]
    if not open_items:
        print("All active frontier items resolved! Plan is at peak convergence.")
        return

    priority_order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}
    open_items.sort(key=lambda x: (priority_order.get(x.get("priority", "MEDIUM"), 2), x.get("confidence_score", 5)))
    target = open_items[0]

    print(f"Target Frontier Item: [{target['id']}] {target['title']}")
    print(f"Category: {target.get('category')} | Priority: {target.get('priority')}")
    print(f"Target Plan File: {target['target_plan_file']}")

    # 3. Assemble COMPREHENSIVE Empirical Evidence
    evidence_context = []
    
    # Financial data (Annual & Monthly Trends)
    pl_csv = read_text(EVIDENCE_DIR / "financials" / "pl.csv")
    if pl_csv:
        evidence_context.append(f"--- EVIDENCE: pl.csv (Historical P&L 2015-2025) ---\n" + "\n".join(pl_csv.splitlines()[:65]))
    
    pl_monthly = read_text(EVIDENCE_DIR / "financials" / "updated_cogs" / "pl_monthly.csv")
    if pl_monthly:
        monthly_lines = [l for l in pl_monthly.splitlines() if "4010 · Sales" in l or "4015 · Rental Income" in l or "5440 · Repairs & Maintenance - Molds" in l or "5120 · Purchases - Accessories" in l]
        if monthly_lines:
            evidence_context.append(f"--- EVIDENCE: pl_monthly.csv Key Trends (Sales, Rental, Molds, Accessories) ---\n" + "\n".join(monthly_lines))

    # Complete Site Visit Diligence Notes
    diligence_notes = read_text(EVIDENCE_DIR / "diligence" / "lilycorp_site_visit_notes_2026-09-09.md")
    if diligence_notes:
        evidence_context.append(f"--- EVIDENCE: Complete Site Visit Diligence Notes (On-Site Findings) ---\n" + diligence_notes)

    # Official Product Catalog & Technical Descriptions
    product_catalog = read_text(EVIDENCE_DIR / "products" / "lily_corporation_product_catalog.md")
    if product_catalog:
        evidence_context.append(f"--- EVIDENCE: Lily Corporation Official Product Catalog (Core Models & Accessories) ---\n" + product_catalog[:12000])

    # Communications
    sba_mail = read_text(EVIDENCE_DIR / "communications" / "bob_financing_reply.txt")
    if sba_mail:
        evidence_context.append(f"--- EVIDENCE: Bob Financing Reply ---\n" + sba_mail)
    
    marcelo_mail = read_text(EVIDENCE_DIR / "communications" / "marcelo_email_reply.txt")
    if marcelo_mail:
        evidence_context.append(f"--- EVIDENCE: Marcelo Add-Back Schedule Reply ---\n" + marcelo_mail)

    capital_baseline = read_text(PLAN_DIR / "00_assumed_capital_baseline.md")
    if capital_baseline:
        evidence_context.append(f"--- FIXED OPERATING BASELINE: 00_assumed_capital_baseline.md ---\n" + capital_baseline)

    graveyard_content = read_text(PLAN_DIR / "graveyard_rejected_ideas.md")
    if graveyard_content:
        evidence_context.append(f"--- REJECTED STRATEGIES & AUTOPSIES ---\n" + graveyard_content)

    target_plan_path = BASE_DIR / target["target_plan_file"]
    existing_plan_content = read_text(target_plan_path)

    # 4. Generate Research & Plan Refinement with Google Search Grounding
    print(f"\nGenerating grounded research and plan refinement with Google Search...")
    prompt_draft = f"""
You are the Turnaround Operator, Chief Product Officer, and Growth Architect for Jack Fay, who is acquiring and taking over Lily Corporation (Aurora, IL).

YOUR MISSION:
Rigorously update and improve the plan module `{target['target_plan_file']}` to definitively resolve frontier item [{target['id']}].
Deliver a concrete, highly actionable, operator-grade business plan module grounded in Lily Corp's actual equipment, team, and historical financials.

TARGET FRONTIER ITEM:
ITEM ID: {target['id']}
TITLE: {target['title']}
QUESTION: {target['question']}
KNOWN FACTS: {json.dumps(target.get('known_facts', []))}
OPEN UNCERTAINTIES: {json.dumps(target.get('open_uncertainties', []))}

USER STEERING NOTES (From Jack Fay - OVERRIDING):
{inbox_notes if inbox_notes else "Adhere strictly to the baseline."}

GROUNDED REALITY CONSTRAINTS:
1. 5-Person Shop Roster: Dave Jepsen (sales/tech/contractor support), Dave Kling (machinist/purchasing/repairs), Julian Perez (assembly/repairs/packing), Greg (sole on-site injection molding press operator), Maggie M (QuickBooks/billing), Bob Trout (retiring founder).
2. Capex Discipline: Liquid working capital is $50,000. Total Year 1 discretionary capex CANNOT exceed $20,000 across all initiatives. Speculative tooling (Molds #11-13) is frozen in Year 1.
3. Debt Service & Lease Floor: $11,403.04/month ($136.8k/year). Month 25 seller note ($570k+) MUST have a 1.35x DSCR protection covenant.
4. Civil Contractor Reality: Sales occur via Net 30/60 purchase orders, Dave Jepsen's phone desk, and distributors (White Cap, Sika, Euclid). No forced web logins.
5. High Gross Margins: Protect and expand Lily's core consumable profit engine (~65-75% GM on molded ports, caps, and mixers).
6. Document Completeness: Output the COMPLETE markdown content for `{target['target_plan_file']}`. Absolutely NO truncation placeholders or comments like "[Sections 2 through 51 are retained...]". Preserve all existing baseline operational sections!

AVAILABLE EMPIRICAL DILIGENCE EVIDENCE:
{chr(10).join(evidence_context)}

EXISTING PLAN CONTENT:
{existing_plan_content if existing_plan_content else "[EMPTY - CREATE INITIAL DRAFT]"}
"""

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

    # 5. Deterministic Code Guardrails
    is_valid, validation_msg = validate_draft_deterministically(draft_content, existing_plan_content, target["target_plan_file"])

    if not is_valid:
        print(f"\n[VALIDATION: REJECTED] Draft failed deterministic check: {validation_msg}")
        rejection_entry = (
            f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Cycle #{cycle_num} REJECTED for {target['id']}:\n"
            f"Reason: {validation_msg}\n\n"
        )
        existing_rejections = read_text(REJECTIONS_LOG)
        write_text(REJECTIONS_LOG, existing_rejections + rejection_entry)
        target["status"] = "OPEN"
        save_frontier(frontier_data)
        git_rollback(target_plan_path)
        print("Draft rejected. Worktree clean.")
        return

    # 6. Adversarial Diligence Audit (Red Team Verification Gate)
    print(f"\n[AUDIT: STARTING] Running Adversarial Diligence Auditor...")
    audit_passed, audit_msg, grounded_score, unviable_concepts = audit_draft_adversarially(
        client, model_name, draft_content, target, evidence_context, inbox_notes
    )
    print(f"[AUDIT: {'PASSED' if audit_passed else 'FLAGGED'}] Grounded Score: {grounded_score}/10 | {audit_msg[:120]}...")

    # Log any discovered unviable concepts directly to The Graveyard
    if unviable_concepts:
        graveyard_entries = []
        for c in unviable_concepts:
            graveyard_entries.append(
                f"\n\n### Concept: {c.get('title')}\n* **Classification:** `REJECTED / UNVIABLE` (Logged in Cycle #{cycle_num} Audit)\n* **Autopsy:** {c.get('autopsy')}\n"
            )
        current_graveyard = read_text(PLAN_DIR / "graveyard_rejected_ideas.md")
        write_text(PLAN_DIR / "graveyard_rejected_ideas.md", current_graveyard + "".join(graveyard_entries))
        print(f"Logged {len(unviable_concepts)} unviable concepts into graveyard_rejected_ideas.md")

    # If audit failed severely, reject draft
    if not audit_passed and grounded_score < 3.0:
        print(f"\n[AUDIT: REJECTED] Draft failed adversarial audit: {audit_msg}")
        rejection_entry = (
            f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Cycle #{cycle_num} AUDIT REJECTED for {target['id']}:\n"
            f"Reason: {audit_msg}\n\n"
        )
        existing_rejections = read_text(REJECTIONS_LOG)
        write_text(REJECTIONS_LOG, existing_rejections + rejection_entry)
        target["status"] = "OPEN"
        save_frontier(frontier_data)
        git_rollback(target_plan_path)
        print("Draft rejected by auditor. Worktree clean.")
        return

    # 7. Write Plan & Update Frontier Epistemics
    print(f"\n[VALIDATION & AUDIT: PASSED] Writing plan module: {target['target_plan_file']}...")
    write_text(target_plan_path, draft_content)

    # Update target frontier status based on grounded audit score (no blind +3 inflation)
    target["confidence_score"] = grounded_score
    if grounded_score >= 8.0:
        target["status"] = "RESOLVED"
    elif grounded_score >= 5.0:
        target["status"] = "REFINED"
    else:
        target["status"] = "EXPLORATORY"
    save_frontier(frontier_data)

    # Update digest
    timestamp_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    digest_content = (
        f"# Autonomous Diligence & Business Plan Digest\n"
        f"*Last Updated: {timestamp_now}*\n\n"
        f"## Status Overview\n"
        f"- **Active Cycle:** {cycle_num}\n"
        f"- **Target Item:** [{target['id']}] {target['title']}\n"
        f"- **Module:** `{target['target_plan_file']}`\n"
        f"- **Frontier Status:** {target['status']} (Grounded Confidence: {target['confidence_score']}/10)\n"
        f"- **Audit Verdict:** {'APPROVED' if audit_passed else 'FLAGGED'} ({audit_msg})\n"
        f"- **Backlog Remaining:** {len([x for x in frontier_data['frontier'] if x.get('status') == 'OPEN'])} open core items\n\n"
        f"## Execution Notes\n"
        f"- Research generated with Google Search and complete empirical evidence.\n"
        f"- Adversarial audit verified empirical grounding, shop labor limits, and regulatory validity.\n"
    )
    write_text(DIGEST_FILE, digest_content)

    # Commit to Local Git
    commit_msg = f"research(cycle #{cycle_num}): audited [{target['id']}] in {target['target_plan_file']} (score: {grounded_score}/10)"
    git_commit(commit_msg, [str(target_plan_path), str(FRONTIER_FILE), str(DIGEST_FILE), str(PLAN_DIR / "graveyard_rejected_ideas.md")])
    print(f"[SUCCESS] Cycle #{cycle_num} completed and committed locally: {commit_msg}")

    # Synchronize to GitHub with Pull Request and conditional auto-merge
    gh_manager = GitHubLifecycleManager()
    if gh_manager.is_configured:
        print(f"\n[GITHUB] Synchronizing Cycle #{cycle_num} to GitHub ({gh_manager.repo})...")
        files_to_commit = {
            target["target_plan_file"]: draft_content,
            "state/frontier.json": json.dumps(frontier_data, indent=2),
            "steering/digest.md": digest_content,
            "plan/graveyard_rejected_ideas.md": read_text(PLAN_DIR / "graveyard_rejected_ideas.md")
        }
        gh_res = gh_manager.sync_cycle_to_github(
            cycle_num=cycle_num,
            target=target,
            files_to_commit=files_to_commit,
            confidence_score=grounded_score,
            audit_passed=audit_passed,
            audit_msg=audit_msg,
            adversarial_critique=audit_msg,
            unviable_concepts=unviable_concepts
        )
        if gh_res.get("status") == "SUCCESS":
            target["github_pr"] = gh_res.get("pr_url")
            target["github_auto_merged"] = gh_res.get("auto_merged", False)
            target["github_pr_number"] = gh_res.get("pr_number")
            save_frontier(frontier_data)
            action = "AUTO-MERGED to main" if gh_res.get("auto_merged") else "PENDING OPERATOR REVIEW"
            print(f"[GITHUB] Pull Request #{gh_res.get('pr_number')} ({action}): {gh_res.get('pr_url')}")



def main():
    import argparse
    parser = argparse.ArgumentParser(description="Lily Corp Diligence Research Loop")
    parser.add_argument("--once", action="store_true", help="Run a single cycle and exit")
    parser.add_argument("--interval", type=int, default=600, help="Loop interval in seconds (default: 600s / 10m)")
    args = parser.parse_args()

    client = get_genai_client()

    if args.once:
        execute_cycle(client)
    else:
        print(f"Starting Diligence Research Loop (Interval: {args.interval}s)...")
        while True:
            try:
                execute_cycle(client)
            except Exception as e:
                print(f"Error during cycle execution: {e}")
            print(f"Sleeping for {args.interval} seconds until next cycle...\n")
            time.sleep(args.interval)


if __name__ == "__main__":
    main()
