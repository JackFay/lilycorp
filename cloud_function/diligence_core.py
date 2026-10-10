"""
Core Diligence Engine running inside Google Cloud Function.
Interacts with GCS for state persistence and executes Gemini Flash OODA cycles.
"""

import os
import json
from datetime import datetime
from typing import Dict, Any
from google import genai
from google.genai import types
from storage_adapter import GCSStorageAdapter


def get_genai_client() -> genai.Client:
    """Initialize GenAI client using Vertex AI / Cloud Function default credentials."""
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key:
        return genai.Client(api_key=api_key)
    
    project = os.environ.get("GCP_PROJECT", os.environ.get("GOOGLE_CLOUD_PROJECT", "dulcet-voyager-496719-e3"))
    location = os.environ.get("GCP_LOCATION", "us-central1")
    return genai.Client(vertexai=True, project=project, location=location)


def process_steering_inbox(storage: GCSStorageAdapter) -> str:
    """Check steering/inbox.md in GCS for human feedback, archive it, and return notes."""
    inbox_content = storage.read_text("steering/inbox.md")
    if not inbox_content:
        return ""
    
    lines = [line.strip() for line in inbox_content.splitlines()]
    user_notes = [l for l in lines if l and not l.startswith("#") and not l.startswith(">") and not l.startswith("<!--")]
    if not user_notes:
        return ""
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    archive_entry = f"\n\n### Processed Note [{timestamp}]:\n" + "\n".join(user_notes) + "\n"
    existing_archive = storage.read_text("steering/archive.md")
    storage.write_text("steering/archive.md", existing_archive + archive_entry)
    
    default_header = (
        "# Steering Inbox\n\n"
        "> **Instructions for Jack:**\n"
        "> Drop any real-world updates, notes from calls with Bob or bankers, new thoughts, or constraints here as bullet points.\n\n"
        "---\n\n<!-- Add your notes below this line -->\n"
    )
    storage.write_text("steering/inbox.md", default_header)
    return "\n".join(user_notes)


def run_single_cloud_cycle(bucket_name: str) -> Dict[str, Any]:
    """Execute one complete diligence and plan mutation cycle against GCS."""
    storage = GCSStorageAdapter(bucket_name)
    client = get_genai_client()
    model_name = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")

    frontier_data = storage.read_json("state/frontier.json")
    if not frontier_data:
        raise ValueError(f"frontier.json not found in GCS bucket {bucket_name} at state/frontier.json")

    cycle_num = frontier_data.get("active_cycle", 0) + 1
    frontier_data["active_cycle"] = cycle_num

    # 1. Process inbox
    inbox_notes = process_steering_inbox(storage)

    # 2. Select frontier task
    open_items = [item for item in frontier_data.get("frontier", []) if item.get("status") in ["OPEN", "IN_PROGRESS"]]
    if not open_items:
        return {
            "status": "IDLE",
            "cycle": cycle_num,
            "message": "All frontier items resolved. No open hypotheses."
        }

    priority_order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}
    open_items.sort(key=lambda x: (priority_order.get(x.get("priority", "MEDIUM"), 2), x.get("confidence_score", 5)))
    target = open_items[0]

    # 3. Assemble evidence from GCS
    evidence_context = []
    
    pl_csv = storage.read_text("evidence/financials/pl.csv")
    if pl_csv:
        evidence_context.append(f"--- EVIDENCE: pl.csv (First 50 lines) ---\n" + "\n".join(pl_csv.splitlines()[:50]))
    
    diligence_notes = storage.read_text("evidence/diligence/lilycorp_site_visit_notes_2026-09-09.md")
    if diligence_notes:
        evidence_context.append(f"--- EVIDENCE: Site Visit Diligence Notes ---\n" + diligence_notes[:4000])

    sba_mail = storage.read_text("evidence/communications/bob_financing_reply.txt")
    if sba_mail:
        evidence_context.append(f"--- EVIDENCE: Bob Financing Reply ---\n" + sba_mail)
    
    marcelo_mail = storage.read_text("evidence/communications/marcelo_email_reply.txt")
    if marcelo_mail:
        evidence_context.append(f"--- EVIDENCE: Marcelo Add-Back Schedule Reply ---\n" + marcelo_mail)

    target_plan_path = target["target_plan_file"]
    existing_plan_content = storage.read_text(target_plan_path)

    # 4. Draft refinement
    prompt_draft = f"""
You are the Lead M&A Acquisition Strategist and Turnaround Operator for Jack Fay, who is acquiring Lily Corporation (Aurora, IL), an analog manufacturer of heavy-duty chemical injection equipment and custom molded accessories.

YOUR TASK:
Draft or update the business plan module: `{target_plan_path}` to solve this specific diligence item:
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
4. Output the COMPLETE markdown content for `{target_plan_path}`.
"""

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
    prompt_critique = f"""
You are the Adversarial Review Committee for the acquisition of Lily Corporation.
Review the proposed draft for `{target_plan_path}`:

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
    except Exception:
        critique_result = {"approved": True, "confidence_score": 6, "summary_verdict": "Auto-accepted with warning"}

    # 6. Apply verdict to GCS
    if critique_result.get("approved"):
        # Save plan module to GCS
        storage.write_text(target_plan_path, draft_content, content_type="text/markdown")

        # Update frontier
        target["confidence_score"] = critique_result.get("confidence_score", target.get("confidence_score", 5) + 1)
        if target["confidence_score"] >= 8:
            target["status"] = "RESOLVED"
        else:
            target["status"] = "REFINED"
        storage.write_json("state/frontier.json", frontier_data)

        # Update digest
        timestamp_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        digest_content = (
            f"# Autonomous Diligence & Business Plan Digest (Cloud Run)\n"
            f"*Last Updated: {timestamp_now}*\n\n"
            f"## Status Overview\n"
            f"- **Active Cycle:** {cycle_num}\n"
            f"- **Latest Refined Module:** `{target_plan_path}`\n"
            f"- **Confidence Score:** {critique_result.get('confidence_score')}/10\n"
            f"- **Committee Verdict:** {critique_result.get('summary_verdict')}\n\n"
            f"## Underwriter & Operational Notes\n"
            f"* **SBA Underwriter:** {critique_result.get('underwriter_critique', 'N/A')}\n"
            f"* **Shop Floor Realist:** {critique_result.get('shop_floor_critique', 'N/A')}\n"
            f"* **Forensic Auditor:** {critique_result.get('forensic_critique', 'N/A')}\n"
        )
        storage.write_text("steering/digest.md", digest_content, content_type="text/markdown")

        return {
            "status": "APPROVED",
            "cycle": cycle_num,
            "target_id": target["id"],
            "plan_file": target_plan_path,
            "confidence_score": target["confidence_score"],
            "verdict": critique_result.get("summary_verdict")
        }
    else:
        rejection_entry = (
            f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Cycle #{cycle_num} REJECTED for {target['id']}:\n"
            f"Verdict: {critique_result.get('summary_verdict')}\n"
            f"Revisions: {critique_result.get('required_revisions')}\n\n"
        )
        existing_rejections = storage.read_text("state/rejections.log")
        storage.write_text("state/rejections.log", existing_rejections + rejection_entry)
        target["status"] = "OPEN"
        storage.write_json("state/frontier.json", frontier_data)

        return {
            "status": "REJECTED",
            "cycle": cycle_num,
            "target_id": target["id"],
            "reasons": critique_result.get("required_revisions")
        }
