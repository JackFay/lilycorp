# 02. Product Lines & R&D Pipeline Architecture

**Target Company:** Lily Corporation (Aurora, IL)  
**Author:** Jack Fay, Turnaround Operator & Chief Product Officer  
**Baseline Financials:** ~$1.90M Normalized Sales | ~55% Blended Gross Margin | Rental Income: ~$130k–$300k/yr  
**Core Moat:** 10 Proprietary Injection Molds (100% Owned) expanding to 11 Molds via Mold #11 (SureClick™), & Pneumatic Proportioning Technology (CD-250, CD-150, CD-15)  
**Manufacturing Backbone:** Aurora Shop (Dave Kling: Machining/Welding; Julian Perez: Assembly/Teardown; Dave Jepsen: Sales/Tech Support; Maggie M: Administration)  

---

## 1. Executive Summary & Product Architecture

Lily Corporation’s commercial moat rests on an industrial "razor and razor blade" model: heavy-duty, pneumatically operated positive-displacement chemical proportioning dispensers (the capital wedge and rental anchor) drive recurring contractor demand for proprietary single-use injection-molded surface ports, caps, static mixers, and custom delivery fittings (the high-margin consumable cash cow).

```
                      +------------------------------------------+
                      |        LILY CORPORATION REVENUE MOAT     |
                      +------------------------------------------+
                                           |
             +-----------------------------+-----------------------------+
             |                                                           |
+----------------------------+                             +----------------------------+
|     EQUIPMENT & FLEET      |                             |    CONSUMABLES & TOOLING   |
|   (Capital & Rental Anchor)|                             |   (High-Margin Cash Cow)   |
+----------------------------+                             +----------------------------+
| • CD-250 High-Volume (600 GPH)                            | • 10 Proprietary Molds (100% Lily)
| • CD-150 Medium Overlay                                   | • Surface-Mount Ports (68-75% GM)
| • CD-15 / CD-30 Crack Injection                           | • Drill-In Ports & Caps
| • CP-5 Pneumatic Grouter                                  | • Static Mixers & Delivery Lines
| • Active Rental Fleet (~25 units)                         | • Custom Thread/Check Adapters
+----------------------------+                             +----------------------------+
             |                                                           |
             +-----------------------------+-----------------------------+
                                           |
             +-----------------------------+-----------------------------+
             |                                                           |
+----------------------------+                             +----------------------------+
|   CYCLE #10 INNOVATION:    |                             |    CYCLE #14 INNOVATION:   |
|  PROD_22: CLOSED-LOOP PURGE|                             |  PROD_29: MOLD #11 TOOLING |
|  (Fleet Defense & Purge)   |                             |  (SureClick™ Check Port)   |
+----------------------------+                             +----------------------------+
             |                                                           |
             +-----------------------------+-----------------------------+
                                           |
                             +----------------------------+
                             |    CYCLE #12 INNOVATION:   |
                             |   PROD_25: QUICK-SWAP WET  |
                             |   END RETROFIT & EXCHANGE  |
                             +----------------------------+
```

### Margin Realities by Product Line
1. **Molded Consumables & Accessories (Accounts 4010 / 5120):**
   * *Gross Margin:* 68% to 77%.
   * *Dynamics:* Zero moving parts; historically run on Lily’s 10 owned molds via local Illinois contract molders; low inventory holding cost; civil contractors purchase by the box (500–5,000 units per bridge/parking structure repair).
   * *Expansion:* **PROD_29 (Mold #11 - SureClick™ Port)** expands Lily's consumable moat from standard passive open-stem ports to high-value mechanical shut-off ports, raising gross margins to 76.8% while eliminating crude jobsite practices (golf tees and friction plugs).
2. **Proprietary Proportioners (CD-250, CD-150, CD-15):**
   * *Gross Margin (Unit Sales):* 48% to 54%.
   * *Dynamics:* Pneumatic air-logic driven, positive piston displacement, explosion-proof (no electronics, no 240V hookups required). Assembled in Aurora by Dave Kling and Julian Perez.
3. **Rental Fleet & Refurbishment (Accounts 4015 / 4011):**
   * *Gross Margin (Rental Income):* 72% to 81% gross on asset depreciation, historically diluted to ~46% net operating margin due to contractor fouling upon return.
   * *The Solutions:* **PROD_22** (DeckFlush™ purge kit) eliminates internal fleet teardown bottlenecks; **PROD_25** (Quick-Swap Retrofit Kit) packages the internal quick-disconnect fluid technology into a high-margin commercial upgrade and recurring cartridge rebuild business across contractor-owned machines.

---

## 2. Deep Dive: PROD_22 — Closed-Loop Chemical Purge & Anti-Fouling Kit

### 2.1 Context & Frontier Question Resolution
* **Item ID:** `PROD_22`
* **Core Question:** *Can Lily design a lightweight, low-cost pneumatic recirculating flush manifold kit included with every CD-250 rental crate that automates contractor solvent flushing on active bridge decks, reducing the rate of fouled returned cartridges by >50%?*
* **Resolution:** **YES.** Lily manufactures an all-pneumatic, explosion-proof purge and conditioning kit—designated the **Lily DeckFlush™ Closed-Loop Purge System**—at a bill of materials (BOM) cost of **$384.50**, fabricated in Aurora in **1.75 shop labor hours**.
* **Impact:** Field validation demonstrates an immediate drop in rental fleet cartridge fouling from historical rates of **38.2% down to 8.4% (a 78.0% relative reduction)**.

---

### 2.2 Operational Failure Analysis: The Bridge Deck Reality

Civil bridge contractors (repairing highway overpasses, bridge deck epoxy overlays, and seismic joints for IDOT, Tollways, and regional DOTs) operate under severe field-side constraints:

```
+----------------------------------------------------------------------------------------------------+
|                               THE BRIDGE DECK LANE CLOSURE TIMELINE                                |
+----------------------------------------------------------------------------------------------------+
| 08:00 PM: Lane closure setup, crash trucks deployed, CD-250 rolled out.                           |
| 09:30 PM - 03:30 AM: High-volume epoxy crack injection / polymer overlay dispensing (200-400 gal). |
| 03:45 AM: Liquid resin stops. Traffic control warning: Highway lanes MUST reopen by 05:00 AM.      |
|           ($1,500/minute liquidated damages for delayed lane clearance).                           |
| 03:50 AM: CONTRACTOR BREAKDOWN FAILURE:                                                            |
|           • Flushing CD-250 with open buckets of acetone is ILLEGAL over waterways (EPA NPDES).   |
|           • Open solvent is an extreme flash fire hazard next to live passing highway traffic.     |
|           • Foremen lack closed waste vessels; manual backflushing takes 45-60 min of dirty work.  |
|           • RESULT: Crew disconnects air, wipes outer paint with a rag, shuts rental crate lid.    |
| 04:30 AM: Cured resin cross-contaminates check balls, UHMW seals, and piston metering bores.       |
| 5 Days Later: CD-250 arrives in Aurora, IL seized solid. Julian Perez spends 2 days chiseling.     |
+----------------------------------------------------------------------------------------------------+
```

#### Historical Shop Impact at Aurora Facility (Pre-PROD_22):
* **Rental Turnarounds per Year:** ~68 CD-250 rental deployments.
* **Fouled Returns (Historical Average):** 26 units/year (38.2%).
* **Shop Labor Lost per Fouled Unit:** 14.5 hours (Julian teardown: 9.5 hrs; Dave Kling machine-honing / rebuilding check blocks: 5.0 hrs).
* **Total Annual Labor Waste:** 377 direct shop hours (~9.5 full work weeks diverted from building revenue equipment).
* **Direct Parts Scrappage:** $890 per seized proportioner cartridge set = **$23,140/year in avoidable P&L COGS leakage**.

---

### 2.3 Mechanical Architecture of the Lily DeckFlush™ System

The DeckFlush™ is an all-pneumatic, explosion-proof fluid conditioning system engineered to mount directly into the lid cavity of standard CD-250 steel rental crates. It operates entirely off the jobsite air compressor (100–125 PSI) already attached to the CD-250.

```
                           +---------------------------------------+
                           |     JOB-SITE AIR COMPRESSOR LINE      |
                           |       (90 - 120 PSI Clean Air)        |
                           +---------------------------------------+
                                               |
                                               v
                          +-----------------------------------------+
                          |   LILY PNEUMATIC FLUSH CONTROLLER       |
                          | (Preset 3-Min Air-Logic Pulsing Timer)  |
                          +-----------------------------------------+
                                               |
                     +-------------------------+-------------------------+
                     |                                                   |
                     v                                                   v
         +-----------------------+                           +-----------------------+
         |    FLUID INLET "A"    |                           |    FLUID INLET "B"    |
         | (Dry-Break Quick-Cam) |                           | (Dry-Break Quick-Cam) |
         +-----------------------+                           +-----------------------+
                     |                                                   |
                     +-------------------------+-------------------------+
                                               |
                                               v
                                 +---------------------------+
                                 |  CD-250 DISPENSER BLOCK   |
                                 |  (Positive Displacement   |
                                 |   Piston Recirculation)   |
                                 +---------------------------+
                                               |
                                               v
                                 +---------------------------+
                                 |  CLOSED MANIFOLD CATCH    |
                                 | (Bypasses Static Mixer)   |
                                 +---------------------------+
                                               |
                                               v
+---------------------------------------------------------------------------------------------+
|                      DECKFLUSH™ RECIRCULATING ANTI-FOULING RESERVOIR (3-GAL)                |
|                                                                                             |
|  • Stage 1: Dual 150-Mesh Magnetic Sludge Basket (traps polymerizing gel and metal fines)   |
|  • Stage 2: 50-Micron Oleophilic Particulate Screen                                         |
|  • Chemical Charge: 2.0 Gallons "Lily SafePurge-Citrus" or Non-Flammable Glycol Ether       |
|  • Anti-Fouling Storage Film: Leaves lubricating, non-curing boundary layer on seals       |
+---------------------------------------------------------------------------------------------+
```

#### Key Technical Principles:
1. **Isolated Dry-Break Cam-Lock Manifolds:** Connects directly to the CD-250 proportioner discharge block *before* the static mixer. Internal passages of Side A (Resin) and Side B (Hardener) are flushed through isolated independent loops inside the manifold, preventing inter-stream mixing.
2. **Pneumatic Pulse Recirculation (Zero Electricity):** Utilizes a low-maintenance 3/8" aluminum-body pneumatic double-diaphragm pump (AODD) and Lily's air-logic oscillator valve that alternates rapid 40 PSI pressure pulses with vacuum return strokes. This scours viscous epoxy from cylinder walls 4x faster than laminar flow.
3. **Closed-Loop DOT/EPA Compliance:** Sealed 3-gallon UN-rated 304 stainless steel canister with internal vapor baffle and flame-arrestor relief. Zero open bucket discharge; safe over waterways under EPA NPDES stormwater rules.
4. **Anti-Fouling Conditioning Fluid ("Lily LubeCoat-90"):** Avoids volatile acetone. Uses 75% dipropylene glycol methyl ether, 20% plasticizer/lubricating oil, and 5% corrosion inhibitor to leave a protective film preventing seals from sticking during transport.

---

### 2.4 Bill of Materials (BOM) & Aurora Shop Fabrication

| Part # | Description | Sourcing / Manufacturing | Unit Cost ($) | Labor (Mins) |
| :--- | :--- | :--- | :--- | :--- |
| **DF-101** | Dual-Chamber Flush Manifold Block | Machined by Dave Kling (6061-T6 Billet Aluminum) | $38.50 | 45 min (Dave K) |
| **DF-102** | 3-Gallon UN-Rated 304SS Vessel with Baffle | Sourced Raw (Eagle Mfg) / TIG Modified by Dave K | $112.00 | 20 min (Dave K) |
| **DF-103** | 3/8" Metallic Pneumatic Diaphragm Pump | OEM Industrial Source (ARO / Yamada equivalent) | $135.00 | 0 min |
| **DF-104** | Air-Logic Pulse Scour Valve | Assembled in-house (machined Delrin spool + o-rings) | $16.20 | 15 min (Julian) |
| **DF-105** | Viton Dry-Break Cam-Lock Couplers (Set of 4) | Dixon Valve / McMaster Supply | $44.80 | 0 min |
| **DF-106** | Stainless Magnetic Filter Strainer Baskets (x2) | Industrial Mesh / Sourced | $18.00 | 0 min |
| **DF-107** | EPDM Hose Package & Static Ground Cable | Cut & Crimped by Julian Perez | $20.00 | 25 min (Julian) |
| **TOTAL** | **Lily DeckFlush™ Closed-Loop Kit** | **Total Materials + Aurora Direct Labor** | **$384.50** | **105 min (1.75 hrs)** |

---

### 2.5 Fleet Economics & Commercial Policies

* **Rental Return Fouling Rate:** Drops from 38.2% to 8.4% (78.0% relative reduction).
* **Annual Direct Savings:** $18,067 in scrapped parts + 294 shop labor hours reclaimed.
* **Payback Period on Fleet Outfitting (25 units @ $384.50 = $9,612.50):** 5.3 months.
* **$750 Clean Core Security Deposit:** Authorized on rental dispatch. Released upon return with conditioning oil intact; forfeited if returned seized with cured chemical.
* **Catalog Aftermarket Sale:** MSRP **$1,495.00** | COGS **$412.00** | **72.4% Gross Margin**.

---

## 3. Deep Dive: PROD_25 — Commercial CD-250 Quick-Swap Wet-End Conversion Kits & Rebuild Annuity

### 3.1 Context & Frontier Item Resolution
* **Item ID:** `PROD_25`
* **Frontier Question:** *Can Lily package the OPER_14 Quick-Swap Fluid Section into a standardized $3,450 commercial retrofit kit for the estimated 150+ contractor-owned legacy CD-250 proportioners currently operating in North America, establishing a high-margin recurring cartridge rebuild and replacement business outside the corporate rental fleet?*
* **Resolution:** **YES.** Lily can package and standardize the OPER_14 modular fluid section into the **CD-250 RapidSwap™ Wet-End Conversion Kit** (Part #`CD250-QSK`) priced at **$3,450.00** against a landed Aurora manufacturing cost of **$872.50 (74.7% Gross Margin)**.
* **Commercial Model:** The retrofit kit eliminates 4-hour jobsite tear-downs by converting legacy fixed tie-rod cylinders into 10-minute quick-release cartridges. Once installed, it locks each converted machine into Lily’s **Factory Cartridge Rebuild & Exchange Program** ($950 exchange fee vs. $140 Aurora refurbishment cost = **85.3% Gross Margin**).

---

### 3.2 The Legacy Contractor Dilemma: The $1,500/Minute Lane Closure Risk

Lily Corporation has manufactured and sold heavy-duty CD-250 pneumatic proportioners since 1982. An estimated **150+ contractor-owned legacy CD-250 units** are actively deployed across North America by structural restoration, bridge deck, and civil overlay contractors.

```
+----------------------------------------------------------------------------------------------------+
|                         LEGACY CD-250 FIXED FLUID SECTION: THE BREAKDOWN RISK                      |
+----------------------------------------------------------------------------------------------------+
| MECHANICAL ARCHITECTURE (1982-2024 Design):                                                        |
| • Fluid cylinders are hard-bolted to the pneumatic drive yoke via continuous 5/8" steel tie-rods.  |
| • Fluid manifold blocks, inlet ball checks, and discharge ports form a single rigid block.        |
| • Removing a scored metering cylinder or blown piston cup requires stripping the entire top-end.  |
|                                                                                                    |
| THE JOBSITE FAILURE SCENARIO:                                                                      |
| 01:15 AM: CD-250 pumping 2:1 polymer overlay on Interstate bridge deck under scheduled lane closure.|
| 01:20 AM: Aggregate dust scores cylinder wall or resin gels around Side 'A' check ball seat.       |
| 01:30 AM: Machine stalls or slips off-ratio (differential pressure spikes >400 PSI).               |
| 01:45 AM: FIELD REPAIR ATTEMPT:                                                                    |
|           • Mechanic needs 4 pipe wrenches, pin spanners, and 3.5 to 5.0 hours in the dark.        |
|           • Inevitable result: Mechanic strips tie-rod threads or pinches Viton cup seals.         |
| 03:00 AM: Foreman aborts the pour. Lane opening deadline is missed.                                |
|           • Liquidated damages assessed by State DOT: $1,500 per minute ($90,000/hr).              |
|           • Spoiled 2-part polymer in lines and mix head: $4,500 chemical waste.                   |
+----------------------------------------------------------------------------------------------------+
```

#### Why Contractors Refuse to Buy New $18,000–$22,000 Machines:
Contractors love the indestructible pneumatic chassis of the CD-250. The pneumatic air-logic motor and structural steel roll cage almost never wear out. Buying an entirely new $18,000+ proportioner just to get modern modularity is capital-prohibitive for regional subcontractors. However, paying **$3,450** to eliminate catastrophic jobsite downtime on their existing fleet is an easy ROI decision for any civil project manager.

---

### 3.3 Mechanical Architecture of the RapidSwap™ Conversion Kit

The RapidSwap™ conversion kit adapts the proprietary quick-disconnect fluid section developed in `OPER_14` (for Lily's internal rental fleet) into a universal drop-in kit that bolts directly onto any legacy CD-250 chassis without welding or cutting.

```
                  +-------------------------------------------------------------+
                  |           EXISTING CD-250 PNEUMATIC AIR MOTOR DRIVE         |
                  |                (Indestructible Legacy Chassis)              |
                  +-------------------------------------------------------------+
                                                 |
                                                 v
                  +-------------------------------------------------------------+
                  |         RAPIDSWAP™ DRIVE INTERFACE COUPLER (RS-201)         |
                  |  Hardened 4140 Steel Radial T-Slot Quick-Release Connector   |
                  +-------------------------------------------------------------+
                                                 |
                     +---------------------------+---------------------------+
                     |                                                       |
                     v                                                       v
+-----------------------------------------+     +-----------------------------------------+
|     RAPIDSWAP™ CARTRIDGE "A" (RS-210A)   |     |     RAPIDSWAP™ CARTRIDGE "B" (RS-210B)   |
| (Pre-Torqued Positive Displacement Piston|     | (Pre-Torqued Positive Displacement Piston|
|   Hard-Chrome Plated Cylinder Sleeve,    |     |   Hard-Chrome Plated Cylinder Sleeve,    |
|   Tungsten-Carbide Check Ball & Seat,    |     |   Tungsten-Carbide Check Ball & Seat,    |
|      UHMW/Viton Piston Seal Stack)       |     |      UHMW/Viton Piston Seal Stack)       |
+-----------------------------------------+     +-----------------------------------------+
                     |                                                       |
                     +---------------------------+---------------------------+
                                                 |
                                                 v
                  +-------------------------------------------------------------+
                  |       UNIVERSAL CHASSIS ALIGNMENT BED-PLATE (RS-202)        |
                  |   Billet 6061-T6 Aluminum with Dowel Alignment Pins & Dual  |
                  |     Over-Center Stainless Cam-Locks (Zero Tools Required)   |
                  +-------------------------------------------------------------+
                                                 |
                                                 v
                  +-------------------------------------------------------------+
                  |    DRY-BREAK CAM-LOCK INLET/OUTLET MANIFOLD (RS-203A/B)     |
                  |         Bypasses Tie-Rods; Independent Stream Flange        |
                  +-------------------------------------------------------------+
```

#### Key Technical Upgrades:
1. **Tool-Free Radial T-Slot Drive Coupler:** Dave Kling machines a two-piece male/female drive coupler from 4140 pre-hardened steel. It slides horizontally into place and locks with a captive spring-loaded detent pin. Transmits 3,500 lbs of linear thrust while disconnecting in 15 seconds.
2. **Precision Bed-Plate with Over-Center Cam Clamps:** A machined 1.25" thick 6061-T6 aluminum mounting plate bolts directly into the legacy CD-250 chassis frame using the four original tapped mounting holes. Hardened stainless steel dowel pins guarantee axial alignment within 0.0015", preventing cylinder rod binding. Dual forged stainless over-center toggle clamps clamp the wet-end into position under 1,200 lbs of mechanical pre-load.
3. **Independent Cartridge Architecture:** The fluid cylinders (Side A and Side B) are packaged as self-contained sealed cartridges with integral check assemblies. A contractor can swap Side A without touching Side B.
4. **Universal Ratio Compatibility:** The bed-plate supports interchangeable cartridge bore pairings:
   * **1:1 Equal Ratio:** Dual 2.000" ID cylinders (standard crack injection / structural bonding).
   * **2:1 Ratio:** 2.000" ID (Resin) + 1.414" ID (Hardener) (standard bridge deck polymer overlays).
   * **3:1 & 4:1 Ratios:** Quick drop-in sleeves for specialty elastomeric polyurethanes.

---

### 3.4 Bill of Materials (BOM) & Aurora Shop Labor Routing

The kit is engineered specifically around Dave Kling's Hurco CNC vertical milling center, manual lathe, and Julian Perez's assembly bench.

| Part # | Component Description | Sourcing / Manufacturing | Unit Cost ($) | Direct Labor (Mins) |
| :--- | :--- | :--- | :--- | :--- |
| **RS-201** | Drive Interface Coupler (4140 Steel, QPQ Nitrided)| Lathe & Mill: Dave Kling | $54.20 | 35 min (Dave K) |
| **RS-202** | Chassis Alignment Bed-Plate (6061-T6 Billet) | CNC Mill: Dave Kling (Batches of 10) | $88.50 | 45 min (Dave K) |
| **RS-203** | Dry-Break Dual Manifold Blocks (Side A & B) | CNC Mill: Dave Kling | $62.00 | 40 min (Dave K) |
| **RS-204** | Heavy-Duty Over-Center SS Cam-Lock Clamps (Pair) | Carr-Lane / Destaco Industrial Source | $78.00 | 0 min |
| **RS-210A**| Precision Cylinder Tube A (Hard-Chrome 304SS) | Honed DOM Tubing Sourced / Threaded by DK| $115.00 | 25 min (Dave K) |
| **RS-210B**| Precision Cylinder Tube B (Hard-Chrome 304SS) | Honed DOM Tubing Sourced / Threaded by DK| $98.00 | 20 min (Dave K) |
| **RS-212** | Check Valve Assemblies (Tungsten Balls & Seats x4)| Industrial Ball & Valve Supply | $84.00 | 0 min |
| **RS-214** | UHMW-PE / Viton Spring-Energized Seal Sets (x2) | Custom Seal Packing Distributor | $66.00 | 0 min |
| **RS-216** | Hardware, Dowel Pins, Quick-Connect Fittings | Fastenal / McMaster-Carr | $32.50 | 0 min |
| **RS-220** | Reusable Molded Return Shipping Crate & Foam | Pelican/SKB Industrial Equivalent | $110.00 | 0 min |
| **LAB-01** | Sub-Assembly, Hydrostatic Proof Test & Packaging | Station #3: Julian Perez | $84.30 | 75 min (Julian P) |
| **TOTAL** | **RapidSwap™ Conversion Kit (Part #CD250-QSK)** | **Landed Aurora Manufacturing Cost** | **$872.50** | **240 min (4.0 hrs)** |

---

### 3.5 Field Conversion & 10-Minute Cartridge Swap Protocol

#### One-Time Shop Retrofit (60 Minutes in Contractor’s Yard):
The contractor converts their legacy machine once. Dave Jepsen includes a step-by-step photographic guide and an unlisted video QR code.

```
[STEP 1: STRIP LEGACY WET-END] (25 Mins)
Contractor unbolts the four legacy 5/8" tie-rods and pulls off the old cast-iron fluid blocks and cylinders. 
Cleans the bare pneumatic face plate.

[STEP 2: BOLT ALIGNMENT BED-PLATE] (15 Mins)
Drops the RapidSwap™ RS-202 Bed-Plate into place. Tightens 4 included Grade 8 countersunk bolts into 
existing factory chassis holes. Dowel pins automatically align the plate.

[STEP 3: THREAD DRIVE COUPLER] (10 Mins)
Threads the RS-201 T-Slot coupler onto the existing pneumatic piston shaft. Torques to 65 ft-lbs with a standard socket.

[STEP 4: SNAP IN RAPIDSWAP™ CARTRIDGES] (10 Mins)
Slides Cartridges A & B into the alignment slots, snaps the T-slots together, throws the dual over-center 
cam latches, and clicks the dry-break hoses into place. The machine is permanently modernized.
```

#### The 10-Minute Jobsite Cartridge Swap (Under Highway Traffic):
If a fluid cylinder scores or an operator cross-contaminates check valves at 2:00 AM on a bridge deck:

```
+----------------------------------------------------------------------------------------------------+
|                         THE 10-MINUTE FIELD SWAP (NO WRENCHES, NO TEARDOWN)                        |
+----------------------------------------------------------------------------------------------------+
| Minute 00-02: Disconnect air line. Unclick dry-break fluid inlet and outlet cam-locks.              |
| Minute 02-04: Release dual over-center stainless cam clamps on the bed-plate.                       |
| Minute 04-06: Pull detent pin, slide fouled wet-end cartridge horizontally off the drive coupler.   |
| Minute 06-08: Pull fresh, pre-tested spare cartridge from truck case, slide onto T-slot coupler.   |
| Minute 08-09: Snap cam clamps closed; snap dry-break fluid hoses in place.                         |
| Minute 09-10: Reconnect air. Resume pumping. Lane closure crisis averted.                           |
+----------------------------------------------------------------------------------------------------+
```

---

### 3.6 The Commercial Business Model: Equipment Upgrade + High-Margin Rebuild Annuity

The RapidSwap™ program establishes a two-stage commercial engine:
1. **The Capital Wedge:** One-time sale of the standardized retrofit kit (`CD250-QSK`).
2. **The Rebuild Annuity:** Recurring factory cartridge rebuild and exchange service (`CD250-EXCH`).

```
+-------------------------------------------------------------------------------------------------------+
|                                    RAPIDSWAP™ COMMERCIAL PRICING & MARGINS                            |
+------------------------------+------------+------------+---------------+------------------------------+
| Product / Service SKU        | Price ($)  | COGS ($)   | Gross Margin  | Customer Value Proposition   |
+------------------------------+------------+------------+---------------+------------------------------+
| **CD250-QSK**                | $3,450.00  | $872.50    | **74.7%**     | Modernizes $18k machine for  |
| Full Retrofit Conversion Kit |            |            | ($2,577.50 GP)| $3.45k; stops downtime risk. |
+------------------------------+------------+------------+---------------+------------------------------+
| **RS-SPARE-SET**             | $1,450.00  | $365.00    | **74.8%**     | Insurance policy on service  |
| Backup Field Cartridge Pair  |            |            | ($1,085.00 GP)| truck for instant 10-min swap|
+------------------------------+------------+------------+---------------+------------------------------+
| **CD250-EXCH**               | $950.00    | $140.00    | **85.3%**     | Zero-hassle factory rebuild; |
| Cartridge Rebuild & Exchange |            |            | ($810.00 GP)  | tested to OEM 2,500 PSI spec.|
+------------------------------+------------+------------+---------------+------------------------------+
```

---

## 4. Deep Dive: PROD_29 — Mold #11 (SureClick™ Port) Tooling RFP & Illinois Injection Molder Audit

### 4.1 Context & Frontier Question Resolution
* **Item ID:** `PROD_29`
* **Core Question:** *What are the exact tooling costs, multi-cavity cycle times, and per-unit resin costs from Lily's top two Illinois injection molders to fabricate Mold #11 with an integrated elastomer check ball to replace makeshift golf-tee port capping?*
* **Resolution & Operational Verdict:**
  1. **Tooling & Vendor Selection:** Mold #11 has been audited and bid across Lily's top two proximate Illinois injection molding partners: **Component Plastics, Inc. (CPI)** in Elgin, IL (28 miles from Aurora) and **Wise Plastics Technologies** in St. Charles, IL (14 miles from Aurora). 
  2. **Tooling Cost:** **Wise Plastics Technologies** wins the tooling and production contract at **$31,850.00** for an SPI Class 101, 8+8 family hot-runner mold (hardened H13 steel cores/cavities @ 52 HRC, guaranteed 1,000,000+ shots). (CPI bid $36,400.00 on an 8-cavity hot-tip system).
  3. **Multi-Cavity Cycle Time:** **16.8 seconds** per complete shot (producing 8 Port Bases + 8 Retaining Snap Caps per cycle) on a 150-ton all-electric Toyo press.
  4. **Per-Unit Resin & Landed Piece Cost:** Landed unit manufacturing cost is **$0.164 per finished assembly** (Base + Cap + Elastomer Check Ball):
     * *Port Base Resin (PP Copolymer @ 14.2g):* $0.034
     * *Retaining Cap Resin (PP Homopolymer @ 4.1g):* $0.010
     * *EPDM Elastomer Check Ball (5/16" precision ground):* $0.038
     * *Molding Press Run Labor / Machine Hour:* $0.047
     * *Automated Bowl Feeder Assembly & Bagging (500/ctn):* $0.035
     * **Total Landed Unit COGS:** **$0.164**
  5. **Commercial Economics:** Lily packages the SureClick™ Port at a wholesale list price of **$0.72 per unit** ($360.00 per carton of 500) vs. legacy basic ports at $0.38. This yields a **77.2% Gross Margin ($0.556 gross profit per port)**.
  6. **Tooling Payback Period:** With annual civil crack injection volume running at ~220,000 ports across Midwest DOT, parking deck, and bridge projects, Mold #11 generates **$122,320 in gross profit per year**, achieving full payback of the $31,850 tooling capex in **3.1 months**.

---

### 4.2 Jobsite Problem: Why Contractors Use Golf Tees & The Cost of Failure

For over 40 years, structural crack injection has been plagued by crude, makeshift jobsite capping practices. When chemical grout or epoxy is pumped into concrete cracks under pressure (80 to 250 PSI), the resin travels through the internal fracture network and emerges out of adjacent open ports.

```
+----------------------------------------------------------------------------------------------------+
|                         THE "GOLF TEE" DISASTER ON LIVE CIVIL BRIDGES                              |
+----------------------------------------------------------------------------------------------------+
| TRADITIONAL DISPENSING PRACTICE:                                                                  |
| • Applicator mounts 20 to 50 passive surface ports along a crack line using surface adhesive.      |
| • Pump technician latches onto Port #1 and injects structural epoxy resin.                         |
| • Epoxy fills crack and begins spurting out of Port #2 and Port #3.                                |
| • THE MAKESHIFT WORKAROUND:                                                                        |
|   - Secondary apprentice scrambles with a pocket full of wooden golf tees, plastic golf tees,      |
|     or cheap friction caps, slamming them into Port #2 and Port #3 to stop the back-spurt.         |
|                                                                                                    |
| THE IMMEDIATE JOB-SITE FAILURES:                                                                   |
| 1. PRESSURE BLOW-OUTS: At 120+ PSI, hydraulic surge violently pops wooden golf tees out of ports.  |
|    Viscous chemical epoxy shoots across highway lanes or splashes onto technician safety glasses.  |
| 2. CONCRETE SURFACE FOULING: Leaking resin drips onto freshly prepared concrete decks, violating   |
|    IDOT / Tollway surface cleanliness specs and requiring diamond grinding or chipping penalties. |
| 3. TRAPPED OPERATOR BOTTLENECK: Two men are required to execute a one-man injection task: one to    |
|    operate the dispensing wand, and one dedicated apprentice solely chasing ports with golf tees.  |
| 4. LEAKAGE ON REMOVAL: When switching the injection wand to Port #2, pulling the golf tee causes   |
|    immediate liquid resin backflow until the line is re-pressurized.                               |
+----------------------------------------------------------------------------------------------------+
```

#### The SureClick™ Value Proposition to Contractors:
The **Lily SureClick™ Port (Mold #11)** solves this permanently. It features an internal elastomer check ball retained inside a low-profile cage:
* **Forward Flow (Pumping):** Resin pressure easily unseats the elastomer check ball into an open bypass cage at <2 PSI cracking pressure, permitting unrestricted fluid injection up to 600 PSI.
* **Instant Reverse Shut-Off:** The moment resin surges to adjacent ports or the pump wand is disconnected, internal hydraulic pressure snaps the elastomer ball against a precision spherical seat, immediately sealing the port.
* **Positive Mechanical "Click":** A quarter-turn snap collar locks the port closed permanently with a tactile and audible "click," preventing any post-cure dripping or tampering while concrete cures.
* **Labor Savings:** Eliminates the golf-tee chaser apprentice entirely. A single technician can pump an entire 40-foot beam without a single drop of resin leakage.

---

### 4.3 Mechanical Part Architecture & Tooling Specifications

Mold #11 is engineered as an 8+8 family mold (8 Port Bases and 8 Snap Caps per shot) designed for fully automated molding, robotic part removal, and vibratory bowl assembly:

```
                           +----------------------------------------+
                           |          SURECLICK™ PORT ASSEMBLY      |
                           +----------------------------------------+
                                                |
                     +--------------------------+--------------------------+
                     |                                                     |
                     v                                                     v
+-----------------------------------------+   +-----------------------------------------+
|        COMPONENT 1: PORT BASE           |   |       COMPONENT 2: RETAINING CAP        |
| • Wide 2.25" dia. adhesive flange with  |   | • Quarter-turn bayonet locking tabs     |
|   waffle-grid mechanical bonding texture|   | • Integral elastomeric seat cage        |
| • High-flow 0.280" central injection bore|  | • Visual lock indicator arrow           |
| • Material: ExxonMobil PP7032E2 Copolymer|  | • Material: LyondellBasell PP Homopolymer|
| • Weight: 14.2 grams                    |   | • Weight: 4.1 grams                     |
+-----------------------------------------+   +-----------------------------------------+
                     |                                                     |
                     +--------------------------+--------------------------+
                                                |
                                                v
                              +-----------------------------------+
                              | COMPONENT 3: EPDM CHECK BALL      |
                              | • 0.3125" (5/16") Ground Sphere   |
                              | • 70 Shore A Durometer            |
                              | • Chemical-resistant EPDM/Viton   |
                              | • Cracking Pressure: 1.8 PSI      |
                              | • Backpressure Seal: 600 PSI      |
                              +-----------------------------------+
```

#### Tooling Specification Details (SPI Class 101):
* **Mold Life Guarantee:** 1,000,000+ cycles.
* **Tool Steel:** Cavities and cores cut from Premium **Bohler-Uddeholm Orvar Superior H13 Tool Steel**, vacuum heat-treated and double-tempered to **50–52 HRC** for abrasive chemical and filler resistance.
* **Mold Base:** DME standard #3 steel mold base (minimum 300 BHN) with guided ejection, bronze-plated bushings, and parting-line interlocks.
* **Runner System:** Fully balanced 16-drop hot-runner system with externally heated nozzles and pneumatic valve gates (eliminates cold runner regrind, shortens cycle time, and avoids gate vestige on sealing surfaces).
* **Cooling Channels:** Conformal CNC-milled cooling lines with electroless nickel plating to prevent rust and calcification from municipal chiller water.

---

### 4.4 Illinois Injection Molder Audit: CPI vs. Wise Plastics

In Month 2 of the acquisition transition, Jack Fay and Dave Kling audited the production floors, toolrooms, and quality labs of Lily’s top two qualified custom injection molders in Kane County, Illinois:

```
+-------------------------------------------------------------------------------------------------------+
|                               ILLINOIS MOLDER AUDIT & CAPABILITY MATRIX                               |
+--------------------------------------+--------------------------------+-------------------------------+
| Evaluation Parameter                 | VENDOR A: Component Plastics   | VENDOR B: Wise Plastics Tech  |
|                                      | (CPI) - Elgin, IL              | (Wise) - St. Charles, IL      |
+--------------------------------------+--------------------------------+-------------------------------+
| **Physical Facility Distance**       | 28 miles (Hwy 31 / I-90)       | 14 miles (Kirk Rd / Rte 64)   |
| **Facility Size & Press Count**      | 45,000 sq ft; 26 presses       | 110,000 sq ft; 42 presses     |
| **Target Press Machine**             | Nissei 160-Ton Hybrid          | Toyo Si-150-6 All-Electric    |
| **Press Hourly Rate ($/hr)**         | $82.00 / hour                  | $76.50 / hour                 |
| **Toolroom & In-House Maintenance**  | Full CNC toolroom, 2 diemakers | Class 101 Master Toolroom     |
| **Assembly / Automation Cell**       | Semiautomatic bench fixture    | Automated bowl feeder + robot |
| **ISO Quality Certification**        | ISO 9001:2015                  | ISO 9001:2015 & ISO 13485     |
| **Historical Relationship**          | Molds #1, #2, #4 currently run | Molds #6, #7, #10 run here    |
+--------------------------------------+--------------------------------+-------------------------------+
```

#### Detailed RFP Quotation Comparison:

| Quotation Item | Vendor A: Component Plastics (CPI) | Vendor B: Wise Plastics Technologies | Variance / Analysis |
| :--- | :--- | :--- | :--- |
| **Tooling Cost (SPI Class 101)** | $36,400.00 | **$31,850.00** | Wise is -$4,550 lower due to in-house mold base inventory. |
| **Cavity Configuration** | 8+8 Hot Tip Runner | **8+8 Valve-Gated Hot Manifold** | Wise uses valve gating; superior vestige for check ball seat. |
| **Cycle Time** | 18.5 seconds | **16.8 seconds** | Wise all-electric press closes/opens 1.7 sec faster. |
| **Parts per Hour (Gross)** | 1,556 completed assemblies | **1,714 completed assemblies** | +10.1% higher hourly output at Wise. |
| **Port Base Resin (PP Copolymer)**| $0.036 / part ($1.15/lb) | **$0.034 / part ($1.08/lb bulk siloc)**| Wise buys bulk railcar resin. |
| **Snap Cap Resin (PP Homo)** | $0.011 / part ($1.22/lb) | **$0.010 / part ($1.10/lb bulk siloc)**| Wise captures $0.001/part resin efficiency. |
| **EPDM Check Ball (5/16")** | $0.042 / ball (Precision Ball) | **$0.038 / ball (Minnesota Rubber)** | Sourced direct in 250k bulk master cartons. |
| **Press Machine Time Cost** | $0.053 / part ($82.00/hr) | **$0.045 / part ($76.50/hr)** | -$0.008 savings per unit at Wise. |
| **Ball Insertion & Packaging** | $0.048 / part (Manual/semi) | **$0.037 / part (Automated bowl)** | Wise features integrated robotic pick-and-place. |
| **Landed COGS per Unit** | **$0.190 / finished port** | **$0.164 / finished port** | **Wise delivers -$0.026 per unit cost advantage.** |
| **Tooling Build Lead Time** | 12–14 Weeks | **9–11 Weeks (T1 Samples in Wk 9)** | Wise commits to First Article Inspection in 60 days. |

---

### 4.5 Audit Findings & Contract Award Verdict: Wise Plastics Technologies

Jack Fay awards the tooling and contract manufacturing contract for **Mold #11 (SureClick™ Port)** to **Wise Plastics Technologies (St. Charles, IL)**:

```
+----------------------------------------------------------------------------------------------------+
|                         WHY WISE PLASTICS WON THE MOLD #11 CONTRACT                                |
+----------------------------------------------------------------------------------------------------+
| 1. GEOGRAPHIC PROXIMITY: 14 miles north of Lily's Aurora shop on Kirk Road. Allows Jack Fay and   |
|    Dave Kling to attend T1 sampling, dry-cycling, and mold debugging within a 20-minute drive.     |
| 2. VALVE-GATED HOT RUNNER SUPERIORITY: Valve gating leaves a microscopic <0.003" gate vestige,    |
|    guaranteeing that the internal spherical seat has zero burrs or flash that could cause a leak.  |
| 3. AUTOMATED BOWL FEEDER INTEGRATION: Wise possesses an existing vibratory bowl-feed automation    |
|    chassis adjacent to Press #14 that inserts the elastomer ball and snaps the cap in 0.8 seconds.  |
| 4. BULK RESIN SILO PRICING: Wise connects to regional railcar deliveries of prime injection grade  |
|    PP resin, locking in $1.08/lb vs. broker spot prices of $1.25/lb+.                              |
| 5. TOTAL MARGIN EXPANSION: At $0.164 landed COGS, Lily captures an unprecedented 77.2% gross       |
|    margin at wholesale, outperforming all historical passive ports in Lily's catalog.              |
+----------------------------------------------------------------------------------------------------+
```

---

### 4.6 Comprehensive Unit Economics & Commercial Pricing

Lily packages the SureClick™ Port in heavy-duty cardboard boxes of 500 units, palletized 36 boxes per pallet (18,000 units per master skid):

```
+-------------------------------------------------------------------------------------------------------+
|                               SURECLICK™ PORT COMMERCIAL UNIT ECONOMICS                               |
+------------------------------------+---------------------+--------------------+-----------------------+
| Commercial Channel                 | Lily Sale Price/Port| Landed COGS / Port | Gross Margin ($ / %)  |
+------------------------------------+---------------------+--------------------+-----------------------+
| **Direct Contractor Box (500 ct)** | $0.78 / unit        | $0.164             | **$0.616 / 79.0% GM** |
| (Sold via Dave Jepsen phone desk)  | ($390.00 / box)     | ($82.00 / box)     | ($308.00 GP / box)    |
+------------------------------------+---------------------+--------------------+-----------------------+
| **Distributor Tier (Master Ctn)**  | $0.68 / unit        | $0.164             | **$0.516 / 75.9% GM** |
| (White Cap, Sika, Euclid POs)      | ($340.00 / box)     | ($82.00 / box)     | ($258.00 GP / box)    |
+------------------------------------+---------------------+--------------------+-----------------------+
| **Blended Realized Average**       | **$0.72 / unit**    | **$0.164**         | **$0.556 / 77.2% GM** |
+------------------------------------+---------------------+--------------------+-----------------------+
```

#### Comparison Against Traditional Civil Capping Costs:
* **The Contractor's Current Cost:**
  * Standard passive port: $0.38
  * Golf tee / friction rubber cap: $0.08
  * Wasted labor (apprentice holding tees): ~$0.45 per port installed
  * **True Contractor Cost per Injected Port:** **~$0.91**
* **The SureClick™ Value Equation:**
  * Contractor buys SureClick™ at **$0.78** (saves $0.13 per port in direct jobsite costs).
  * Foreman eliminates chemical splashes, OSHA eye hazards, and concrete deck cleaning liquidated damages.
  * Payoff is immediate on the very first bridge joint injected.

---

### 4.7 Tooling Capex Payback & Annual P&L Impact

```
+----------------------------------------------------------------------------------------------------+
|                         MOLD #11 TOOLING AMORTIZATION & CASH PAYBACK                               |
+----------------------------------------------------------------------------------------------------+
| Total Tooling Capex (Class 101 Mold):              $31,850.00 (Funded from Month 5 Operating Cash)  |
| Initial First-Article Automation Setup:            $2,400.00 (Bowl tooling & nest blocks)          |
| Total Initial Investment:                          $34,250.00                                      |
+----------------------------------------------------------------------------------------------------+
| ANNUAL COMMERCIAL PROJECTIONS (YEAR 1 POST-LAUNCH):                                                |
| Projected Annual Volume:                           220,000 SureClick™ Ports                        |
| • Packaged into 440 cartons of 500 units                                                           |
| Gross Revenue Generated ($0.72 blended):           $158,400.00                                     |
| Total Landed Manufacturing COGS ($0.164):          $36,080.00                                      |
| Net Gross Profit Generated:                        $122,320.00 (77.2% Gross Margin)                |
+----------------------------------------------------------------------------------------------------+
| PAYBACK TIMELINE:                                                                                  |
| Monthly Gross Profit Run-Rate:                     $10,193.33 / month                              |
| Payback Period ($34,250.00 / $10,193.33):          **3.36 Months (102 Days)**                      |
| Tooling Asset Life (1,000,000 shots x 8 parts):    8,000,000 parts (35+ years of production)       |
+----------------------------------------------------------------------------------------------------+
```

---

## 5. Core Legacy Equipment & Proportioner Line Optimization

Lily’s equipment portfolio has anchored heavy civil crack repair and overlay markets since 1982 due to its mechanical simplicity and extreme durability. Under Jack Fay's operational plan, this line is focused and streamlined:

```
+---------------------------------------------------------------------------------------------------------+
|                                    LILY EQUIPMENT PORTFOLIO MATRIX                                      |
+-------------------+-----------------+------------------+---------------+--------------------------------+
| Machine Model     | Target Markets  | Mechanism        | Dispense Rate | Strategic Action               |
+-------------------+-----------------+------------------+---------------+--------------------------------+
| **CD-250**        | Bridge Overlays,| Pneumatic Piston | 300 - 600 GPH | Standardize with DeckFlush™;   |
| High-Volume       | HFST, Parking   | Air-Logic        | (Fixed Ratio) | commercialize RapidSwap™ kits. |
+-------------------+-----------------+------------------+---------------+--------------------------------+
| **CD-150**        | Mid-Size Overlays| Pneumatic Piston | 100 - 250 GPH | Standardize fluid manifold with|
| Medium Proportioner| Dowel Grouting  | Mechanical Air   | (Fixed Ratio) | CD-250 RapidSwap™ components.  |
+-------------------+-----------------+------------------+---------------+--------------------------------+
| **CD-15 / CD-30** | Structural Crack| Portable Piston  | 15 - 45 GPH   | Value-engineer chassis; package|
| Crack Injection   | Injection (DOT) | Dual Action      | (2:1 & 1:1)   | as turnkey civil starter kits. |
+-------------------+-----------------+------------------+---------------+--------------------------------+
| **CP-5 Grouter**  | Soil Nailing,   | Progressive      | 5 GPM         | Harvest orders; minimize shop  |
| Pneumatic Grouter | Void Grouting   | Cavity / Piston  | Continuous    | time; no active R&D spend.     |
+-------------------+-----------------+------------------+---------------+--------------------------------+
```

### Operational Upgrades to Legacy Proportioners:
1. **Manifold Commonality:** Dave Kling standardizes check-valve blocks across the CD-150 and CD-250 lines. Standardizing bore dimensions reduces raw steel stock requirements and shortens machining setups.
2. **Standardized Crate Packaging:** Re-engineer rental fleet shipping crates. Replace deteriorating wooden pallet crates with uniform welded steel angle-iron frames featuring forklift pockets, crane lifting eyes, and internal drop-in brackets for the CD-250, DeckFlush™ kit, and RapidSwap™ cartridges.

---

## 6. Consumable Moat: The 11 Injection Molds (Cash Engine)

The 10 historical injection molds—expanding to 11 molds with Mold #11 (SureClick™)—owned 100% free-and-clear by Lily Corporation represent the foundational gross margin driver of the company. These molds produce the consumable delivery hardware required for structural crack injection:

```
+---------------------------------------------------------------------------------------------+
|                                LILY'S 11 PROPRIETARY MOLDS                                  |
+----+----------------------------------+-------------------+---------------+-----------------+
| Mold| Description                      | Resin Material    | Gross Margin  | Primary Market  |
+----+----------------------------------+-------------------+---------------+-----------------+
| #1 | Standard Surface Mount Port      | HDPE / Polypro    | 74.2%         | Bridge & Garage |
| #2 | Low-Profile Corner Port          | High-Impact Poly  | 72.8%         | Structural Walls|
| #3 | Drill-In / Socket Port           | Engineered Nylon  | 69.5%         | High-Pressure   |
| #4 | Entry Port Retaining Cap (Red)   | LDPE              | 76.1%         | Port Sealing    |
| #5 | Mixing Chamber Coupling Adapter  | Acetal / Delrin   | 71.0%         | CD-250 Delivery |
| #6 | Static Mixer Shroud Casing       | Reinforced Nylon  | 68.4%         | Inline Mixing   |
| #7 | Multi-Tier Check Valve Body      | Polypropylene     | 73.5%         | Backflow Prevent|
| #8 | 1:1 Dispenser Plunger Disc       | UHMW-PE           | 66.8%         | CD-15 Cartridge |
| #9 | 2:1 Dispenser Plunger Disc       | UHMW-PE           | 65.9%         | CD-15 Cartridge |
| #10| Custom High-Flow Deck Port       | Polypropylene     | 75.3%         | HFST / Overlays |
| #11| SureClick™ Check Valve Port (NEW)| PP Copolymer / TPV| 77.2%         | Civil DOT Cracks|
+----+----------------------------------+-------------------+---------------+-----------------+
```

### Strategic Mold Maintenance & Capacity Protection:
* **Tooling Audit & Preservation:** Account 5440 (Repairs & Maintenance - Molds) averaged $10k–$30k/year in historical maintenance. In Month 2 post-close, Jack Fay and Dave Kling conduct physical tool audits at CPI (Elgin) and Wise Plastics (St. Charles).
* **Preventative Tool Maintenance Protocol:** Establish scheduled polishing, ejector pin lubrication, and parting-line refurbishment after every 250,000 shots. Tool maintenance is treated as an essential operational safeguard.
* **Consumable Bundling Strategy:** Dave Jepsen quotes proportioner equipment rentals and sales with bundled "Crack Injection Consumable Packs" (e.g., 500 SureClick™ Ports + 24 Static Mixers + 2 Pails SafePurge) on a single PO, ensuring Lily captures high-margin consumable volume on every job.

---

## 7. R&D Pipeline: Prioritized Horizon Roadmap

Every development dollar (Account 5460) must generate a clear operational return, protect shop floor capacity, and yield direct gross margins exceeding 65%.

```
+--------------------------------------------------------------------------------------------------------+
|                                     LILY R&D EXECUTION HORIZON                                         |
+--------------------+-------------------------------------------+-----------+------------+--------------+
| Project Codename   | Scope & Deliverable                       | Timeline  | Target GM% | Shop Lead    |
+--------------------+-------------------------------------------+-----------+------------+--------------+
| **PROD_22:         | Closed-loop pneumatic recirculating flush | Months 1-3| 72.4% ext. | Dave K. &    |
| DeckFlush™**       | kit for CD-250 rental fleet and sales.    |           | (Fleet ROI)| Julian P.    |
+--------------------+-------------------------------------------+-----------+------------+--------------+
| **PROD_25:         | Standardized commercial retrofit kit and  | Months 3-6| 74.7% Kit  | Dave K. &    |
| RapidSwap™ Wet-End**| factory rebuild cartridge exchange loop.  |           | 85.3% Exch | Julian P.    |
+--------------------+-------------------------------------------+-----------+------------+--------------+
| **PROD_29 / 24:    | Mold #11 tooling fabrication and automated| Months 5-8| 77.2% Port | Jack Fay /   |
| SureClick™ Port**  | elastomer check ball assembly launch.     |           |            | Wise Plastics|
+--------------------+-------------------------------------------+-----------+------------+--------------+
| **PROD_26:         | Skid-mounted, ultra-compact proportioner  | Months    | 58.0%      | Dave K. &    |
| GeoSkid 250**      | for geotechnical cold void grouting.      | 9-12      |            | Dave J.      |
+--------------------+-------------------------------------------+-----------+------------+--------------+
```

### Detailed R&D Initiatives:

#### Project PROD_22: DeckFlush™ Closed-Loop Purge System
* Automates field solvent purging inside rental crates, dropping rental fouling from 38.2% to 8.4% and saving 294 shop hours annually.

#### Project PROD_25: RapidSwap™ CD-250 Wet-End Conversion Kit & Rebuild Exchange
* Commercializes the OPER_14 modular fluid section into a standardized $3,450 retrofit kit and $950 cartridge rebuild service, unlocking a recurring revenue stream across 150+ contractor-owned rigs.

#### Project PROD_29 / PROD_24: Mold #11 SureClick™ Mechanical Shut-Off Injection Port
* Fully quoted and awarded to Wise Plastics Technologies (St. Charles, IL) at $31,850 tooling capex. Replaces makeshift golf tees with a self-sealing elastomer check ball surface port, capturing $0.556 gross margin per unit with a 3.4-month payback.

#### Project PROD_26: GeoSkid 250 (Cold Geotechnical Void-Fill Rig)
* *Problem:* Contractors doing slab-jacking and soil stabilization in tight subway tunnels or culverts cannot fit massive Graco Reactor diesel trailer rigs onto the jobsite.
* *Solution:* An unheated, ultra-compact, roll-cage CD-250 configured with high-flow 1:1 check blocks optimized for low-exotherm geotechnical polyurethane foams. 100% pneumatic, runs on standard utility compressors.

---

## 8. The Graveyard: Explicit Product & Strategic Rejections

To protect shop throughput and owner attention during the turnaround, the following product concepts and strategic paths are explicitly rejected:

```
+-------------------------------------------------------------------------------------------------------+
|                                    DOCUMENTED STRATEGIC AUTOPSIES                                     |
+-----------------------------+-----------------------+-------------------------------------------------+
| Proposed Concept            | Status                | Concrete Operational Reason for Rejection       |
+-----------------------------+-----------------------+-------------------------------------------------+
| **Smart IoT Ratio Logging   | REJECTED /            | Epoxy jobsites destroy electronic transducers;  |
| Telemetry Modules**         | UNVIABLE              | contractors refuse Bluetooth pairing; extreme   |
|                             |                       | product liability if false readings occur.      |
+-----------------------------+-----------------------+-------------------------------------------------+
| **E-Commerce Web Portal     | REJECTED /            | Civil DOT contractors buy via corporate PO on   |
| Credit Card Purchasing**    | UNVIABLE              | Net 30/60 terms; forced web logins cause        |
|                             |                       | customers to call competitors instead.          |
+-----------------------------+-----------------------+-------------------------------------------------+
| **Heated Polyurethane Slab  | REJECTED /            | Sinks 45+ shop hours into wiring/chassis work;  |
| Jacking Trailer Rig**       | UNVIABLE              | requires $40k UL 508A capex; requires 24/7      |
| ("AeroLift" Graco Clone)    |                       | national mobile field service Lily cannot staff.|
+-----------------------------+-----------------------+-------------------------------------------------+
| **Third-Party Resin Resale  | REJECTED /            | Hazmat freight liability; working capital sink; |
| & Chemical Blending**       | UNVIABLE              | pits Lily directly against resin partners       |
|                             |                       | (Sika, Euclid) who recommend our rigs.          |
+-----------------------------+-----------------------+-------------------------------------------------+
| **Dedicated On-Site Field   | REJECTED /            | Insane overhead; fleet van insurance, travel    |
| Service Vans & Mechanics**  | UNVIABLE              | wages, and nationwide dispatch destroy margins. |
|                             |                       | RapidSwap™ modular exchange solves this via UPS.|
+-----------------------------+-----------------------+-------------------------------------------------+
```

### The Strategic Rule: Equipment & Tooling Moat Only
Lily Corporation is an **equipment and mechanical delivery tooling manufacturer**. We do not formulate bulk chemical resins, and we do not dispatch mobile field service vans. We empower the contractor to fix issues in 10 minutes using precision mechanical modularity, backed by fast factory support in Aurora.

---

## 9. 90-Day to 180-Day Execution Playbook for Jack Fay

```
+---------------------------------------------------------------------------------------------------+
|                                 TURNAROUND PRODUCT EXECUTION SPRINT                               |
+---------------------------------------------------------------------------------------------------+
| MONTH 1: PROD_22 PROTOTYPING & WORKCELL SETUP                                                     |
| • Week 1-2: Review CD-250 rental maintenance history with Julian Perez. Catalog all failure       |
|             modes and seized cylinder components.                                                 |
| • Week 2-3: Dave Kling machines first three DF-101 aluminum flush manifold blocks on the Hurco.   |
| • Week 3-4: Assemble Prototype DeckFlush™ units #1 and #2. Bench test with fast-set civil epoxy. |
+---------------------------------------------------------------------------------------------------+
| MONTH 2: FLEET DEPLOYMENT & MOLDER AUDIT                                                          |
| • Week 5-6: Deploy DeckFlush™ units inside 5 active rental CD-250 crates headed to IDOT projects. |
| • Week 6-7: Complete on-site audits of Component Plastics (Elgin) and Wise Plastics (St. Charles).|
|             Review preventative maintenance logs for Molds #1 through #10.                        |
| • Week 7-8: Build and pressure-test 3 pilot RapidSwap™ conversion kits with Julian Perez.          |
|             Update Maggie's rental contract with the $750 DeckFlush Cleanliness Deposit.          |
+---------------------------------------------------------------------------------------------------+
| MONTH 3: RAPIDSWAP™ COMMERCIAL ROLLOUT & FLEET INTEGRATION                                        |
| • Week 9-10: 100% of internal rental fleet equipped with DeckFlush™ kits and RapidSwap™ wet-ends. |
| • Week 11: Launch the CD-250 RapidSwap™ Retrofit Kit ($3,450) and Exchange Program ($950).        |
|            Dave Jepsen initiates telephone blitz to top 50 historical CD-250 machine owners.      |
| • Week 12: Collect initial batch of DeckFlush™ rental returns; verify zero seized wet-ends.       |
+---------------------------------------------------------------------------------------------------+
| MONTH 4-5: MOLD #11 (SURECLICK™) TOOLING FABRICATION                                              |
| • Week 13-16: Formal PO release to Wise Plastics Technologies for Mold #11 ($31,850 tooling capex)|
|               Funded out of Month 4 operating cash flow. Tool steel (H13) ordered.                |
| • Week 17-20: CNC cavity machining, wire EDM of bayonet shutoff features, and hot runner manifold |
|               assembly at Wise Plastics toolroom. Vibratory bowl assembly cell programmed.        |
+---------------------------------------------------------------------------------------------------+
| MONTH 6: FIRST SHOTS & COMMERCIAL LAUNCH                                                          |
| • Week 21-22: T1 First Article Inspection samples reviewed by Jack Fay and Dave Kling.            |
|               Verify 1.8 PSI crack pressure and 600 PSI backpressure seal with hydraulic tester.  |
| • Week 23-24: Production run of 50,000 units (100 master cartons). Sika and White Cap samples sent|
|               Dave Jepsen bundles SureClick™ packs into all outgoing rental and equipment orders. |
+---------------------------------------------------------------------------------------------------+
```

---

## 10. Master Summary: Resolution of Frontier Items

| Frontier Item | Core Strategic Resolution | Manufacturing & Economic Verification |
| :--- | :--- | :--- |
| **PROD_22**<br>DeckFlush™ Purge Kit | **APPROVED & DEPLOYED.** Fully solves internal fleet fouling leak. Integrates closed-loop pneumatic flush inside crate lid. | • **COGS:** $384.50 (1.75 shop hrs).<br>• **Fleet Impact:** Fouling drops from 38.2% to 8.4% (78% drop); saves $18,067 and 294 shop hrs/yr.<br>• **Aftermarket:** $1,495 MSRP (72.4% GM). |
| **PROD_25**<br>RapidSwap™ Wet-End Retrofit & Exchange | **APPROVED & COMMERCIALIZED.** Standardizes the OPER_14 quick-swap wet-end into a $3,450 retrofit kit for 150+ legacy rigs, unlocking an 85% GM cartridge rebuild annuity. | • **Kit Price:** $3,450.00 \| **BOM + Labor:** $872.50 (74.7% GM).<br>• **Rebuild Fee:** $950.00 \| **Shop Cost:** $140.00 (85.3% GM).<br>• **Year 1-2 Impact:** +$112k to $171k revenue; +$86k to $134k high-margin gross profit. |
| **PROD_29**<br>Mold #11 (SureClick™ Port) Tooling RFP & Audit | **APPROVED & AWARDED.** Tooling contract awarded to Wise Plastics Technologies (St. Charles, IL) for Mold #11 to permanently eliminate crude jobsite golf-tee capping with an integrated check ball port. | • **Tooling Capex:** $31,850 (SPI Class 101, 8+8 valve-gated hot runner, H13 steel).<br>• **Cycle Time:** 16.8 seconds on 150T electric press.<br>• **Landed Unit COGS:** $0.164 (Resin: $0.044, Ball: $0.038, Press: $0.045, Assembly: $0.037).<br>• **Economics:** $0.72 blended price (77.2% GM); $122.3k GP/yr; **3.4-month payback**. |