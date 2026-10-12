#!/usr/bin/env python3
"""
Lily Corp Business Plan Cockpit & AI Page Generator Server.
Provides real-time monitoring of recursive diligence cycles and generates on-the-fly
executive review HTML pages using Google Gemini.
"""

import os
import sys
import json
import time
import uuid
import re
import secrets
import base64
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict, Any, List

from fastapi import FastAPI, HTTPException, Request, Response, BackgroundTasks
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from google import genai
from google.genai import types

# Base paths
BASE_DIR = Path(__file__).resolve().parent.parent
PORTAL_DIR = Path(__file__).resolve().parent
STATIC_DIR = PORTAL_DIR / "static"
GENERATED_DIR = PORTAL_DIR / "generated"
PLAN_DIR = BASE_DIR / "plan"
STATE_DIR = BASE_DIR / "state"
STEERING_DIR = BASE_DIR / "steering"
EVIDENCE_DIR = BASE_DIR / "evidence"

# Ensure directories exist
STATIC_DIR.mkdir(parents=True, exist_ok=True)
GENERATED_DIR.mkdir(parents=True, exist_ok=True)

# Load environment
def load_env():
    env_file = BASE_DIR / ".env"
    if env_file.exists():
        with open(env_file, "r") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    os.environ[k.strip()] = v.strip()

load_env()

# Initialize Google Cloud Storage if configured
GCS_BUCKET = os.environ.get("GCS_BUCKET_NAME")
gcs_adapter = None
if GCS_BUCKET:
    try:
        from google.cloud import storage
        class GCSStore:
            def __init__(self, bname):
                self.client = storage.Client()
                self.bucket = self.client.bucket(bname)
            def read_text(self, path: str) -> str:
                blob = self.bucket.blob(path.lstrip("/"))
                return blob.download_as_text() if blob.exists() else ""
            def write_text(self, path: str, content: str, content_type: str = "text/plain"):
                blob = self.bucket.blob(path.lstrip("/"))
                blob.upload_from_string(content, content_type=content_type)
            def read_json(self, path: str) -> dict:
                txt = self.read_text(path)
                return json.loads(txt) if txt else {}
            def write_json(self, path: str, data: Any):
                self.write_text(path, json.dumps(data, indent=2), content_type="application/json")
            def list_blobs(self, prefix: str):
                return [b.name for b in self.client.list_blobs(self.bucket, prefix=prefix.lstrip("/"))]
        gcs_adapter = GCSStore(GCS_BUCKET)
        print(f"[STORAGE] Connected to Google Cloud Storage: gs://{GCS_BUCKET}", flush=True)
    except Exception as e:
        print(f"[STORAGE] GCS initialization failed ({e}), falling back to local files.", flush=True)

def get_genai_client() -> genai.Client:
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key:
        return genai.Client(api_key=api_key)
    project = os.environ.get("GCP_PROJECT", "dulcet-voyager-496719-e3")
    location = os.environ.get("GCP_LOCATION", "us-central1")
    return genai.Client(vertexai=True, project=project, location=location)

app = FastAPI(title="Lily Corp Diligence Cockpit", version="2.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# HTTP Basic Authentication Middleware
@app.middleware("http")
async def basic_auth_middleware(request: Request, call_next):
    # Health checks exempt from auth
    if request.url.path in ("/health", "/api/health"):
        return await call_next(request)

    # Allow disabling auth explicitly via env
    if os.environ.get("PORTAL_DISABLE_AUTH", "false").lower() == "true":
        return await call_next(request)

    expected_username = os.environ.get("PORTAL_USERNAME", "jack")
    expected_password = os.environ.get("PORTAL_PASSWORD", "lilycorp2026")

    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Basic "):
        return Response(
            content="Authentication required. Please enter your Lily Corp Cockpit credentials.\n",
            status_code=401,
            headers={"WWW-Authenticate": 'Basic realm="Lily Corp Diligence Cockpit"'}
        )

    try:
        encoded_creds = auth_header.split(" ", 1)[1]
        decoded_creds = base64.b64decode(encoded_creds).decode("utf-8")
        username, password = decoded_creds.split(":", 1)
    except Exception:
        return Response(
            content="Invalid Authorization header.\n",
            status_code=401,
            headers={"WWW-Authenticate": 'Basic realm="Lily Corp Diligence Cockpit"'}
        )

    correct_username = secrets.compare_digest(username.encode("utf-8"), expected_username.encode("utf-8"))
    correct_password = secrets.compare_digest(password.encode("utf-8"), expected_password.encode("utf-8"))

    if not (correct_username and correct_password):
        return Response(
            content="Incorrect username or password.\n",
            status_code=401,
            headers={"WWW-Authenticate": 'Basic realm="Lily Corp Diligence Cockpit"'}
        )

    return await call_next(request)

# Storage helpers (supporting both GCS and local filesystem)
def normalize_rel_path(path: Any) -> str:
    s = str(path)
    if s.startswith(str(BASE_DIR)):
        return os.path.relpath(s, str(BASE_DIR))
    return s.lstrip("/")

def read_text(path: Any) -> str:
    rel_path = normalize_rel_path(path)
    if gcs_adapter:
        txt = gcs_adapter.read_text(rel_path)
        if txt:
            return txt
    p = BASE_DIR / rel_path if not isinstance(path, Path) else path
    if p.exists():
        with open(p, "r", encoding="utf-8") as f:
            return f.read()
    return ""

def write_text(path: Any, content: str, content_type: str = "text/plain"):
    rel_path = normalize_rel_path(path)
    if gcs_adapter:
        try:
            gcs_adapter.write_text(rel_path, content, content_type=content_type)
        except Exception as e:
            print(f"[STORAGE] GCS write error for {rel_path}: {e}")
    try:
        p = BASE_DIR / rel_path if not isinstance(path, Path) else path
        p.parent.mkdir(parents=True, exist_ok=True)
        with open(p, "w", encoding="utf-8") as f:
            f.write(content)
    except Exception:
        pass

def read_json(path: Any) -> dict:
    rel_path = normalize_rel_path(path)
    if gcs_adapter:
        data = gcs_adapter.read_json(rel_path)
        if data:
            return data
    p = BASE_DIR / rel_path if not isinstance(path, Path) else path
    if p.exists():
        with open(p, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def write_json(path: Any, data: Any):
    rel_path = normalize_rel_path(path)
    if gcs_adapter:
        try:
            gcs_adapter.write_json(rel_path, data)
        except Exception as e:
            print(f"[STORAGE] GCS write_json error for {rel_path}: {e}")
    try:
        p = BASE_DIR / rel_path if not isinstance(path, Path) else path
        p.parent.mkdir(parents=True, exist_ok=True)
        with open(p, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    except Exception:
        pass

def get_generated_registry() -> List[Dict[str, Any]]:
    res = read_json("portal/generated/registry.json")
    if isinstance(res, list):
        return res
    return []

def save_generated_registry(items: List[Dict[str, Any]]):
    write_json("portal/generated/registry.json", items)


# Models
class SteeringInput(BaseModel):
    note: str
    run_cycle_now: bool = False

class PageGenerateRequest(BaseModel):
    title: Optional[str] = None
    template_type: str = "briefing"  # briefing | red_team | operator_checklist | custom
    item_id: Optional[str] = None
    plan_file: Optional[str] = None
    custom_prompt: Optional[str] = None

class AdvisorQuestionRequest(BaseModel):
    question: str
    topic: Optional[str] = "general"


# API Routes
@app.get("/api/status")
def get_system_status():
    frontier = read_json(STATE_DIR / "frontier.json")
    items = frontier.get("frontier", [])
    active_cycle = frontier.get("active_cycle", 0)

    status_counts = {"OPEN": 0, "RESOLVED": 0, "REFINED": 0, "EXPLORATORY": 0, "PARKED_YEAR_3": 0}
    priority_counts = {"CRITICAL": 0, "HIGH": 0, "MEDIUM": 0, "LOW": 0}
    scores = []

    for item in items:
        st = item.get("status", "OPEN")
        pr = item.get("priority", "MEDIUM")
        sc = item.get("confidence_score")
        if st in status_counts:
            status_counts[st] += 1
        else:
            status_counts["OPEN"] += 1

        if pr in priority_counts:
            priority_counts[pr] += 1

        if sc is not None:
            try:
                scores.append(float(sc))
            except (ValueError, TypeError):
                pass

    avg_score = round(sum(scores) / len(scores), 2) if scores else 0.0

    digest_content = read_text(STEERING_DIR / "digest.md")
    rejections_content = read_text(STATE_DIR / "rejections.log")
    rejection_count = len([l for l in rejections_content.splitlines() if "REJECTED for" in l or "AUDIT REJECTED" in l])
    graveyard_content = read_text(PLAN_DIR / "graveyard_rejected_ideas.md")
    graveyard_count = len(re.findall(r"### Concept:", graveyard_content))

    github_prs_merged = len([i for i in items if i.get("github_auto_merged") is True])
    github_prs_pending = len([i for i in items if i.get("github_pr") and not i.get("github_auto_merged")])

    return {
        "active_cycle": active_cycle,
        "total_frontier_items": len(items),
        "status_counts": status_counts,
        "priority_counts": priority_counts,
        "avg_confidence_score": avg_score,
        "rejection_count": rejection_count,
        "graveyard_count": graveyard_count,
        "github_prs_merged": github_prs_merged,
        "github_prs_pending": github_prs_pending,
        "digest_snippet": digest_content[:500] if digest_content else "No digest available yet.",
        "last_updated": datetime.now().isoformat()
    }


@app.get("/api/frontier")
def get_frontier_items(
    status: Optional[str] = None,
    priority: Optional[str] = None,
    search: Optional[str] = None
):
    frontier = read_json(STATE_DIR / "frontier.json")
    items = frontier.get("frontier", [])

    filtered = []
    for item in items:
        if status and item.get("status", "").upper() != status.upper():
            continue
        if priority and item.get("priority", "").upper() != priority.upper():
            continue
        if search:
            s = search.lower()
            text_corpus = f"{item.get('id', '')} {item.get('title', '')} {item.get('question', '')} {item.get('category', '')}".lower()
            if s not in text_corpus:
                continue
        filtered.append(item)

    return {"count": len(filtered), "items": filtered}


@app.get("/api/frontier/{item_id}")
def get_frontier_item(item_id: str):
    frontier = read_json(STATE_DIR / "frontier.json")
    for item in frontier.get("frontier", []):
        if item.get("id") == item_id:
            # Also attach relevant plan excerpt if available
            target_plan = item.get("target_plan_file")
            plan_text = ""
            if target_plan:
                p_path = BASE_DIR / target_plan
                if p_path.exists():
                    plan_text = read_text(p_path)
            return {"item": item, "target_plan_text": plan_text[:8000]}
    raise HTTPException(status_code=404, detail="Item not found")


@app.get("/health")
def health_check():
    return {"status": "ok", "service": "lilycorp-cockpit", "time": datetime.now().isoformat()}


@app.get("/api/plans")
def list_plans():
    plans = []
    if gcs_adapter:
        blob_names = gcs_adapter.list_blobs("plan/")
        for name in sorted(blob_names):
            if name.endswith(".md"):
                filename = name.split("/")[-1]
                content = read_text(name)
                plans.append({
                    "filename": filename,
                    "relative_path": name,
                    "size_bytes": len(content),
                    "lines": len(content.splitlines()),
                    "is_graveyard": filename == "graveyard_rejected_ideas.md"
                })
    if not plans and PLAN_DIR.exists():
        for f in sorted(PLAN_DIR.glob("*.md")):
            size = f.stat().st_size
            lines = len(read_text(f).splitlines())
            plans.append({
                "filename": f.name,
                "relative_path": f"plan/{f.name}",
                "size_bytes": size,
                "lines": lines,
                "is_graveyard": f.name == "graveyard_rejected_ideas.md"
            })
    return {"plans": plans}


@app.get("/api/plans/{filename}")
def get_plan_content(filename: str):
    rel_path = f"plan/{filename}"
    content = read_text(rel_path)
    if not content:
        raise HTTPException(status_code=404, detail="Plan file not found")
    return {
        "filename": filename,
        "content": content,
        "line_count": len(content.splitlines()),
        "last_modified": datetime.now().isoformat()
    }


@app.get("/api/graveyard")
def get_graveyard():
    content = read_text("plan/graveyard_rejected_ideas.md")
    # Parse concepts
    concepts = []
    chunks = content.split("### Concept: ")
    for chunk in chunks[1:]:
        lines = chunk.strip().splitlines()
        title = lines[0].strip() if lines else "Unknown"
        body = "\n".join(lines[1:])
        classification = "REJECTED"
        if "* **Classification:**" in body:
            m = re.search(r"\* \*\*Classification:\*\* `([^`]+)`", body)
            if m:
                classification = m.group(1)
        concepts.append({
            "title": title,
            "classification": classification,
            "raw_text": chunk.strip()
        })
    return {"count": len(concepts), "concepts": concepts, "raw_content": content}


@app.get("/api/steering")
def get_steering_info():
    inbox = read_text("steering/inbox.md")
    archive = read_text("steering/archive.md")
    digest = read_text("steering/digest.md")
    return {
        "inbox": inbox,
        "archive_recent": archive[-5000:] if archive else "",
        "digest": digest
    }


@app.post("/api/steering")
def submit_steering(data: SteeringInput, background_tasks: BackgroundTasks):
    note = data.note.strip()
    if not note:
        raise HTTPException(status_code=400, detail="Note cannot be empty")

    current_inbox = read_text("steering/inbox.md")
    entry = f"\n- [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {note}\n"
    write_text("steering/inbox.md", current_inbox + entry)

    if data.run_cycle_now:
        # Trigger cycle runner in background
        background_tasks.add_task(run_local_cycle)

    return {"status": "SUCCESS", "message": "Steering note added to inbox", "triggered_cycle": data.run_cycle_now}


def run_local_cycle():
    """Run single cycle in background using venv python or direct cloud call."""
    try:
        if GCS_BUCKET:
            from cloud_function.diligence_core import run_single_cloud_cycle
            run_single_cloud_cycle(GCS_BUCKET)
            return
        import subprocess
        python_bin = BASE_DIR / "engine" / ".venv" / "bin" / "python"
        runner_script = BASE_DIR / "engine" / "cycle_runner.py"
        subprocess.run([str(python_bin), str(runner_script), "--once"], cwd=BASE_DIR, check=True)
    except Exception as e:
        print(f"Background cycle execution failed: {e}", flush=True)


@app.post("/api/run-cycle")
def trigger_cycle(background_tasks: BackgroundTasks):
    background_tasks.add_task(run_local_cycle)
    return {"status": "TRIGGERED", "message": "Cycle execution launched in background."}


@app.get("/api/generated-pages")
def list_generated_pages():
    return {"pages": get_generated_registry()}


@app.get("/view/{page_id}", response_class=HTMLResponse)
def view_generated_page(page_id: str):
    html = read_text(f"portal/generated/{page_id}.html")
    if not html:
        raise HTTPException(status_code=404, detail="Generated page not found")
    return HTMLResponse(content=html)


@app.post("/api/ask-advisor")
def ask_operator_advisor(req: AdvisorQuestionRequest):
    """
    Dedicated AI Operator Advisor for Jack Fay.
    Provides plain-English, deeply empathetic, highly grounded executive guidance.
    """
    client = get_genai_client()
    model_name = os.environ.get("GEMINI_MODEL", "gemini-3.8-flash")

    # Load real operator context
    guide_text = read_text("plan/05_jack_fay_operator_guide.md")
    baseline_text = read_text("plan/00_assumed_capital_baseline.md")
    site_visit = read_text("evidence/diligence/lilycorp_site_visit_notes_2026-09-09.md")
    graveyard = read_text("plan/graveyard_rejected_ideas.md")

    prompt = f"""You are Jack Fay's trusted Senior Operating Advisor, Mentor, and Executive Coach.
Jack Fay is acquiring Lily Corporation (Aurora, IL), a 44-year-old manufacturer of heavy-duty chemical injection equipment and custom molded accessories.
Jack lives in Riverside, IL and is stepping into an industrial manufacturing business in an industry he has never worked in.

YOUR PERSONA & TONE:
- Calm, deeply empathetic, highly encouraging, yet ruthlessly practical and grounded.
- Speak in clear, plain English. Avoid consulting jargon, MBA buzzwords, and vague platitudes.
- Give concrete, step-by-step guidance. Jack is feeling overwhelmed and needs digestible, actionable clarity.

THE CORE REALITY OF LILY CORP:
- Founder: Bob Trout (retiring founder, 70+; 44 years of unwritten formulas and pricing math).
- 5-Person Shop Roster:
  * Dave Jepsen: VP Sales/Tech Support (~2 yrs). Contractor whisperer. Answers technical calls, specifies injection port spacing and pumps. Needs a $15k stay bonus + gross margin pool.
  * Dave Kling: Lead Fabricator, Machinist, Welder, Purchasing Agent. Craftsman pride. Hates corporate talk. Needs respect, $3,500 Day-1 tooling budget, and $2,500 PO autonomy.
  * Greg: Sole operator of Cincinnati Milacron injection molding press and 2,200 PSI hydrostatic test bench. Terrified of being replaced. Needs $5,000 stay bonus + $250/mo uptime bonus + Master Trainer bonus to cross-train Julian.
  * Julian Perez: Assembly, teardown repairs, cleaning, crating/shipping. Reliable workhorse.
  * Maggie M: Office Manager & Bookkeeper. QuickBooks Desktop, paper checks, billing. Zero software changes in Year 1!
- What Lily Sells:
  * The Machines (Razors): CD-250 ($18k-$25k) and CD-15 proportioner pumps. Air-powered/pneumatic, simple, repairable with a wrench. Beats Graco in confined spaces and bridges.
  * The Consumables (Blades): Plastic injection ports (LPP, socket ports), caps, static mixers molded on-site by Greg. 65-75% Gross Margin! This pays the bills.
- Financial & Capital Guardrails:
  * Acquisition price: $1,250,000.
  * Debt service + lease floor: $11,403.04/month ($136.8k/year).
  * Liquid working capital floor: $50,000 minimum cash balance. Never let it drop below this!
  * Year 1 Discretionary Capex: Maximum $20,000 total. NO new CNC machines or speculative molds.

OPERATOR PLAYBOOK CONTEXT:
--- 05_jack_fay_operator_guide.md ---
{guide_text[:14000]}

--- 00_assumed_capital_baseline.md ---
{baseline_text[:6000]}

--- SITE VISIT REALITY ---
{site_visit[:6000]}

--- THE GRAVEYARD (BURIED BAD IDEAS) ---
{graveyard[:4000]}

USER QUESTION:
"{req.question}"

INSTRUCTIONS FOR ANSWER:
1. Provide a direct, reassuring 1-2 sentence executive summary answering the question immediately.
2. Provide 3-4 concrete, numbered steps or key points grounded in Lily Corp's actual people, machines, or financials.
3. Highlight an explicit "⚠️ What NOT to do" warning to keep Jack out of trouble.
4. Conclude with a clear "🎯 Recommended Action for Today".
Keep the formatting clean, concise, and easy to read with clear markdown headers.
"""

    try:
        response = client.models.generate_content(
            model=model_name,
            contents=prompt
        )
        answer_text = response.text.strip()
        return {"status": "SUCCESS", "answer": answer_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI Advisor error: {e}")


@app.post("/api/generate-page")
def generate_ai_html_page(req: PageGenerateRequest):
    """
    Core AI On-The-Fly Page Generator.
    Synthesizes rich, interactive, standalone HTML pages grounded in real company facts.
    """
    client = get_genai_client()
    model_name = os.environ.get("GEMINI_MODEL", "gemini-3.8-flash")

    # 1. Gather context
    evidence_snippets = []
    
    # Financials
    pl_csv = read_text("evidence/financials/pl.csv")
    if pl_csv:
        evidence_snippets.append("--- P&L 2015-2025 ---\n" + "\n".join(pl_csv.splitlines()[:40]))
        
    # Site Notes
    site_notes = read_text("evidence/diligence/lilycorp_site_visit_notes_2026-09-09.md")
    if site_notes:
        evidence_snippets.append("--- SITE VISIT NOTES ---\n" + site_notes[:4000])

    # Target item or plan
    target_context = ""
    frontier_item = None
    if req.item_id:
        frontier = read_json("state/frontier.json")
        for item in frontier.get("frontier", []):
            if item.get("id") == req.item_id:
                frontier_item = item
                target_context += f"TARGET FRONTIER ITEM:\nID: {item.get('id')}\nTitle: {item.get('title')}\nQuestion: {item.get('question')}\nStatus: {item.get('status')}\nConfidence: {item.get('confidence_score')}\nKnown Facts: {item.get('known_facts')}\n\n"
                break

    if req.plan_file:
        plan_txt = read_text(req.plan_file)
        if plan_txt:
            target_context += f"PLAN MODULE ({req.plan_file}):\n" + plan_txt[:12000]
    elif frontier_item and frontier_item.get("target_plan_file"):
        plan_txt = read_text(frontier_item.get("target_plan_file"))
        if plan_txt:
            target_context += f"TARGET PLAN MODULE:\n" + plan_txt[:12000]

    graveyard_text = read_text("plan/graveyard_rejected_ideas.md")

    # 2. Template instructions
    template_instructions = {
        "briefing": """
GENERATE A HIGH-IMPACT EXECUTIVE BRIEFING & VISUAL SCORECARD:
- Top hero with badge, confidence indicator, and clear strategic bottom line.
- Key Financials / KPI Cards (Revenue impact, gross margin %, capex required, risk level).
- Empirical Truth vs Assumption Table: What is proven in diligence vs what is an exploratory hypothesis.
- Shop Floor Reality Check: Exact labor hours impact on Dave Kling, Julian Perez, and Greg.
- Actionable Decision Matrix for Jack Fay.
""",
        "red_team": """
GENERATE A BRUTALLY HONEST ADVERSARIAL RED-TEAM STRESS TEST:
- Executive Alert / Risk Level Banner (Critical / High / Moderate).
- "Assumption Autopsy": List every hidden or unproven assumption in this strategy.
- Regulatory & Legal Reality Check: How federal BABA, EPA AIS, or FHWA public bidding rules actually apply.
- Margin Trap & Wholesale Price Resistance: Landed import pricing vs Lily domestic cost analysis.
- Operational Failure Modes: What breaks on the shop floor or in customer support?
- Recommendation: Kill, Pivot, or De-Risk into Year 2.
""",
        "operator_checklist": """
GENERATE JACK FAY'S ACTIONABLE OPERATOR TRANSITION DASHBOARD:
- 14-Day Sprint & 60-Day Runway Milestones.
- Exact questions Jack must ask Bob Trout before retirement.
- Specific technical handshakes with Dave Jepsen and Dave Kling.
- Interactive checkboxes / step-by-step verification protocols.
- QuickBooks Desktop SKU and margin tracking reminders.
""",
        "custom": f"""
USER CUSTOM REQUEST:
{req.custom_prompt}
"""
    }

    selected_instruction = template_instructions.get(req.template_type, template_instructions["custom"])

    prompt = f"""
You are the Executive Product & Diligence Architect for Jack Fay, who is acquiring Lily Corporation in Aurora, IL.

TASK:
Generate a complete, self-contained, beautifully styled, interactive standalone HTML page that allows Jack to monitor, review, and evaluate this aspect of the business plan.

DESIGN & STYLING REQUIREMENTS (MANDATORY):
1. Complete Single-File HTML with embedded CSS and modern Vanilla Javascript.
2. Aesthetic: High-end, premium dark-mode glassmorphic interface.
   - Fonts: Google Fonts 'Outfit' and 'Plus Jakarta Sans'.
   - Color Palette: Deep rich dark background (#090c15, #0f172a), subtle glowing radial gradients, frosted glass cards (rgba(255, 255, 255, 0.04), backdrop-filter blur), vibrant accents (Electric Orange #ff6b35, Cyan #00e5ff, Emerald #10b981, Amber #f59e0b, Rose #f43f5e).
   - Micro-animations: Hover glows, smooth transitions, pill badges.
3. Interactive Elements:
   - Tab switchers or collapsible sections if appropriate.
   - Print / Save button (`window.print()`).
   - Back to Cockpit navigation link.
   - Interactive KPI gauges or visual meters.
4. CONTENT FIDELITY (CRITICAL):
   - Grounded in Lily Corporation's actual facts (5-person shop: Dave Kling, Julian Perez, Greg, Maggie M, Dave Jepsen; 10 proprietary molds in Aurora; Cincinnati Milacron press; $50k capital baseline).
   - Distinguish strictly between [VERIFIED DILIGENCE] and [EXPLORATORY HYPOTHESIS].
   - Output ONLY the raw HTML code starting with <!DOCTYPE html> and ending with </html>. Do not wrap in markdown quotes if possible, or keep it clean.

SPECIFIC PAGE MANDATE:
{selected_instruction}

CONTEXT & EVIDENCE:
{target_context}

EVIDENCE SNIPPETS:
{chr(10).join(evidence_snippets)}

REJECTED CONCEPTS & AUTOPSIES:
{graveyard_text[:3000]}
"""

    t0 = time.time()
    print(f"[AI GENERATE] Generating {req.template_type} page for item={req.item_id}, plan={req.plan_file} using {model_name}...", flush=True)

    response = client.models.generate_content(
        model=model_name,
        contents=prompt
    )

    html_content = response.text.strip()
    if html_content.startswith("```html"):
        html_content = html_content[7:]
    if html_content.startswith("```"):
        html_content = html_content[3:]
    if html_content.endswith("```"):
        html_content = html_content[:-3]
    html_content = html_content.strip()

    # Save page to disk & GCS
    page_id = f"page_{int(time.time())}_{uuid.uuid4().hex[:6]}"
    write_text(f"portal/generated/{page_id}.html", html_content, content_type="text/html")

    # Derive human title
    page_title = req.title
    if not page_title:
        title_match = re.search(r"<title>(.*?)</title>", html_content, re.IGNORECASE)
        if title_match:
            page_title = title_match.group(1).replace("Lily Corp — ", "").replace("Lily Corp - ", "").strip()
        else:
            page_title = f"{req.template_type.title()} Report - {req.item_id or 'General'}"

    # Update registry
    registry = get_generated_registry()
    entry = {
        "page_id": page_id,
        "title": page_title,
        "template_type": req.template_type,
        "item_id": req.item_id,
        "plan_file": req.plan_file,
        "created_at": datetime.now().isoformat(),
        "url": f"/view/{page_id}",
        "file_size": len(html_content)
    }
    registry.insert(0, entry)
    save_generated_registry(registry)

    elapsed = time.time() - t0
    print(f"[AI GENERATE] Done in {elapsed:.2f}s! Saved {page_id} ({len(html_content)} bytes): {page_title}", flush=True)

    return {
        "status": "SUCCESS",
        "page_id": page_id,
        "title": page_title,
        "url": f"/view/{page_id}",
        "html_preview": html_content[:2000]
    }


# Mount static assets
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

@app.get("/", response_class=HTMLResponse)
def serve_index():
    index_file = STATIC_DIR / "index.html"
    if not index_file.exists():
        return HTMLResponse("<h1>Loading Cockpit...</h1>")
    return HTMLResponse(read_text(index_file))


def main():
    import uvicorn
    port = int(os.environ.get("PORT", 8080))
    print(f"===========================================================")
    print(f" Lily Corp Cockpit & AI Page Generator Running on port {port}")
    print(f" URL: http://localhost:{port}")
    print(f"===========================================================")
    uvicorn.run(app, host="0.0.0.0", port=port)

if __name__ == "__main__":
    main()
