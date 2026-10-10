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


def spawn_cloud_stress_test(client: genai.Client, model_name: str, frontier_data: dict, storage: GCSStorageAdapter) -> dict:
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
        storage.write_json("state/frontier.json", frontier_data)
        return new_item
    except Exception as e:
        print(f"Error generating cloud stress test: {e}")
        return None


def run_single_cloud_cycle(bucket_name: str) -> Dict[str, Any]:
    """Execute one complete diligence and plan mutation cycle against GCS."""
    storage = GCSStorageAdapter(bucket_name)
    client = get_genai_client()
    model_name = os.environ.get("GEMINI_MODEL", "gemini-3.8-flash")

    frontier_data = storage.read_json("state/frontier.json")
    if not frontier_data:
        raise ValueError(f"frontier.json not found in GCS bucket {bucket_name} at state/frontier.json")

    cycle_num = frontier_data.get("active_cycle", 0) + 1
    frontier_data["active_cycle"] = cycle_num

    # 1. Process inbox
    inbox_notes = process_steering_inbox(storage)

    # 2. Select frontier task (or spawn stress test if all resolved)
    open_items = [item for item in frontier_data.get("frontier", []) if item.get("status") in ["OPEN", "IN_PROGRESS"]]
    if not open_items:
        stress_item = spawn_cloud_stress_test(client, model_name, frontier_data, storage)
        if stress_item:
            open_items = [stress_item]
        else:
            return {
                "status": "IDLE",
                "cycle": cycle_num,
                "message": "All frontier items resolved and stress tests converged."
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

    capital_baseline = storage.read_text("plan/00_assumed_capital_baseline.md")
    if capital_baseline:
        evidence_context.append(f"--- FIXED OPERATING BASELINE: 00_assumed_capital_baseline.md ---\n" + capital_baseline)

    graveyard_content = storage.read_text("plan/graveyard_rejected_ideas.md")
    if graveyard_content:
        evidence_context.append(f"--- REJECTED STRATEGIES & AUTOPSIES ---\n" + graveyard_content)

    target_plan_path = target["target_plan_file"]
    existing_plan_content = storage.read_text(target_plan_path)

    # 4. Draft refinement with Gemini 3.8 Flash & Google Search Grounding
    prompt_draft = f"""
You are the Turnaround Operator, Chief Product Officer, and Growth Architect for Jack Fay, who is acquiring and taking over Lily Corporation (Aurora, IL), a 44-year-old manufacturer of heavy-duty chemical injection equipment and custom molded accessories.

CONTEXT:
The acquisition capital structure is FIXED and ASSUMED (see 00_assumed_capital_baseline.md). Do NOT spend time debating pre-deal senior debt sizing or financing structures. 

YOUR MISSION:
Focus 100% on TAKING OVER, OPERATING, AND TRANSFORMING LILY CORP into a high-margin, scalable manufacturing and distribution powerhouse.
Research markets, invent/validate new product lines, build operational automations, establish commercial distribution channels (e.g. Sika, Euclid, White Cap, IDOT), and author Jack Fay's concrete operator playbook.

YOUR IMMEDIATE TASK:
Draft or update the plan module: `{target_plan_path}` to solve this specific frontier item:
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
5. Output the COMPLETE markdown content for `{target_plan_path}`.
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

    # 5. Adversarial Red-Team Committee Review & Frontier Expansion
    prompt_critique = f"""
You are the Executive Operating & Product Committee for Lily Corporation, consisting of:
1. Shop Floor & Manufacturing Feasibility (Dave Kling & Bob Trout): Can our 4-person shop in Aurora fabricate/assemble this with our existing CNC, welding, and 10 injection molds without a massive capex spend? Does it cause shop floor chaos?
2. Contractor & Customer Adoption Realist (Dave Jepsen): Will civil bridge and concrete contractors actually buy and spec this? Does it fit how general contractors procure equipment and consumables?
3. Unit Economics & Margin Specialist: Does this protect Lily's ~65-70% gross margins on accessories and drive real incremental EBITDA?
4. Competitive Moat vs Graco & ChemCo: Is this truly differentiated, or are we walking into a commodity trap?

Review the proposed draft for `{target_plan_path}`:

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
    except Exception:
        critique_result = {"approved": True, "confidence_score": 6, "summary_verdict": "Auto-accepted with warning", "spawned_frontier_items": []}

    # 6. Dynamically Expand Frontier in GCS
    spawned = critique_result.get("spawned_frontier_items", [])
    existing_questions = {item.get("question", "").strip().lower() for item in frontier_data.get("frontier", [])}
    existing_titles = {item.get("title", "").strip().lower() for item in frontier_data.get("frontier", [])}
    
    new_spawns_count = 0
    for s in spawned:
        q_text = s.get("question", "").strip()
        t_text = s.get("title", "").strip()
        if not q_text or q_text.lower() in existing_questions or t_text.lower() in existing_titles:
            continue
        
        cat_prefix = s.get("category", "DEAL")[:4].upper().replace(" ", "_")
        spawn_id = f"{cat_prefix}_{len(frontier_data.get('frontier', [])) + 1:02d}"
        
        new_frontier_item = {
            "id": spawn_id,
            "category": s.get("category", "Diligence & Operations"),
            "title": t_text,
            "question": q_text,
            "known_facts": [f"Uncovered during Cycle #{cycle_num} cloud investigation of [{target['id']}]."],
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

    # 7. Apply verdict to GCS
    if critique_result.get("approved"):
        # Save plan module to GCS
        storage.write_text(target_plan_path, draft_content, content_type="text/markdown")

        # Update target frontier status
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
            f"- **Total Backlog Items:** {len(frontier_data['frontier'])} ({new_spawns_count} newly spawned)\n"
            f"- **Committee Verdict:** {critique_result.get('summary_verdict')}\n\n"
            f"## Product & Operating Committee Perspectives\n"
            f"* **Shop Floor Feasibility (Dave K/Bob):** {critique_result.get('shop_floor_critique', 'N/A')}\n"
            f"* **Contractor Adoption (Dave J):** {critique_result.get('contractor_adoption_critique', 'N/A')}\n"
            f"* **Unit Economics & Margin:** {critique_result.get('unit_economics_critique', 'N/A')}\n"
            f"* **Competitive Moat:** {critique_result.get('competitive_moat_critique', 'N/A')}\n"
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
