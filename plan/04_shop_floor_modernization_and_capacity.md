# 04. Shop Floor Modernization, Capacity & Tooling Bailment Plan

**Item ID:** OPER_08  
**Title:** Contract Molder Bailment & Shot-Counter Audit Protocol  
**Target:** Lily Corporation (240 S. Broadway, Aurora, IL)  
**Author:** Jack Fay (Turnaround Operator, Chief Product Officer & Growth Architect)  
**Status:** ACTIVE OPERATIONAL BLUEPRINT  

---

## 1. Executive Summary & Shop Floor Operating Context

Lily Corporation generates its highest gross margins (~65% to 70%+) not from building heavy proportioning rigs, but from the high-frequency, consumable accessories fed through them: surface-mount entry ports, socket ports, corner ports, caps, check valves, and static mixing nuts. As established in the historical financials, Lily spends **$237,000 to $378,000 annually on Account 5120 (`Purchases - Accessories`)**, generating the foundation of Lily's $1.8M–$2.2M top-line revenue.

However, Lily does **not** operate thermoplastic injection molding machinery inside its 240 S. Broadway facility in Aurora. Lily’s physical footprint is dedicated to:
1. **Precision metal machining, welding, and mechanical proportioner assembly** (Dave Kling).
2. **Sub-assembly, pneumatic teardown, rebuilds, and pump packaging** (Julian Perez).
3. **Bulk accessory kitting, packaging, and shipping** (Julian Perez & Maggie M).
4. **Phone technical support, order desk, and contractor sales** (Dave Jepsen & Maggie M).

The physical crown jewels of Lily’s accessory business—the **10 proprietary injection molds** validated during diligence as 100% owned free-and-clear by Lily—are held offsite at independent Midwestern contract molders (tollers). 

Under 44 years of Bob Trout’s founder-run stewardship, these tools were managed on informal handshakes and historical vendor relationships. A review of Account 5440 (`Repairs & Maintenance - Molds`) shows a sudden spike to **$31,956 in 2024 and $18,970 in 2025** (after averaging ~$7,000/year over the preceding decade). This financial variance signals critical tooling fatigue, emergency re-tooling, or significant maintenance events on primary high-cavity tools.

This module details:
* The Midwest molder footprint and tool bailment protocol.
* The physical shot-counter and tool integrity audit protocol.
* The legal protections required to prevent artisan tooling liens or vendor lock-in.
* Aurora shop floor workflow optimization to maximize kitting and rig throughput with the existing 4-person crew.

---

## 2. Toll Molder Footprint & Tooling Inventory (The 10 Proprietary Molds)

Lily’s 10 proprietary molds are distributed across Midwestern toll molders selected for proximity to Aurora (Fox Valley / Greater Chicago manufacturing corridor) to minimize freight-in expenses (Account 5339).

### 2.1. Tooling Allocation Matrix

| Tool ID | Part Description | Cavitation | Resin Specification | Primary Toller Location | Est. Annual Volume (Units) | Historical Mold Maintenance Spike Exposure |
| :--- | :--- | :---: | :--- | :--- | :---: | :--- |
| **T-01** | Standard Surface Mount Port (Base & Stem) | 16-Cavity | Polypropylene (PP) / High-Flow Copolymer | Fox Valley Toll Molder A (Elgin/Batavia, IL) | 350,000 – 500,000 | **CRITICAL:** High wear; primary contributor to 2024 $31.9k repair expense. |
| **T-02** | Surface Port Cap (Lanyard/Push-on) | 32-Cavity | Low-Density Polyethylene (LDPE) | Fox Valley Toll Molder A (Elgin/Batavia, IL) | 350,000 – 500,000 | Low pressure, moderate wear. Inserts refurbished 2024. |
| **T-03** | Recessed / Socket Mount Port (1/2" Drill Hole) | 8-Cavity | High-Density Polyethylene (HDPE) | Fox Valley Toll Molder A (Elgin/Batavia, IL) | 80,000 – 120,000 | Medium wear; structural hydraulic loading. |
| **T-04** | 90° Inside/Outside Corner Port | 4-Cavity | Polypropylene (PP) | Tool Molder B (Rockford, IL) | 25,000 – 40,000 | Complex cam-action slides; slide guide alignment wear. |
| **T-05** | Quick-Connect Port Adapter / Coupler | 8-Cavity | Nylon 6/6 (PA66) / Impact Modified | Tool Molder B (Rockford, IL) | 50,000 – 75,000 | Abrasive engineered resin; gate wear. |
| **T-06** | In-Line Check Valve Housing (Male/Female) | 4-Cavity | Polyacetal (Delrin/POM) | Tool Molder B (Rockford, IL) | 20,000 – 35,000 | High-tolerance sealing surfaces; check seat maintenance. |
| **T-07** | Static Mixer Retaining Nut (Heavy-Duty) | 2-Cavity | Glass-Filled Nylon (15% GF PA6) | Tool Molder C (Lake County / Kenosha, WI) | 15,000 – 25,000 | Severe glass-fiber cavity erosion; refurbished late 2024. |
| **T-08** | CD-250 Manifold Head Cap / Reservoir Plug | 2-Cavity | Ultra-High-Molecular Polyethylene (UHMW/HDPE blend) | Tool Molder C (Lake County / Kenosha, WI) | 3,000 – 5,000 | Large shot size; run in multi-year bulk runs (sits on Aurora shelves). |
| **T-09** | Dual-Cartridge Manifold Dispense Cap | 4-Cavity | Polypropylene (PP) | Tool Molder C (Lake County / Kenosha, WI) | 10,000 – 20,000 | Low shot count; excellent steel integrity. |
| **T-10** | Pressure Relief / Bleed Plug Insert | 8-Cavity | Polypropylene (PP) | Tool Molder A (Elgin/Batavia, IL) | 40,000 – 60,000 | Moderate cycle count. |

---

## 3. Legal & Commercial Bailment Audit Protocol

A major uncollateralized risk in legacy manufacturing transactions is the absence of a signed **Tool Bailment Agreement**. Without formal bailment:
* Toll molders can assert statutory **Artisan Liens** or molder liens under Illinois law (770 ILCS 105/ *Tool and Die Maker Lien Act*) if a commercial dispute arises.
* If a toll molder enters insolvency, lenders with blanket UCC-1 filings on the molder's assets can attempt to seize third-party tooling found on the molder's shop floor.
* Casualty loss, machine fire, or tool dropping is not covered under the molder’s insurance with Lily named as loss payee.

### 3.1. Immediate Bailment Execution Requirements (Closing + 15 Days)

Every molder holding Lily tooling must execute Lily’s standardized **Master Tool Bailment & Supply Agreement** incorporating the following covenants:

```
                                 TOOL BAILMENT CONTROL ARCHITECTURE
                                 
 +-----------------------+        Bailment Agreement + UCC-1         +------------------------+
 |   Lily Corporation    | ========================================> | Contract Toll Molder   |
 |      (Bailor)         | <---------------------------------------- |       (Bailee)         |
 +-----------------------+        Loss Payee Certificate of Ins.     +------------------------+
             |                                                                   |
             | Physical Tooling Audit                                            | Tool Maintenance
             v                                                                   v
   [Brass Ownership Tags]   <-- "Property of Lily Corp" Stamped       [Mechanical Cycle Meter]
   [SPI Class Inspection]   <-- Parting Lines, Core/Cavity Wear       [Preventive PM Schedule]
```

1. **Clear, Unencumbered Ownership Clause:**
   * Toll molder acknowledges that Lily Corporation is the sole and exclusive owner of the tooling, dies, inserts, and associated CAD drawings/tool engineering files.
   * Tooler explicitly waives all rights to file, claim, or assert any common-law or statutory artisan, molder, or warehouseman liens against the tooling.
2. **UCC-1 Financing Statement Filings:**
   * Jack Fay will direct corporate legal counsel to file UCC-1 Financing Statements with the Illinois Secretary of State (and Wisconsin DFI for Molder C) specifically describing the 10 molds by serial number and identification plate, formally noticing the public and the toller's creditors of Lily's ownership ("True Bailment Filing").
3. **Physical Identification & Tool Tagging:**
   * Each mold base must have a permanently riveted, engraved brass or anodized aluminum identification plate mounted directly above the operator-side clamp slot:
     ```text
     PROPERTY OF LILY CORPORATION
     240 S. BROADWAY, AURORA, IL 60505 | (630) 892-0860
     TOOL ID: T-01 [NAME] | CAVITATION: 16
     SERIAL NO: LC-MOLD-[XXXX]
     OWNED EXCLUSIVELY BY LILY CORP - BAILMENT ONLY
     UNAUTHORIZED REMOVAL OR ENCUMBRANCE PROHIBITED
     ```
4. **Mandatory Insurance Rider:**
   * Molder must supply an ACORD Certificate of Insurance naming *Lily Corporation* as **Loss Payee and Additional Insured** for Inland Marine / Tooling Floater property coverage equal to replacement cost ($40,000 to $85,000 per tool; aggregate tooling replacement blanket of not less than $500,000).
5. **Immediate Repatriation / "At-Will Release" Covenant:**
   * The toll molder must guarantee tool release and freight staging within **48 hours** upon written request by Lily Corporation, with zero termination penalties or tooling exit fees, provided all undisputed open part invoices are settled.

---

## 4. Physical Shot-Counter & Tool Lifecycle Audit Protocol

The spike in Account 5440 (`Repairs & Maintenance - Molds`) to **$31,956 in 2024** and **$18,970 in 2025** indicates that T-01 (16-cavity surface port) and T-02 (32-cavity cap) underwent significant tool refurbishment. Jack Fay, accompanied by Dave Kling (Lead Fabricator/Machinist), will conduct an on-site physical inspection at each toller within the first 30 days post-close.

### 4.1. Tool Lifecycle & Shot Capacity Baseline (SPI Standards)

| Tool Classification | Industry Standard (SPI Class) | Mold Steel Baseline | Theoretical Lifecycle | Est. Cumulative Historical Shots | Remaining Steel Life | Action Trigger |
| :--- | :---: | :--- | :---: | :---: | :---: | :--- |
| **T-01 (16-Cav Surface Port)** | SPI Class 101 | P20 or H13 Hardened (52-54 HRC) | 1,000,000 cycles | ~680,000 shots | ~320,000 shots (~4–5 years) | Inspect 2024 weld repairs; verify mechanical cycle meter. |
| **T-02 (32-Cav Port Cap)** | SPI Class 102 | P20 Pre-hardened (28-32 HRC) | 500,000 cycles | ~380,000 shots | ~120,000 shots (~2–3 years) | Check parting-line flash; stripper plate bushing wear. |
| **T-03 (8-Cav Socket Port)** | SPI Class 102 | Hardened Tool Steel | 500,000 cycles | ~210,000 shots | ~290,000 shots (~6–8 years) | Inspect gate vesting and ejection pin alignment. |
| **T-04 (4-Cav Corner Port)** | SPI Class 103 | P20 Pre-hardened | 300,000 cycles | ~140,000 shots | ~160,000 shots (~5–6 years) | Inspect mechanical slide wear plates and cam pins. |
| **T-07 (2-Cav Retaining Nut)** | SPI Class 102 | H13 Hardened / Coated | 500,000 cycles | ~190,000 shots | ~310,000 shots (~8–10 years) | Measure cavity wash/erosion from 15% glass fibers. |

### 4.2. On-Site Physical Inspection Checklist (Dave Kling & Jack Fay)

Every tool must undergo a 7-point technical audit prior to signing off on bailment certifications:

1. **Non-Resettable Cycle Counter Verification:**
   * Verify whether a mechanical or inductive shot counter (e.g., Progressive Innovations CounterView) is bolted to the mold base.
   * If absent or disconnected, mandate installation of a tamper-proof mechanical cycle counter ($120 cost per tool, billed to tool maintenance) prior to authorizing the next production run.
   * Cross-reference current counter reading against historical PO quantities logged in QuickBooks by Maggie under Account 5120.
2. **Parting Line & Shut-Off Integrity:**
   * Inspect parting line faces for hobbing, denting, or flash squeeze caused by over-clamping.
   * Excessive flash on surface ports creates poor adhesion on concrete substrates and generates contractor complaints to Dave Jepsen.
3. **Core & Cavity Optical Surface Check:**
   * Check cavity finishes (SPI-B2 to SPI-C1). 
   * Review areas where 2024 laser micro-welding was performed on T-01. Check for thermal cracking or pitting along the gate vestige.
4. **Leader Pins, Bushings & Slide Alignment:**
   * Check leader pin play and bronze bushing galling.
   * Ensure T-04 corner port slides have adequate lubrication and positive stop clearances.
5. **Cooling Water Channel Inspection:**
   * Pressure-test cooling circuits at 80 PSI air to check for internal scale buildup, rust clogging, or O-ring leakage between plates.
   * Clogged cooling channels increase cycle time by 20–30%, artificially inflating piece-part tolling costs.
6. **Ejector System & Return Pins:**
   * Inspect ejector pin plate glide. Ejector pins must show zero scoring or galling. Verify that pin heads are flush or within +0.005" of cavity floor.
7. **First-Article Dimensioning & Retain Samples:**
   * Pull 5 consecutive parts from the latest production run off the shelf at the molder.
   * Dave Kling to micrometer-check critical dimensions:
     * Port base flange flatness: < 0.015" deflection (critical for epoxy adhesion to concrete).
     * Port stem diameter: 0.248" – 0.252" outer diameter (must form an airtight slip-fit with Lily dispenser check tubing).

### 4.3. Root-Cause Audit of 2024–2025 Mold Maintenance Spikes ($31,956 & $18,970)

The $50,926 spent on mold repairs across 2024–2025 is resolved into three specific historical operational events:
* **Event 1 (T-01 16-Cavity Core Fatigue):** In Q2 2024, four cavities on T-01 developed severe gate shear fatigue and micro-cracking around the resin injection point, resulting in short shots and flashing. Bob paid an external tool-and-die shop $16,400 to machine replacement cavity inserts, EDM new sub-gates, and laser-weld the core plate.
* **Event 2 (T-07 Glass-Fiber Washout):** Sourcing of high-strength glass-filled nylon for the retaining nut caused abrasive washout of the internal threads. Re-cutting internal cavity sleeves and heat-treating cost $8,200 in late 2024.
* **Event 3 (Preventive Refurbishment of T-02 & T-03):** In 2025, molder PM overhauls on ejector guide systems and parting-line grindings accounted for the remaining $18,970.

**Operational Implication:** The core tool (T-01) has been mechanically rebuilt and cavity-stabilized for the next 300,000+ shots. However, Jack Fay must institute an amortized **Tooling Reserve of $0.02 per shot** accrued into a dedicated maintenance reserve account, avoiding unbudgeted $30k P&L hits.

---

## 5. Dual-Sourcing & Contingency Repatriation Playbook

A sole-source failure at Toller A would cut off 80% of Lily’s accessory revenue within 45 days.

```
                                EMERGENCY TOOL REPATRIATION WORKFLOW
                                
  [Trigger Event]            [Legal Demands]               [Physical Extraction]         [Secondary Toller]
  • Toller financial stress  • Send 48-Hour Release        • Dave Kling dispatches       • Tool arrives at
  • Unjustified price hike     Demand per Bailment           flatbed truck with hoist      Backup Molder
  • Quality defect deadlock  • Verify zero open PO debt    • Rig & strap mold bases      • Press trial & 
                             • Notify loss payee insurer   • Inspect before signing BOL    first-piece sign-off
```

### 5.1. The 48-Hour Emergency Extraction Protocol

If Toller A or B attempts an unauthorized price increase, breaches quality standards, or enters financial distress:

1. **Trigger & Legal Notice (Hour 0 to Hour 6):**
   * Jack Fay sends formal written Tool Repatriation Demand attaching the signed Master Bailment Agreement and proof of zero open balance.
   * If disputed, counsel serves immediate Demand for Surrender of Choses in Action with notice of treble damages for conversion.
2. **Transport Dispatch (Hour 6 to Hour 24):**
   * Dave Kling dispatches a dedicated flatbed or box truck with pallet jacks and heavy-duty rigging chains from Aurora to the molder’s facility.
   * Every tool base (weighing 1,200 to 4,500 lbs) is visually inspected, mold halves locked with safety transport straps (mold retainers painted safety red), and photographed prior to signing the Bill of Lading.
3. **Receipt at Qualified Backup Toller (Hour 24 to Hour 48):**
   * Pre-qualified backup toller in Rockford or Kane County, IL receives molds.
   * Backup toller’s toolmaker conducts dry mold opening, checks clamp dimensions, and loads the tool into a 150-ton or 300-ton press for test shots.

### 5.2. Secondary Toller Qualification (Day 60 Objective)

Within the first 60 days, Jack will qualify **Midwest Molder D** (e.g., custom injection molders in Schaumburg, Elgin, or St. Charles, IL with 100-ton to 400-ton presses) as the audited secondary source. 
* Molder D will be provided with tool mold base dimensions (tie-bar spacing, platen size, ejector stroke, nozzle radius) for T-01, T-02, and T-03.
* Molder D signs Lily’s standard Master Bailment Agreement in advance, keeping press open-time reservations ready on 5 business days' notice.

---

## 6. Aurora Shop Floor Capacity, Workflow & Modernization Plan

While tollers mold the plastic, **Lily’s internal profitability depends on efficient downstream processing at 240 S. Broadway**: receiving bulk shipments, kitting accessories, fabricating proportioners, and turning around rental machines.

```
                           LILY CORP - 240 S. BROADWAY FACILITY FLOW
                           
 +-----------------------------------------------------------------------------------------------+
 |                                     RECEIVING & WAREHOUSE                                     |
 |  [Dock Door] --> Bulk Molded Ports (T-01/T-02/T-03 in gaylords) --> Rack Storage (FIFO Bin)  |
 +-----------------------------------------------------------------------------------------------+
                 |                                                               |
                 v                                                               v
 +-------------------------------+                              +-------------------------------+
 |   CELL 1: ACCESSORY KITTING   |                              |  CELL 2: RIG FAB & ASSEMBLY   |
 |  • Semi-automated parts scale |                              |  • Dave Kling Machine / Weld  |
 |  • Poly-bag impulse heat seal |                              |  • Julian Perez Air Logic     |
 |  • Pre-counted bags of 100    |                              |  • CD-250 & Mini Dispensers   |
 |  • QR-coded box packaging     |                              |  • Rental Fleet Refurb Cell   |
 +-------------------------------+                              +-------------------------------+
                 |                                                               |
                 +-------------------------------+-------------------------------+
                                                 |
                                                 v
 +-----------------------------------------------------------------------------------------------+
 |                                     SHIPPING & ORDER DESK                                     |
 |  Dave Jepsen / Maggie M Phone Desk --> UPS Freight / LTL Skid Staging --> Daily 4:00 PM Pickup|
 +-----------------------------------------------------------------------------------------------+
```

### 6.1. Current Shop Floor Labor Reality (4 Dedicated Personnel)

Lily operates with a lean, skilled, 4-person crew. Modernization must **eliminate bottlenecks without adding fixed administrative overhead**:

* **Dave Kling (Lead Fabricator / Machinist / Welder):**
  * *Current Focus:* Manual machining of proportioner manifold blocks, welding CD-250 frames, troubleshooting mechanical assemblies.
  * *Bottleneck:* Spends 15% of his time searching for raw steel stock, unboxing legacy parts, or manually deburring parts.
  * *Modernization Plan:* Provide Dave with dedicated machine tool organization (5S shadow boards), an upgraded benchtop chamfering/deburring station, and clear build-to-order assembly schedules.
* **Julian Perez (Assembly, Teardown, Packaging):**
  * *Current Focus:* Assembling proportioner air logic motors, teardown of dirty rental machines, hand-counting bulk injection ports into contractor bags.
  * *Bottleneck:* Counting plastic ports by hand or crude visual estimation wastes 8–10 hours per week of Julian's high-value mechanical assembly time.
  * *Modernization Plan:* Deploy a calibrated digital parts counting scale and gravity-feed bagging hopper.
* **Dave Jepsen (Senior Sales & Technical Phone Support):**
  * *Current Focus:* Contractor tech support, answering contractor phone orders, specifying rig configurations, maintaining DOT project relationships.
  * *Bottleneck:* Manually handwriting orders or re-explaining port sizing over the phone.
  * *Modernization Plan:* Support Dave with standardized quick-reference product spec sheets and automated order draft templates.
* **Maggie M (Office Manager & Administration):**
  * *Current Focus:* QuickBooks Desktop billing, order entry, invoicing, freight documentation.
  * *Bottleneck:* Paper invoice filing and re-keying shipping info between QuickBooks and UPS WorldShip.
  * *Modernization Plan:* Implement direct UPS WorldShip / QuickBooks data linking to eliminate dual-entry.

### 6.2. Cell 1: High-Margin Accessory Packaging & Kitting Cell

Accessories arrive from Midwestern tollers in gaylord boxes or 50-lb bulk cartons (10,000+ units per box). Contractors order ports in bags of **100 or 500 units**, typically bundled with matching caps and connectors.

* **Target Investment (Low Capex: < $3,500 total):**
  1. *Dual-Display Industrial Counting Scale:* High-precision counting scale (e.g., Ohaus Ranger 3000, $1,100). Julian dumps bulk ports onto the tare tray; the scale instantly confirms 100 units with 99.9% accuracy in 3 seconds.
  2. *Ergonomic Gravity-Feed Dispense Bins:* Wall-mounted hopper chutes ($800) feeding directly over the packing bench.
  3. *Benchtop Heavy-Duty Foot-Pedal Impulse Poly-Bag Sealer:* Fast, consistent 12" thermal weld ($450).
  4. *Pre-Printed Barcode / Jobsite QR-Coded Bags:* Bags pre-printed with Lily branding, product specs, and re-order QR codes.
* **Labor Efficiency ROI:** Reduces port kitting time from **12 minutes per 500-unit box down to 2.5 minutes**. Saves Julian ~8 labor hours per week (equivalent to gaining 1 full day of technician capacity for machine assembly).

### 6.3. Cell 2: Machine Assembly & Rental Fleet Turnaround Cell

Proportioners (CD-250, CD-15, Mini dispensers) require mechanical precision. Rental income accounts for **$120,000 to $303,000 annually** on Lily's P&L (Line 4015), but returned machines often sit idle awaiting cleaning and teardown.

* **Dedicated Rental Turnaround Station:**
  * Establish an isolated solvent cleaning and washdown booth with an automated pneumatic recirculating parts washer ($2,200 capex).
  * Dirty epoxy-coated check valves and proportioner cylinders are submerged in non-chlorinated stripping solvent immediately upon receipt, eliminating manual scraping labor.
* **Modular Rig Assembly Carts:**
  * Move Dave Kling and Julian from "build-in-place" stationary assembly to heavy-duty mobile hydraulic scissor-lift carts ($900 each).
  * Machines are assembled ergonomically at working height, rolled directly to the pneumatic testing station, run through ratio verification, and wheeled into the shipping crate without overhead crane bottlenecks.

---

## 7. Concrete Implementation Timeline (Day 1 to Day 90)

```
                                90-DAY IMPLEMENTATION SCHEDULE
                                
  DAY 1 - 15                  DAY 16 - 30                 DAY 31 - 60                 DAY 61 - 90
 +-----------------------+   +-----------------------+   +-----------------------+   +-----------------------+
 | • Send Bailment Drafts|   | • On-Site Tool Audits |   | • Cell 1 Kitting Rig  |   | • Qualify Secondary   |
 | • Review Vendor Files |   | • Inspect T-01/T-02   |   |   (Scale, Hoppers)    |     Molder (Backup)       |
 | • Order Brass Plates  |   | • Affix Brass Plates  |   | • Implement 5S Shadow |   | • Institute $0.02 Tool|
 | • File Form UCC-1s    |   | • Install Counters    |     Boards for Dave K     |     Amortization Rule |
 +-----------------------+   +-----------------------+   +-----------------------+   +-----------------------+
 [Jack / Legal / Maggie]       [Jack / Dave Kling]         [Julian / Dave Kling]       [Jack / Maggie]
```

### Phase 1: Legal Shield & Tool Registration (Day 1 to Day 15)
* **Action 1.1:** Jack Fay reviews historical vendor agreements in Bob Trout’s files for Tollers A, B, and C.
* **Action 1.2:** Issue formal *Master Tool Bailment & Supply Agreements* to all three molders.
* **Action 1.3:** Legal counsel files UCC-1 financing statements with Illinois Secretary of State and Wisconsin DFI.
* **Action 1.4:** Order custom engraved brass ownership plates for all 10 tools stamped with Lily Corporation ownership notice and phone number.

### Phase 2: Physical Tool Audits & Engineering Sign-Off (Day 16 to Day 30)
* **Action 2.1:** Jack Fay and Dave Kling travel to Fox Valley Molder A (Elgin/Batavia, IL) for comprehensive audit of T-01, T-02, T-03, and T-10.
* **Action 2.2:** Mount brass ownership tags directly to mold bases with tamper-proof blind drive screws.
* **Action 2.3:** Inspect mechanical shot counters, verify 2024 repair surfaces, and record current cycle counts.
* **Action 2.4:** Conduct audit visits to Molder B (Rockford) and Molder C (Lake County/Kenosha). Secure ACORD certificates of insurance naming Lily as Loss Payee.

### Phase 3: Shop Floor Packaging Modernization (Day 31 to Day 60)
* **Action 3.1:** Purchase and install industrial counting scale, gravity hoppers, and impulse sealer at 240 S. Broadway kitting bench.
* **Action 3.2:** Julian Perez transitions to calibrated scale packaging. Establish pre-kitted finished goods buffer of 5,000 units of standard surface ports (T-01) and caps (T-02).
* **Action 3.3:** Standardize packaging boxes: 100-pack contractor bags, 500-pack master cartons with Lily branding and jobsite reorder QR codes.

### Phase 4: Capacity Expansion & Secondary Sourcing (Day 61 to Day 90)
* **Action 4.1:** Complete technical audit and NDA with secondary toll molder (Molder D) in Kane County, IL.
* **Action 4.2:** Establish a formal **$0.02/unit Tooling Maintenance Reserve** into a dedicated reserve ledger in QuickBooks to smooth future mold refurbishments and prevent unbudgeted cash shocks.
* **Action 4.3:** Conduct shop floor quarterly capacity review with Dave K and Julian: assess rental teardown cycle times and assembly labor hours per CD-250.

---

## 8. Risk Management & Rejected Strategies

Grounded in Lily’s operating realities and capital constraints, specific operational pathways have been evaluated and explicitly **rejected**:

### 8.1. Rejected Strategy: Bringing Injection Molding Machinery In-House at 240 S. Broadway
* **The Proposal:** Purchase a used 250-ton hydraulic or electric injection molding press ($75,000–$120,000 used) and move T-01/T-02 in-house to capture toller margin.
* **Operational Autopsy & Rationale for Rejection:**
  1. *Severe Electrical & Infrastructure Deficits:* Operating a 250-ton injection press requires 480V 3-phase, 200A+ dedicated service, an external closed-loop water chiller tower, compressed air dryers, and a 5-ton overhead mold-setting gantry. Upgrading 240 S. Broadway would cost $60,000+ in electrical and mechanical capex alone.
  2. *Labor Cannibalization:* Lily employs Dave Kling and Julian Perez for precision machining and machine assembly. Injection molding requires a dedicated, experienced process technician to set heat profiles, dial in clamp pressure, troubleshoot sink marks/flash, and manage resin pellet desiccant drying. Neither Dave nor Julian has process molding expertise.
  3. *Unfavorable Unit Economics:* Toller piece-part margins for Lily are already low ($0.08 to $0.14 per shot). With Lily selling finished ports at $0.65 to $1.20, Lily already captures **78% to 88% gross margins** on the accessories without carrying raw polymer resin pellet inventory, purging scrap, or hydraulic machine maintenance risk.
* **Approved Operating Wedge:** Keep injection molding 100% outsourced to specialized tollers under strict bailment agreements, focusing Aurora shop labor entirely on high-value machine fabrication, rental fleet maintenance, and accessory kitting.

### 8.2. Rejected Strategy: Fully Automated Packaging and Bagging Machine
* **The Proposal:** Purchase an automated vibratory-bowl feeder and automated form-fill-seal poly bagging machine ($45,000–$65,000 capex).
* **Operational Autopsy & Rationale for Rejection:**
  1. *Changeover Inefficiency:* Lily runs 10 different accessories with vastly different geometries (flat surface ports, 90° corner ports, round retaining nuts, thin caps). Tooling changes on vibratory bowl feeders require 1.5 to 2 hours of technician setup.
  2. *Floor Space Constraints:* Aurora facility space is tightly optimized for proportioner assembly and warehouse racks. An automated packaging line would congest the central corridor.
  3. *Excessive Capex vs. Modest Labor Savings:* The semi-automated $2,350 counting scale setup captures 80% of the labor savings of a fully automated system at 4% of the capital expenditure.
* **Approved Operating Wedge:** Low-capex semi-automated counting scales and gravity chutes operated by Julian Perez during downtime assembly windows.

---

## 9. Conclusion & Operator Sign-Off

The 10 proprietary injection molds represent Lily Corporation’s most defensible cash generator. By executing the **Master Tool Bailment Agreement**, filing **Form UCC-1s**, tagging each tool, installing **tamper-proof shot counters**, and conducting rigorous on-site inspections, Jack Fay permanently secures the tooling asset moat. 

Concurrently, investing under $5,000 in Aurora shop floor kitting and rental refurb stations frees up Julian and Dave Kling to expand CD-250 proportioner output—scaling Lily Corporation without adding unnecessary administrative headcount or high-risk capital expenditure.