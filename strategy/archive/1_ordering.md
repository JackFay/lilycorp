# Project 1: Dual-Channel Smart Ordering (Portal + AI Email Desk)

**Objective:** Modernize Lily Corp’s parts and consumables ordering by deploying a **Dual-Channel Smart Ordering System**: (1) a mobile-friendly 24/7 B2B reorder portal, and (2) an AI-powered email order desk that automatically parses unstructured customer emails and PDF Purchase Orders.  
**Timeline:** Weeks 1–6 post-acquisition (Days 1–45)  
**Target Revenue Impact:** +$10,000 to $25,000/month in high-margin (60%–75%) incremental sales  
**Operational Impact:** Eliminates 80%–90% of manual order entry and phone quoting (~20 hours/week saved for Maggie and Dave J)  

---

## 1. Why Dual-Channel? (Meeting Contractors Where They Are)

In industrial manufacturing and civil contracting, forcing customers into a single digital channel often fails:
* **The Web Portal (`orders.lilycorp.com`)** is perfect for younger foremen, new accounts without established credit, and anyone scanning an equipment **QR code** on a jobsite at 6:30 AM to reorder nozzles in 30 seconds.
* **The AI Email Desk (`orders@lilycorp.com`)** is essential for the 60%–70% of legacy contractors who **hate creating accounts or remembering passwords**. They simply send an email from their truck (*"Hey Dave, send 2 boxes of mixers and 100 ports to the bridge jobsite, PO #4891"*) or have their back office attach a PDF Purchase Order.

By launching both simultaneously, you capture 100% of demand with **zero customer friction**.

---

## 2. Channel Architecture & Workflows

### Channel A: The Mobile B2B Reorder Portal (`orders.lilycorp.com`)
* **Core Function:** A fast, lightweight catalog of the top 50–100 high-margin consumables and wear parts.
* **Jobsite Distribution (The QR Code Hack):** Weather-resistant vinyl stickers applied to every machine leaving the shop, rental units, and parts boxes:
  > *"Need replacement nozzles, ports, or pump parts? Scan here to reorder in 30 seconds."*
* **Payment Rails:** Stored credit card on file (Stripe Billing) or 1-click checkout against pre-approved Net-30 customer credit terms.

### Channel B: The AI Email Order Desk (`orders@lilycorp.com`)
* **Core Function:** An autonomous ingestion agent (powered by an LLM + PDF document parser) monitoring incoming customer order emails.
* **Capabilities:**
  1. **Fuzzy Customer Matching:** Matches the sender's email domain or company name against Lily Corp’s QuickBooks customer master.
  2. **Intelligent SKU & Quantity Parsing:** Extracts line items, quantities, and descriptions from conversational email text or attached PDF Purchase Orders.
  3. **Pricing & Credit Verification:** Applies the customer's negotiated discount tier and checks Net-30 credit status.
  4. **Draft Staging in QuickBooks:** Creates a **DRAFT Sales Order / Invoice** automatically in QuickBooks.
  5. **Human-in-the-Loop Approval:** Prepares a pre-formatted order confirmation email draft for Maggie M to review.

```
                    ┌─────────────────────────────────────────────────────────┐
                    │               INCOMING ORDER CHANNELS                   │
                    └────────────────────────────┬────────────────────────────┘
                                                 │
                   ┌─────────────────────────────┴────────────────────────────┐
                   ▼                                                          ▼
        [Channel A: Web Portal]                                   [Channel B: AI Email Desk]
    Contractor scans QR code at 6:30 AM                       Contractor emails orders@lilycorp.com
    Picks top SKUs & checks out via Net-30                    Sends short text note or attaches PDF PO
                   │                                                          │
                   │                                                          ▼
                   │                                                 [AI Ingestion Agent]
                   │                                           • Fuzzy matches customer & SKUs
                   │                                           • Applies customer discount tier
                   │                                           • Stages DRAFT Order in QuickBooks
                   │                                           • Prepares DRAFT confirmation email
                   │                                                          │
                   └─────────────────────────────┬────────────────────────────┘
                                                 │
                                                 ▼
                                     [Maggie's Review Dashboard]
                                 Maggie clicks [Approve] (5 seconds)
                                                 │
                         ┌───────────────────────┴───────────────────────┐
                         ▼                                               ▼
          Customer receives instant confirmation           Warehouse packing slip auto-prints
          with tracking info / invoice                     at Dave K / Julian's packing station
```

---

## 3. The Human-in-the-Loop Safeguard (Staff Buy-In)

To protect customer relationships and ensure operational accuracy, the AI email agent operates with a **Human-in-the-Loop** model:

1. **No "Blind" Automated Sending (Months 1–3):** The AI does not email customers or finalize invoices autonomously without human sign-off.
2. **The "1-Click" Experience for Maggie:**  
   When Maggie opens her desk at 8:00 AM, she doesn't see 15 emails requiring manual data entry. She sees structured drafts:
   > *"Midwest Concrete sent PO #4921 for 200 Surface Ports and 2 Boxes of 1/2\" Mixers ($1,450). QuickBooks Draft #10482 ready."*  
   > `[Review & Approve]` / `[Edit]`
3. **Internal Morale Boost:** Maggie is transformed from an overworked data-entry clerk into a supervisory manager supported by an AI assistant.

---

## 4. 45-Day Implementation Roadmap

```
[Weeks 1–2] Master Data & Triage ──► [Weeks 3–4] Portal & AI Engine Build ──► [Weeks 5–6] Launch & Rollout
```

### Weeks 1–2: Master Data Audit & SKU Triage
* Export 24 months of invoice history from QuickBooks.
* Normalize the top 50 recurring consumables and replacement parts (SKU, title, unit cost, contractor tier pricing, weight).
* Build the customer reference database (company names, aliases, buyer email domains, billing/shipping addresses, payment terms).

### Weeks 3–4: Build Portal & Deploy AI Ingestion
* **Channel A (Portal):** Deploy lightweight Next.js B2B portal with Stripe and Net-30 account support.
* **Channel B (AI Inbox):** Connect an LLM-based worker to `orders@lilycorp.com` using the Google Workspace / Gmail API and QuickBooks Online/Desktop SDK.
* Configure PDF PO extraction (line items, part numbers, PO numbers, delivery dates).
* Test parser against 100 historical customer emails and POs to ensure >95% extraction accuracy.

### Weeks 5–6: Equipment QR Codes & Field Rollout
* Print heavy-duty, oil/weather-resistant vinyl QR code stickers for all outgoing shop equipment and rental units.
* Train Maggie and Dave J on the draft review interface.
* Send an announcement email blast to Lily Corp’s entire customer base:
  > *"Order your parts 24/7 online at orders.lilycorp.com or email your POs directly to orders@lilycorp.com for instant 1-hour order processing."*

---

## 5. High-Margin Target Catalog

| Category | Typical Items | Gross Margin | Reorder Frequency |
| :--- | :--- | :--- | :--- |
| **Static Mixers** | Disposable plastic nozzles, bell mixers, spiral elements | 70% – 80% | High (Every job) |
| **Injection Ports & Couplers** | Surface ports, corner ports, brass fittings, nylon adapters | 65% – 75% | High (Weekly/Monthly) |
| **Wear Parts & Hoses** | High-pressure fluid hoses, O-rings, check valves, seals | 60% – 70% | Medium (Quarterly) |
| **Maintenance & Flush** | Seal rebuild kits, pump lubricants, solvent flush kits | 55% – 65% | Medium (As needed) |

*(Engineered custom builds, high-pressure injection pumps, and custom dispenser rigs continue to route to Bob / Dave J for phone consultation).*

---

## 6. Success Metrics & ROI

* **Debt Coverage:** Generate **$15,000 to $25,000/month** in automated high-margin parts volume by Day 60 (directly covering the Chase SBA loan payment).
* **Labor Efficiency:** Save **15–20 hours/week** across office staff, cutting order processing time from 15 minutes per order to under 30 seconds.
* **Capture Rate:** Zero lost revenue from after-hours contractor inquiries or busy morning phone lines.
* **Customer Satisfaction:** 100% same-day order acknowledgment and packing slip dispatch.
