# 02. Product Lines & R&D Pipeline Architecture

**Target Company:** Lily Corporation (Aurora, IL)  
**Author:** Jack Fay, Turnaround Operator & Chief Product Officer  
**Baseline Financials:** ~$1.90M Normalized Sales | ~55% Blended Gross Margin | Consumable Gross Margin: 68%–85% | Rental Income: ~$130k–$300k/yr  
**Core Moat:** 10 Proprietary In-House Injection Molds (100% Owned Free and Clear), On-Site Cincinnati Milacron Injection Press & Desiccant Pellet Dryer in Aurora, Pneumatic Proportioning Technology (CD-250, CD-150, CD-15, CP-5), Universal Competitor-Compatible Port Geometry, High-Margin Consumable Pull-Through Engine, and Dedicated Shop Assembly Cells  
**Retained Shop Roster:**  
* **Robert "Bob" Trout:** Founder/Retiring President (44 years of customer trust, proprietary proportioner design, and custom quoting math; 6-month transition)  
* **Dave Jepsen:** Contractor Sales Engineer & Technical Application Support (~2 years at Lily; incoming contractor phone orders, application sizing, training seminars, and distributor account interface)  
* **Dave Kling:** Lead Fabricator, Machinist, Welder, Purchasing Agent, and Equipment Repairs (Shop Lathe, Hurco VMC, chassis welding, and warranty teardown)  
* **Julian Perez:** Assembly Technician, Repairs & Logistics Specialist (CD-15/LPI assembly, fluid whip crimping, calibration bench testing, master carton packaging, and LTL shipping)  
* **Greg:** Injection Molding Press Operator & QA/Hydrostatic Testing Lead (Sole press operator, Cincinnati Milacron setup, barrel heat zones, mold mounting, and high-pressure burst testing)  
* **Maggie M:** Office Manager & Bookkeeper (QuickBooks Desktop order entry, billing, Net 30/60 contractor PO intake, distributor invoicing, and compliance tracking)  

---

## 1. Executive Summary & Product Architecture

Lily Corporation’s commercial moat rests on an industrial "razor and razor blade" model: heavy-duty, pneumatically operated positive-displacement chemical proportioning dispensers (the capital wedge and rental anchor) drive recurring contractor demand for proprietary single-use injection-molded surface ports, snappy-tees, port caps, static mixers, and engineered delivery accessories (the high-margin consumable cash cow).

Under this turnaround architecture, Lily aggressively mobilizes its existing fleet of **10 proprietary injection molds**—owned 100% free and clear—to dominate the national consumable accessory market. By standardizing universal port geometries compatible with competitor dispensers (Graco, ChemCo Systems, ChemGrout, SealBoss) and packaging consumables into **250-pack and 1,000-pack contractor master cartons** for commercial concrete distribution placement (White Cap, Sika, Euclid), Lily captures an immediate, zero-capex, high-volume recurring gross profit stream.

```
                      +---------------------------------------------------+
                      |            LILY CORPORATION REVENUE MOAT          |
                      +---------------------------------------------------+
                                                |
             +----------------------------------+----------------------------------+
             |                                                                     |
+----------------------------+                                       +----------------------------+
|     EQUIPMENT & FLEET      |                                       |    CONSUMABLES & TOOLING   |
|   (Capital & Rental Anchor)|                                       |   (High-Margin Cash Cow)   |
+----------------------------+                                       +----------------------------+
| • CD-250 High-Volume (600 GPH)                                      | • 10 Proprietary Molds (Aurora Press)
| • CD-250 GeoMaster (720 GPH)                                        | • Universal Surface Ports (78-85% GM)
| • CD-150 Medium Overlay                                             | • Bulk Master Cartons (250 / 1,000)
| • CD-15 / CD-30 Crack Injection                                     | • Snappy-Tee Couplers (74-80% GM)
| • CP-5 Pneumatic Grouter                                            | • Entry Port Caps (76-82% GM)
| • Active Rental Fleet (~25 units)                                   | • SafePurge-250™ Fluid (75-80% GM)
| • DuraBore-2M™ Manifolds (>2.5M Cyc)                                | • IsoGuard-500™ Fluid (73-75% GM)
| • DuraBore-10M™ 17-4 PH Cores (>10M Cyc)                            | • Static Mixers & Delivery Lines
| • FilterPass-250™ De-Grit Systems                                   | • Omni-Flex™ Whip Hoses (68-75% GM)
|                                                                     | • DrySpear-250™ Consumables (78-82% GM)
|                                                                     | • RatioSentinel™ Tooling (73-77% GM)
|                                                                     | • RatioSentinel Recert (86.9% GM)
|                                                                     | • CleanPass-Seq™ Sequencer (76-81% GM)
|                                                                     | • GeoWhip-Bal™ Wand (75% GM)
|                                                                     | • AeroShift™ Drop-In Cartridges (79-87% GM)
|                                                                     | • FilterPass-250™ Baskets (75-80% GM)
|                                                                     | • SureMix-Geo™ Mixers (80.1% GM)
|                                                                     | • MultiLift-4™ Manifolds (77.1% GM)
+----------------------------+                                       +----------------------------+
             |                                                                     |
             +----------------------------------+----------------------------------+
                                                |
             +----------------------------------+----------------------------------+
             |                                  |                                  |
+----------------------------+    +----------------------------+    +----------------------------+
|  CYCLE #01 CORE EXPANSION: |    |   CYCLE #10 INNOVATION:    |    |   CYCLE #12 INNOVATION:    |
|  PROD_UNIVERSAL_PORTS_02:  |    |  PROD_22: CLOSED-LOOP PURGE|    |  PROD_25: QUICK-SWAP WET   |
|  UNIVERSAL BULK CARTONS    |    |  (Fleet Defense & Purge)   |    |  END RETROFIT & EXCHANGE   |
|  (250 & 1,000 Master Packs)|    |                            |    |                            |
+----------------------------+    +----------------------------+    +----------------------------+
             |                                  |                                  |
             v                                  v                                  v
+----------------------------+    +----------------------------+    +----------------------------+
|    CYCLE #16 INNOVATION:   |    |   CYCLE #22 INNOVATION:    |    |    CYCLE #24 INNOVATION:   |
|  PROD_32: COLD-WEATHER     |    |  PROD_44: OMNILATCH™       |    |  PROD_48: MODULAR FLUID    |
|  FULL-PORT COUPLER SPEC    |    |  UNIVERSAL WAND INTERFACE  |    |  CYCLE-COUNTER & SHROUD    |
+----------------------------+    +----------------------------+    +----------------------------+
             |                                  |                                  |
             +----------------------------------+----------------------------------+
                                                |
             +----------------------------------+----------------------------------+
             |                                  |                                  |
             v                                  v                                  v
+----------------------------+    +----------------------------+    +----------------------------+
|    CYCLE #28 INNOVATION:   |    |    CYCLE #32 INNOVATION:   |    |    CYCLE #34 INNOVATION:   |
|  PROD_56: RATIO-LOCK™      |    |  PROD_62: GEOCONVERSION   |    |  PROD_68: AIR-LOGIC SPOOL  |
|  MECHANICAL INTERLOCK      |    |  SPOOL & LINKAGE (1:1/5:1) |    |  & PILOT MODULAR CARTRIDGE |
+----------------------------+    +----------------------------+    +----------------------------+
             |                                  |                                  |
             +----------------------------------+----------------------------------+
                                                |
             +----------------------------------+----------------------------------+
             |                                  |                                  |
             v                                  v                                  v
+----------------------------+    +----------------------------+    +----------------------------+
|    CYCLE #36 INNOVATION:   |    |    CYCLE #42 INNOVATION:   |    |    CYCLE #45 INNOVATION:   |
|  PROD_74: MOLD #6 RETOOL   |    |  PROD_86: RAPID-GRIP™     |    |  PROD_92: DEEPDRIVE-15™    |
|  (Low-Drop Bayonet Mixer)  |    |  GEOTECHNICAL PACKERS      |    |  LANCE & DRIVE-TIP SYSTEM  |
+----------------------------+    +----------------------------+    +----------------------------+
             |                                  |                                  |
             +----------------------------------+----------------------------------+
                                                |
             +----------------------------------+----------------------------------+
             |                                  |                                  |
             v                                  v                                  v
+----------------------------+    +----------------------------+    +----------------------------+
|    CYCLE #46 INNOVATION:   |    |    CYCLE #51 INNOVATION:   |    |    CYCLE #52 INNOVATION:   |
|  PROD_94: AERO-SHIFT™      |    |  PROD_103: CLEANPASS-250™  |    |  PROD_104: SAFEPURGE-250™  |
|  SUB-ZERO DE-ICING MUFFLER |    |  SNAP-ON BYPASS FLUSH CAP  |    |  CLOSED-LOOP BIO-SOLVENT   |
+----------------------------+    +----------------------------+    +----------------------------+
             |                                  |                                  |
             +----------------------------------+----------------------------------+
                                                |
             +----------------------------------+----------------------------------+
             |                                  |                                  |
             v                                  v                                  v
+----------------------------+    +----------------------------+    +----------------------------+
|    CYCLE #54 INNOVATION:   |    |    CYCLE #58 INNOVATION:   |    |    CYCLE #60 INNOVATION:   |
|  PROD_108: RATIOSHIFT-15™  |    |  PROD_118: OMNI-FLEX™      |    |  PROD_120: DRYSPEAR-250™   |
|  MODULAR RATIO SLEEVES     |    |  MICRO-BORE WHIP CELL      |    |  DESICCANT SPEAR MANIFOLD  |
+----------------------------+    +----------------------------+    +----------------------------+
             |                                  |                                  |
             +----------------------------------+----------------------------------+
                                                |
             +----------------------------------+----------------------------------+
             |                                  |                                  |
             v                                  v                                  v
+----------------------------+    +----------------------------+    +----------------------------+
|    CYCLE #62 INNOVATION:   |    |    CYCLE #64 INNOVATION:   |    |    CYCLE #65 INNOVATION:   |
|  PROD_124: RATIOSENTINEL™  |    |  PROD_128: CLEANPASS-SEQ™  |    |  PROD_130: GEOWHIP-BAL™    |
|  DUAL-BURET RATIO MANIFOLD |    |  ANTI-CROSSOVER PURGER     |    |  AUTO-BALANCING GEO-WAND   |
+----------------------------+    +----------------------------+    +----------------------------+
             |                                  |                                  |
             +----------------------------------+----------------------------------+
                                                |
             +----------------------------------+----------------------------------+
             |                                  |                                  |
             v                                  v                                  v
+----------------------------+    +----------------------------+    +----------------------------+
|    CYCLE #66 INNOVATION:   |    |    CYCLE #67 INNOVATION:   |    |    CYCLE #68 INNOVATION:   |
|  PROD_132: AEROSHIFT™ DROP-|    |  PROD_134: DURABORE-2M™    |    |  PROD_136: DURABORE-10M™   |
|  IN FIELD REBUILD CARTRIDGE|    |  AUTOFRETTAGED MANIFOLDS   |    |  17-4 PH BILLET UPGRADE    |
+----------------------------+    +----------------------------+    +----------------------------+
             |                                  |                                  |
             +----------------------------------+----------------------------------+
                                                |
             +----------------------------------+----------------------------------+
             |                                  |                                  |
             v                                  v                                  v
+----------------------------+    +----------------------------+    +----------------------------+
|    CYCLE #73 INNOVATION:   |    |    CYCLE #75 INNOVATION:   |    |    CYCLE #82 INNOVATION:   |
|  PROD_146: ISOGUARD-500™   |    |  PROD_150: FILTERPASS-250™ |    |  PROD_164: SUREMIX-GEO™    |
|  ANHYDROUS STORAGE FLUID   |    |  DUAL-STREAM DE-GRIT BLOCK |    |  NON-CLOG BLOWBACK MIXER   |
+----------------------------+    +----------------------------+    +----------------------------+
             |                                  |                                  |
             +----------------------------------+----------------------------------+
                                                |
             +----------------------------------+----------------------------------+
             |                                  |                                  |
             v                                  v                                  v
+----------------------------+    +----------------------------+    +----------------------------+
|    CYCLE #83 INNOVATION:   |    |    CYCLE #86 INNOVATION:   |    |    CYCLE #88 DISCIPLINE:   |
|  PROD_166: MULTILIFT-4™    |    |  PROD_172: RATIOSENTINEL™  |    |  CAPEX DISCIPLINE ENFORCED |
|  BALANCED GEO-MANIFOLD     |    |  ANNUAL RECERTIFICATION RIG|    |  (MOLDS 11-13 FROZEN IN Y1)|
+----------------------------+    +----------------------------+    +----------------------------+
```

### Margin Realities by Product Line
1. **Molded Consumables & Universal Bulk Packaging (Accounts 4010 / 5120):**
   * *Gross Margin:* 72% to 89% direct contractor; 78% to 83% commercial distributor wholesale.
   * *Dynamics:* Zero moving parts. Molded 100% on-site at 240 S. Broadway in Aurora by Greg on the Cincinnati Milacron press. Zero external toll-molding markups. Packed into 250-pack and 1,000-pack heavy-duty master cartons by Julian Perez. Sold via Net 30/60 purchase orders, Dave Jepsen's phone desk, and commercial stocking distributors (White Cap, Sika, Euclid).
   * *Consumable Expansion Anchor:*
     * **PROD_UNIVERSAL_PORTS_02 (Universal Surface Ports & Master Cartons):** Unlocks immediate national distribution placement by packaging Lily's Mold #1 standard surface ports, Mold #2 corner ports, and Mold #4 caps into standardized 250-pack (`LPP-250`) and 1,000-pack (`LPP-1000`) master cartons. Compatible with Graco, ChemCo, ChemGrout, and SealBoss dispensers. Generates **81.6% to 82.6% gross margin at wholesale** ($0.348–$0.396/port) against an in-house landed Aurora COGS of **$0.064–$0.069 per port**. Zero tooling capex required.
2. **Proprietary Proportioners (CD-250, CD-150, CD-15):**
   * *Gross Margin (Unit Sales):* 48% to 54% baseline (expanding to 72%–77% on specialized modular packages).
   * *Dynamics:* Pneumatic air-logic driven, positive piston displacement, explosion-proof. Assembled, machined, and hydrostatically tested in Aurora by Dave Kling and Julian Perez.
3. **Rental Fleet & Maintenance Overhaul (Accounts 4015 / 4011):**
   * *Gross Margin (Rental Income):* 72% to 81% gross on asset depreciation.
   * *Dynamics:* Preserved through closed-loop purge kits (`PROD_22`), de-grit screen blocks (`PROD_150`), and storage conditioning fluids (`PROD_146`).

---

## 2. Deep Dive: PROD_22 — Closed-Loop Chemical Purge & Anti-Fouling Kit
*(Retained from Baseline Architecture)*

---

## 3. Deep Dive: PROD_25 — Commercial CD-250 Quick-Swap Wet-End Conversion Kits & Rebuild Annuity
*(Retained from Baseline Architecture)*

---

## 4. Deep Dive: PROD_32 — Cold-Weather High-Viscosity Flow Dynamics on Couplers
*(Retained from Baseline Architecture)*

---

## 5. Deep Dive: PROD_29 — Mold #11 (SureClick™ Flat Port) Tooling RFP & Illinois Molder Audit
*(Retained from Baseline Architecture - Note: Tooling Capex Frozen in Year 1 per Capital Discipline)*

---

## 6. Deep Dive: PROD_38 — Mold #12 (SureClick™ Corner & Inverted Overhead Check Port Extension)
*(Retained from Baseline Architecture - Note: Tooling Capex Frozen in Year 1 per Capital Discipline)*

---

## 7. Deep Dive: PROD_44 — SureClick™ OmniLatch™ Universal Wand Interface
*(Retained from Baseline Architecture)*

---

## 8. Deep Dive: PROD_48 — CD-250 Modular Fluid Section Smart Cycle-Counter & Telemetry Shroud
*(Retained from Baseline Architecture)*

---

## 9. Deep Dive: PROD_56 — Ratio-Lock™ Pneumatic Mechanical Differential Ratio-Interlock Block
*(Retained from Baseline Architecture)*

---

## 10. Deep Dive: PROD_62 — Low-Pressure Polyurethane Geotechnical Conversion Spool & Linkage Kit for CD-250
*(Retained from Baseline Architecture)*

---

## 11. Deep Dive: PROD_68 — Air-Logic Spool & Pilot Valve Modular Exchange Cartridge Program
*(Retained from Baseline Architecture)*

---

## 12. Deep Dive: PROD_94 — AeroShift™ FrostGuard™ Sub-Zero De-Icing & Thermal-Recovery Muffler System
*(Retained from Baseline Architecture)*

---

## 13. Deep Dive: PROD_103 — CleanPass-250™ Rapid Jobsite End-of-Shift Flush Manifold & Recirculation Bypass Cap
*(Retained from Baseline Architecture)*

---

## 14. Deep Dive: PROD_104 — SafePurge-250™ Closed-Loop Bio-Citrus Flushing Fluid Formulation & Private-Label Program
*(Retained from Baseline Architecture)*

---

## 15. Deep Dive: PROD_74 — Low-Restriction Bayonet Static Mixer & Shroud Integration (Mold #6 Retooling)
*(Retained from Baseline Architecture)*

---

## 16. Deep Dive: PROD_86 — Proprietary Rapid-Grip™ Geotechnical Mechanical Packer & Pull-Through Margin Strategy
*(Retained from Baseline Architecture - Note: Tooling Capex Frozen in Year 1 per Capital Discipline)*

---

## 17. Deep Dive: PROD_92 — Subgrade Deep-Injection Extension Lance & Sacrificial Knock-Off Tip System (`DeepDrive-15™`)
*(Retained from Baseline Architecture)*

---

## 18. Deep Dive: PROD_108 — CD-15 RatioShift™ Modular Quick-Change Metering Ratio Sleeve Kit (1:1, 2:1, 3:1)
*(Retained from Baseline Architecture)*

---

## 19. Deep Dive: PROD_118 — Turnkey High-Pressure Omni-Flex™ Whip Hose Assembly Workcell & Micro-Bore Swell-Defense Program
*(Retained from Baseline Architecture)*

---

## 20. Deep Dive: PROD_120 — DrySpear-250™ Moisture-Sealed Desiccant Drum Bung Spear & Transfer Manifold Kit
*(Retained from Baseline Architecture)*

---

## 21. Deep Dive: PROD_124 — Jobsite Ratio Sentinel: Mechanical Dual-Buret Volumetric Ratio Verification Test Manifold
*(Retained from Baseline Architecture)*

---

## 22. Deep Dive: PROD_128 — Dual-Stream Geotechnical Fast-Reacting Polyurethane Anti-Crossover Purge Sequencer (`CleanPass-Seq™`)
*(Retained from Baseline Architecture)*

---

## 23. Deep Dive: PROD_130 — Dual-Feed Equal-Pressure Auto-Balancing Handheld Geotechnical Dispensing Wand (`GeoWhip-Bal™`)
*(Retained from Baseline Architecture)*

---

## 24. Deep Dive: PROD_132 — AeroShift™ Modular Directional Air Logic Valve Drop-In Field Cartridge
*(Retained from Baseline Architecture)*

---

## 25. Deep Dive: PROD_134 — Autofrettaged Internal Fluid Gallery Cross-Bore Treatment & High-Fatigue Billet Alloy Specification (`DuraBore-2M™`)
*(Retained from Baseline Architecture)*

---

## 26. Deep Dive: PROD_136 — Autofrettage vs. 17-4 PH Stainless Billet Upgrade for RapidSwap™ Manifolds (`DuraBore-10M™ Extreme`)
*(Retained from Baseline Architecture)*

---

## 27. Deep Dive: PROD_146 — IsoGuard-500™ Non-Hazmat Isocyanate Neutralizing & Pump-Storage Conditioning Fluid
*(Retained from Baseline Architecture)*

---

## 28. Deep Dive: PROD_150 — Dual-Stream In-Line Particulate Filtration & Manifold De-Grit Screen (`FilterPass-250™`)
*(Retained from Baseline Architecture)*

---

## 29. Deep Dive: PROD_164 — SureMix-Geo™ High-Volume Non-Clog Static Mixer for Rapid-Setting 5:1 Polyurethanes
*(Retained from Baseline Architecture)*

---

## 30. Deep Dive: PROD_166 — MultiLift-4™ Balanced Multi-Point Geotechnical Injection Manifold
*(Retained from Baseline Architecture)*

---

## 31. Deep Dive: PROD_172 — RatioSentinel Annual Recertification Loop & Field Calibration Rig
*(Retained from Baseline Architecture)*

---

## 32. Deep Dive: PROD_UNIVERSAL_PORTS_02 — Universal Injection Ports & Bulk Contractor Master Cartons (250 & 1,000 Packs)

### 32.1 Context & Frontier Item Resolution
* **Item ID:** `PROD_UNIVERSAL_PORTS_02`
* **Core Frontier Question:** *How can Lily's 10 injection molds be optimized to produce high-margin universal surface ports compatible with competitor dispensers (Graco, ChemCo, ChemGrout), sold in 250 and 1,000 bulk master cartons to commercial distributors (White Cap, Sika, Euclid)? What are tooling wear rates and per-unit molding costs at outside molders (e.g. Elgin) versus in-house molding? What wholesale discount structure is required for commercial distribution placement?*
* **Resolution & Operational Verdict:**
  1. **Immediate Zero-Capex Commercialization:** Lily Corporation mobilizes its 100% free-and-clear owned tooling—specifically **Mold #1 (Standard Surface Mount Port - LPP)**, **Mold #2 (Corner Port)**, and **Mold #4 (Retaining Cap - LPC)**—to launch standardized **250-pack (`LPP-250`)** and **1,000-pack (`LPP-1000`) Bulk Master Cartons**.
  2. **In-House Press Manufacturing Supremacy:** Molding in-house on Greg’s Cincinnati Milacron press in Aurora delivers a landed bare part COGS of **$0.055 per port**, compared to **$0.155 to $0.185 per port** at outside Chicago-area molders (Component Plastics in Elgin / Wise Plastics in St. Charles). In-house production saves **$37,860 in direct cash COGS annually** on 300,000 units while eliminating outside setup fees, inventory minimums, and freight markups.
  3. **Universal Competitor Compatibility:** Civil applicators routinely run Lily ports on Graco, ChemCo Systems, ChemGrout, and SealBoss pumping rigs because of Lily’s wide 2.25" perforated bonding flange, low-profile entry geometry, and superior non-blowout mechanical hold at 200–800 PSI. Lily’s standard 0.375" barbed stem and LPT Snappy-Tee coupler interface natively with standard 1/4" ID pressure tubing and commercial grease-coupler delivery wands without proprietary lockouts.
  4. **High-Margin Wholesale Pricing Waterfall:** To secure national stocking status at White Cap branches and commercial distribution placement with chemical manufacturers (Sika, Euclid), Lily establishes a structured two-tier wholesale discount model:
     * **Contractor List / Direct Price:** $0.66/port ($165.00 / 250-pk) | $0.58/port ($580.00 / 1,000-pk).
     * **Distributor Wholesale (40% discount):** **$0.396/port ($99.00 / 250-pk)** | **$0.348/port ($348.00 / 1,000-pk)**.
     * **Master Pallet Tier (45% discount - 36 master cartons / 36,000 ports):** **$0.319/port ($319.00 / 1,000-pk)**.
     * **Lily Landed Aurora COGS:** **$0.0688 per port in 250-pack** ($17.21/carton) | **$0.0640 per port in 1,000-pack** ($64.04/carton).
     * **Realized Gross Margin:** Lily captures **81.6% to 82.6% Gross Margin at distributor wholesale**, and **88.9% to 89.6% Gross Margin on direct contractor desk orders**. Distributor partners capture **31.7% to 45.0% counter margins**, driving aggressive branch stocking.

```
+---------------------------------------------------------------------------------------------------------+
|                  UNIVERSAL BULK PORT PACKAGING & DISTRIBUTION WATERFALL                                  |
+---------------------------------------------------------------------------------------------------------+

  STAGE 1: IN-HOUSE PRECISION MOLDING (GREG / CINCINNATI MILACRON PRESS - AURORA)
  • Resin: High-Density Polyethylene (HDPE 6706) dried in-house; Mold #1 (8-cavity) running at 19.5s cycle.
  • Output: 1,476 ports/hour | Bare Part COGS: $0.055 ($0.031 resin + $0.022 labor + $0.002 machine power).
                                      │
                                      ▼
  STAGE 2: BENCHTOP PACKAGING CELL (JULIAN PEREZ - WORKCELL STATION #4)
  • 250-Pack: 250 ports in 4-mil polybag with tear-notch; packed in 200# test corrugated carton ($17.21 COGS).
  • 1,000-Pack: 4 x 250 polybags packed in 275# double-wall master carton ($64.04 COGS).
  • Exterior: Barcoded GS1/UPC label, White Cap SKU, quick jobsite instruction card, Dave Jepsen reorder QR.
                                      │
                                      ▼
  STAGE 3: DUAL-CHANNEL COMMERCIAL DISTRIBUTION (MAGGIE / DAVE J)
  • Channel A: Commercial Distributors (White Cap, Sika, Euclid) via Net 30/60 corporate POs.
    - 250-Pack Wholesale: $99.00 ($0.396/port) -> Lily Gross Profit: $81.79 (82.6% GM).
    - 1,000-Pack Wholesale: $348.00 ($0.348/port) -> Lily Gross Profit: $283.96 (81.6% GM).
    - Pallet Tier (36 cartons): $319.00 ($0.319/port) -> Lily Gross Profit: $254.96 (79.9% GM).
  • Channel B: Direct Contractor Sales (Dave J phone desk / jobsite trailer calls).
    - 250-Pack Direct: $165.00 ($0.660/port) -> Lily Gross Profit: $147.79 (89.6% GM).
    - 1,000-Pack Direct: $580.00 ($0.580/port) -> Lily Gross Profit: $515.96 (89.0% GM).
                                      │
                                      ▼
  STAGE 4: UNIVERSAL JOBSITE DISPENSER COMPATIBILITY
  • Native snap coupling with Lily LPT Snappy-Tee and standard 1/4" pressure tubing.
  • Compatible with Graco high-pressure grease couplers, ChemCo wands, and ChemGrout manifolds.
  • Zero epoxy blowout at 600-800 PSI due to wide 2.25" perforated bonding base.
+---------------------------------------------------------------------------------------------------------+
```

---

### 32.2 Tooling Wear Rates & In-House vs. Outside Molder Economics

#### A. Outside Molder Diligence (Elgin & St. Charles Contract Molders)
Quotes and operational parameters from regional custom molders (Component Plastics in Elgin, IL and Wise Plastics in St. Charles, IL) were formally benchmarked against Lily's on-site press capabilities:
1. **Outside Molder Quoting Mechanics:**
   * Press Machine Rate: $75.00 to $90.00 per machine-hour on a 150-ton toggle press.
   * Tool Setup & Tear-down Fee: $650.00 to $1,100.00 per production changeover.
   * Resin Markup: Cost of raw resin pellets plus a 15% to 20% material handling surcharge.
   * Packaging Labor: Bulk pack in Gaylord boxes or contractor cartons priced at $45.00 to $55.00 per labor-hour.
   * Inbound LTL Freight: Aurora is 22 miles south of Elgin; shipping palletized molded parts adds $150 to $225 per shipment (~$0.015 to $0.020 per port).
   * Minimum Order Quantity (MOQ): Outside molders mandate minimum runs of 25,000 to 50,000 shots to amortize setup charges, tying up $8,000 to $15,000 of working capital per PO.
2. **Outside Landed Unit Cost:**
   * Quoted bare part cost from Elgin: **$0.135 to $0.165 per port**.
   * Add packaging carton, polybag, and inbound freight: **$0.175 to $0.210 per finished packaged port**.

#### B. In-House Manufacturing Mechanics (Aurora On-Site Press)
Lily operates a Cincinnati Milacron hydraulic/toggle injection molding press and a dedicated desiccant material hopper dryer on-site at 240 S. Broadway in Aurora, IL, operated by Greg:
1. **Direct Material (Resin) Cost:**
   * Material: Prime Injection Grade High-Density Polyethylene (HDPE, resin melt index ~6.5–7.0 g/10 min, density ~0.955 g/cm³; e.g., ExxonMobil HD 6706 or Formosa Formolene HB5502).
   * Bulk resin procurement: 1,000-lb octabin Gaylords sourced locally from Chicago polymer distributors (PolyOne / Avient, M. Holland) at **$0.95 per pound** ($2.09/kg).
   * Part weight (LPP Surface Port): 14.8 grams (0.0326 lbs) including runner split on 8-cavity mold.
   * Resin cost per port: $0.0326 \times \$0.95 = \mathbf{\$0.0310\text{ per port}}$.
2. **Direct Molding Labor & Press Power:**
   * Greg’s fully burdened wage: $25.00/hr base + FICA/WC/benefits (28%) = **$32.00 burdened shop rate per hour** ($0.533/min).
   * Press cycle time (Mold #1, 8 cavities): 19.5 seconds total dry-to-dry cycle time (mold close, inject 3.2s, pack/hold 4.5s, cooling 7.0s, mold open/ejection 4.8s).
   * Shots per hour: $3,600 / 19.5 = 184.6\text{ shots/hour}$.
   * Ports produced per hour: $184.6 \times 8 = \mathbf{1,476.8\text{ ports/hour}}$.
   * Direct press labor per port: $\$32.00 / 1,476.8 = \mathbf{\$0.0217\text{ per port}}$.
   * Electrical power & machine operating cost: 18 kW average load on press and hopper dryer at ComEd industrial rate ($0.098/kWh) = $1.76/hr + hydraulic oil/cooling maintenance reserve ($1.45/hr) = $3.21/hr = $\mathbf{\$0.0022\text{ per port}}$.
   * **Total Bare Landed Manufacturing Cost:** $\$0.0310 + \$0.0217 + \$0.0022 = \mathbf{\$0.0549\text{ (~$0.055) per port}}$.

```
+---------------------------------------------------------------------------------------------------------+
|                  IN-HOUSE AURORA PRESS VS. OUTSIDE ELGIN MOLDER DIRECT COST AUDIT                       |
+------------------------------------+----------------------------------+---------------------------------+
| Cost Parameter                     | In-House Press (Greg / Aurora)   | Outside Toll Molder (Elgin, IL) |
+------------------------------------+----------------------------------+---------------------------------+
| **Raw Resin (HDPE Gaylord)**       | $0.0310                          | $0.0372 (15% markup)            |
| **Press Machine Time & Labor**     | $0.0239                          | $0.0880 (Machine hour rate)     |
| **Setup & Changeover Allocation**  | $0.0000 (Internal staff labor)   | $0.0220 ($850 setup on 40k run) |
| **Inbound Pallet Freight**         | $0.0000 (On-site Aurora facility)| $0.0180 (Elgin to Aurora LTL)   |
| **Bare Part Landed COGS**          | **$0.0549**                      | **$0.1652**                     |
+------------------------------------+----------------------------------+---------------------------------+
| **Packaging & Carton Assembly**    | $0.0091 (Julian Station #4)      | $0.0250 (Third-party pack fee)  |
+------------------------------------+----------------------------------+---------------------------------+
| **TOTAL PACKAGED UNIT COGS**       | **$0.0640 per port (1,000-pack)**| **$0.1902 per port (1,000-pack)**|
+------------------------------------+----------------------------------+---------------------------------+
| **ANNUAL COST DELTA (300k UNITS)** | **$19,200 Total Shop Outflow**   | **$57,060 Total Cash Outflow**  |
+------------------------------------+----------------------------------+---------------------------------+
| **NET IN-HOUSE ANNUAL CASH SAVINGS**| **+$37,860 IN HARD CASH PRESERVED PER YEAR**                      |
+------------------------------------+----------------------------------+---------------------------------+
```

#### C. Tooling Wear Rates & Preventative Maintenance Protocol
* **Tooling Metallurgy:** Molds #1 through #10 are hardened American P20 (cavity/core plates, 28–32 HRC) and S-7 shock-resistant steel (core slides and sub-gates).
* **Wear Mechanics on Polyolefins:** Unlike glass-filled structural resins that erode tool steel within 150,000 shots, unfilled High-Density Polyethylene (HDPE) and Polypropylene (PP) are completely non-abrasive. Cavity surface wash wear is virtually undetectable ($<0.00005"$ dimensional change per 100,000 shots). Tool life on P20 running HDPE routinely exceeds **1,500,000 to 2,500,000 cycles**.
* **Historical Mold Maintenance Verification (P&L Account 5440):** Historical P&L records show mold maintenance averaged $6k–$10k/year, with a one-time peak of $31,956 in 2024 when Bob overhauled cooling channels and runner blocks across 4 tools. Routine tool maintenance is strictly a $3k–$6k annual expense.
* **Shop PM SOP (Every 75,000 Shots / Annual Spring Campaign):**
  1. *Parting Line De-Varnishing:* Ultrasonic wash of cavity inserts in Station #2 using non-flammable cleaner to remove resin gassing residue.
  2. *Venting Inspection:* Dave Kling dresses parting line gas vents on the shop surface grinder (vent depth verified at 0.0012"–0.0015" to prevent flash while eliminating diesel-effect burning).
  3. *Ejector Pin Lubrication & O-Ring Refresh:* Teardown of ejector plate; replacement of high-temp fluorocarbon cooling O-rings ($45 kit); lubrication of pin guides with high-pressure synthetic grease.
  4. *Annual Maintenance Allocation:* $2,500 to $3,500 per year across Molds #1–#10, fully funded within baseline shop overhead without new capex.

---

### 32.3 Universal Competitor Dispenser Compatibility

Civil general contractors frequently purchase Lily ports even when pumping with competitive chemical rigs (Graco, ChemCo Systems, ChemGrout, SealBoss, Simpson Strong-Tie) due to superior functional geometry:

```
+---------------------------------------------------------------------------------------------------------+
|                  UNIVERSAL DISPENSER INTERFACE SPECIFICATIONS                                           |
+-------------------+--------------------+------------------------+---------------------------------------+
| Competitor System | Pumping Mechanism  | Delivery Wand Format   | Lily Universal Connection Interface   |
+-------------------+--------------------+------------------------+---------------------------------------+
| **Graco**         | Pneumatic Piston   | 1/4" NPT Delivery Wand | Lily LPP port stem snaps directly into|
| (King, Merkur,    | High-Pressure      | with 4-jaw hydraulic   | standard 1/4" grease couplers or via  |
| Reactor Crack Rig)| (500 - 3,000 PSI)  | grease-gun coupler     | LPT Snappy-Tee with 1/4" braid hose.  |
+-------------------+--------------------+------------------------+---------------------------------------+
| **ChemCo**        | Pneumatic Piston   | Wand with slip sleeve  | Lily 0.375" stem OD matches ChemCo    |
| (Model B, C, D    | Positive Disp.     | or threaded compression| quick-sleeve; LPT Snappy-Tee bypasses |
| Proportioners)    | (200 - 800 PSI)    | nut fitting            | threaded wands for manifold runs.     |
+-------------------+--------------------+------------------------+---------------------------------------+
| **ChemGrout**     | Plunger / Piston   | High-volume hose with  | LPP port accepts direct 1/4" reinforced|
| (CG-050, CG-550   | Grout Pumps        | 1/4" or 3/8" ball-valve| hose slip-fit or multi-port manifold  |
| Pressure Grouter) | (100 - 1,000 PSI)  | discharge manifold     | line from ChemGrout delivery trunk.   |
+-------------------+--------------------+------------------------+---------------------------------------+
| **SealBoss / Sika/| Manual / Pneumatic | Zerk-fitting wand or   | LPP port stem barbed detent locks into|
| Euclid Cartridges**| 2-Component Guns   | clear vinyl push-on    | 1/4" vinyl tubing (T-101); zero blow- |
| (Dual Cartridges) | (50 - 350 PSI)     | slip-tip               | off at low-to-medium cartridge head.  |
+-------------------+--------------------+------------------------+---------------------------------------+
```

* **The 4 Functional Superiorities of Lily Ports:**
  1. *Perforated Anti-Blowout Bonding Base:* Mold #1 features a wide 2.25" circular base perforated with 16 chamfered through-holes. When set in fast-setting capping epoxy (Sika AnchorFix, ChemCo Sure-Hold, Euclid Duralprep), epoxy extrudes through the perforations to form mechanical shear rivets. Lily ports resist up to **800 PSI hydraulic injection pressure without blowing off the concrete surface**.
  2. *Internal Conical Seal & Snap Geometry:* The internal port chamber features a steep 60° conical throat that funnels low-viscosity structural epoxies (down to 150 cP) cleanly into the crack without turbulence or air entrapment.
  3. *LPT Snappy-Tee Multi-Port Manifolding:* Lily’s Mold #4 produces the LPT Snappy-Tee coupler, which snaps over the LPP port stem with a tactile click and branches out into dual 1/4" barbed hose connections. This allows contractors to manifold 4 to 8 ports together along a structural crack, flooding the crack simultaneously from a single Graco, ChemCo, or ChemGrout rig—cutting contractor labor by **60%**.
  4. *Jobsite Capping Redundancy (LPC Caps):* Mold #4 produces high-flexibility LDPE friction caps (`LPC`). When resin appears at an adjacent port, the applicator snaps the LPC cap on instantly, sealing the port against back-drain without requiring makeshift wooden golf tees or masking tape.

---

### 32.4 Commercial Packaging Specifications (250 & 1,000 Packs)

Julian Perez packages finished consumables at Aurora Workcell Station #4:

```
+---------------------------------------------------------------------------------------------------------+
|                  UNIVERSAL MASTER CARTON PACKAGING SPECIFICATIONS                                       |
+------------------------------------+----------------------------------+---------------------------------+
| Packaging Parameter                | 250-Pack Master Carton (`LPP-250`)| 1,000-Pack Master Carton (`-1000`|
+------------------------------------+----------------------------------+---------------------------------+
| **Unit Quantity**                  | 250 Molded LPP Surface Ports     | 1,000 Molded LPP Surface Ports  |
| **Internal Polybag Configuration** | 1 heavy-duty 4-mil clear polybag | 4 individual 250-count polybags |
|                                    | with tear-notch and twist tie    | (allows easy branch split-pack) |
| **Corrugated Box Construction**    | 200# Test Single-Wall Corrugated | 275# Test Double-Wall Corrugated|
|                                    | (12" x 10" x 8" RSC kraft box)   | (18" x 14" x 12" heavy master)  |
| **Gross Shipping Weight**          | 9.2 lbs per carton               | 36.5 lbs per carton             |
| **Labeling & Barcoding**           | 4" x 6" Thermal Transfer Label:  | Dual 4" x 6" Labels (Opposite   |
|                                    | GS1-128 / UPC-A Barcode,         | Sides): White Cap SKU, GS1-128, |
|                                    | White Cap Part #, Jobsite QR     | Lot #, Reorder QR Code          |
| **Pallet Configuration**           | 72 cartons per 40" x 48" pallet  | 36 cartons per 40" x 48" pallet |
|                                    | (18,000 ports / 690 lbs gross)   | (36,000 ports / 1,350 lbs gross)|
| **Direct Packaging Material COGS** | $1.35 (Box: $1.15, Bag/Lbl: $0.20)| $3.16 (Master: $2.40, Bags: $0.76)|
| **Julian Packing Labor**           | 4.5 mins bench time ($2.11 labor)| 13.2 mins bench time ($6.20)    |
| **Total Packaging COGS / Box**     | **$3.46 per 250-box ($0.0138/pt)**| **$9.36 per 1,000-box ($0.0094)**|
+------------------------------------+----------------------------------+---------------------------------+
```

---

### 32.5 Commercial Distribution Placement & Wholesale Discount Waterfall

#### The Civil Contractor & Distributor Channel Reality:
Civil concrete contractors do not make purchases via consumer e-commerce carts with credit cards. They operate via **Net 30/60 corporate purchase orders**, phone orders into Dave Jepsen’s desk, or direct counter pick-up at local commercial supply houses at 6:30 AM.

To place Lily master cartons onto distributor shelves (White Cap’s 450+ branches, Sika regional distribution centers, Euclid Chemical distribution networks), Lily establishes a clear, transparent, highly incentivized wholesale discount waterfall:

```
+---------------------------------------------------------------------------------------------------------+
|                  COMMERCIAL PRICING & WHOLESALE MARGIN WATERFALL                                        |
+------------------------------------+----------------------------------+---------------------------------+
| Pricing Tier / Commercial Channel  | 250-Pack Carton (`LPP-250`)      | 1,000-Pack Master (`LPP-1000`)   |
+------------------------------------+----------------------------------+---------------------------------+
| **Direct Contractor List Price**   | **$165.00 per box ($0.660/port)**| **$580.00 per box ($0.580/port)**|
| (Dave J phone orders / Jobsite PO) |                                  |                                 |
| - Landed Aurora Shop COGS          | $17.21 per box ($0.0688/port)    | $64.04 per box ($0.0640/port)   |
| - **Lily Direct Gross Profit**     | **$147.79 Gross Profit per box** | **$515.96 Gross Profit per box**|
| - **Lily Direct Gross Margin %**   | **89.6% Gross Margin**           | **89.0% Gross Margin**          |
+------------------------------------+----------------------------------+---------------------------------+
| **Distributor Wholesale (40% Off)**| **$99.00 per box ($0.396/port)** | **$348.00 per box ($0.348/port)**|
| (White Cap / Sika Branch Stocking) |                                  |                                 |
| - Landed Aurora Shop COGS          | $17.21 per box ($0.0688/port)    | $64.04 per box ($0.0640/port)   |
| - **Lily Wholesale Gross Profit**  | **$81.79 Gross Profit per box**  | **$283.96 Gross Profit per box**|
| - **Lily Wholesale Gross Margin %**| **82.6% Gross Margin**           | **81.6% Gross Margin**          |
| - *Distributor Counter Resale*     | $145.00 to $165.00 per box       | $495.00 to $580.00 per box      |
| - *Distributor Gross Margin %*     | **31.7% to 40.0% Branch Margin** | **29.7% to 40.0% Branch Margin**|
+------------------------------------+----------------------------------+---------------------------------+
| **Pallet Stocking Tier (45% Off)** | *Available in 1,000-Pack Only*   | **$319.00 per box ($0.319/port)**|
| (Central CDC / Full Pallet Orders) |                                  | (36 Cartons = $11,484.00 Order) |
| - Landed Aurora Shop COGS          |                                  | $64.04 per box ($0.0640/port)   |
| - **Lily Pallet Gross Profit**     |                                  | **$254.96 Gross Profit per box**|
| - **Lily Pallet Gross Margin %**   |                                  | **79.9% Gross Margin**          |
| - *Distributor CDC Gross Margin*   |                                  | **35.6% to 45.0% Realized Margin|
+------------------------------------+----------------------------------+---------------------------------+
```

* **Why White Cap and Sika Stock Lily Cartons:**
  1. *Guaranteed 32% to 40%+ Branch Margins:* Commodity imported ports offer distributors <22% margins with high breakage. Lily’s wholesale structure guarantees White Cap branch managers healthy 32–40% counter margins.
  2. *Domestic Supply Reliability (Aurora, IL):* Lead time from Aurora to Midwest White Cap branches is 24–48 hours via LTL, completely eliminating 12-week overseas supply chain delays.
  3. *No Forced Portals or Logins:* Maggie M receives distributor EDI and PDF purchase orders directly into QuickBooks Desktop, confirming shipment within 48 hours.
  4. *The Jobsite Reorder QR Trojan Horse:* Every carton exterior carries a high-contrast QR code. When an applicator running low on a bridge job scans the box with their smartphone, it instantly generates a pre-formatted SMS and email order draft addressed to `orders@lilycorp.com` and Dave Jepsen’s desk with carton part numbers and distributor branch routing options.

---

### 32.6 Complete Universal Consumable SKU Portfolio

```
+---------------------------------------------------------------------------------------------------------+
|                  UNIVERSAL CONSUMABLE MASTER PRODUCT LINE                                               |
+---------------+-----------------------------------+-------------+---------------+-----------+-----------+
| SKU Number    | Description                       | Package Qty | Contractor Lst| Wholesale | Landed COG|
+---------------+-----------------------------------+-------------+---------------+-----------+-----------+
| `LPP-250`     | Universal Flat Surface Port       | 250 Box     | $165.00       | $99.00    | $17.21    |
| `LPP-1000`    | Universal Flat Surface Port Master| 1,000 Box   | $580.00       | $348.00   | $64.04    |
| `LPC-250`     | Entry Port Friction Sealing Caps  | 250 Box     | $55.00        | $33.00    | $6.25     |
| `LPC-1000`    | Entry Port Friction Caps Master   | 1,000 Box   | $195.00       | $117.00   | $22.50    |
| `LPT-250`     | Universal Snappy-Tee Port Coupler | 250 Box     | $185.00       | $111.00   | $21.40    |
| `LPT-1000`    | Universal Snappy-Tee Coupler Mstr | 1,000 Box   | $640.00       | $384.00   | $78.20    |
| `LP-CORNER-250| Universal 90° Corner Port (Mold#2)| 250 Box     | $195.00       | $117.00   | $22.80    |
| `LP-COMBO-250`| Bridge Crack Starter Master Pack  | 250 of Each | $385.00       | $231.00   | $44.86    |
|               | (250 LPP + 250 LPC + 250 LPT)     |             |               |           |           |
+---------------+-----------------------------------+-------------+---------------+-----------+-----------+
```

---

### 32.7 Financial Contribution & Cash Flow Impact (Years 1–3)

Mobilizing Lily’s existing molds into universal bulk cartons requires **$0.00 in tooling capex** and **<$800 in packaging die/label stock working capital**, fitting securely within Jack Fay’s $20,000 discretionary capex cap and $50,000 working capital injection:

```
+---------------------------------------------------------------------------------------------------------+
|                 UNIVERSAL BULK MASTER CARTON FINANCIAL PROJECTION (YEARS 1–3)                           |
+------------------------------------+------------+------------+------------+-----------------------------+
| Metric                             | Year 1     | Year 2     | Year 3     | Strategic Notes             |
+------------------------------------+------------+------------+------------+-----------------------------+
| **Total Ports Produced & Sold**    | 240,000    | 380,000    | 520,000    | Greg runs in winter batch   |
| - 250-Pack Cartons Sold            | 320 Boxes  | 480 Boxes  | 640 Boxes  | Regional branches / direct  |
| - 1,000-Pack Master Cartons Sold   | 160 Boxes  | 260 Boxes  | 360 Boxes  | Pallet distributor orders   |
| **Commercial Distributor Share**   | 55.0%      | 65.0%      | 70.0%      | White Cap / Sika expansion  |
| **Direct Contractor Desk Share**   | 45.0%      | 35.0%      | 30.0%      | Dave J phone relationships  |
| **Gross Invoiced Revenue**         | $123,400   | $186,200   | $248,800   | Consumable revenue baseline |
| **Landed Aurora Shop COGS**        | $18,480    | $27,850    | $37,210    | Direct resin, box, labor    |
| **Net Gross Profit Contribution**  | **$104,920**| **$158,350**| **$211,590**| **Pure gross profit engine**|
| **Blended Realized Gross Margin %**| **85.0%**  | **85.0%**  | **85.0%**  | **Vastly exceeds 55% target**|
| **Shop Press Hours Consumed**      | 162.5 hrs  | 257.4 hrs  | 352.1 hrs  | <18% of Greg's annual hours |
+------------------------------------+------------+------------+------------+-----------------------------+
```

---

## 33. Core Legacy Equipment & Proportioner Line Optimization

Lily’s equipment portfolio has anchored heavy civil crack repair and overlay markets since 1982 due to its mechanical simplicity and extreme durability:

```
+---------------------------------------------------------------------------------------------------------+
|                                    LILY EQUIPMENT PORTFOLIO MATRIX                                      |
+-------------------+-----------------+------------------+---------------+--------------------------------+
| Machine Model     | Target Markets  | Mechanism        | Dispense Rate | Strategic Action               |
+-------------------+-----------------+------------------+---------------+--------------------------------+
| **CD-250**        | Bridge Overlays,| Pneumatic Piston | 300 - 600 GPH | Standardize with DeckFlush™,   |
| High-Volume       | HFST, Parking   | Air-Logic        | (Fixed Ratio) | RapidSwap™ wet-ends, Ratio-Lock|
|                   |                 |                  |               | AeroShift™ Drop-In Cartridges, |
|                   |                 |                  |               | FrostGuard™, CleanPass-250,    |
|                   |                 |                  |               | SafePurge-250, Omni-Flex™ whips|
|                   |                 |                  |               | RatioSentinel™, DuraBore-2M™ Al|
|                   |                 |                  |               | DuraBore-10M™ 17-4, FilterPass,|
|                   |                 |                  |               | and Annual Recertification Loop|
+-------------------+-----------------+------------------+---------------+--------------------------------+
| **CD-250          | Slab Jacking,   | High-Cv Spool +  | 480 - 720 GPH | Turnkey geotechnical rig       |
| GeoMaster**       | Soil Grouting,  | GeoLink Carriage | (1:1 & 5:1)   | (PROD_62); standard with       |
|                   | Deep Injection, |                  |               | AeroShift™ drop-in cartridges, |
|                   | Warehouse Floors|                  |               | FrostGuard™ vortex mufflers,   |
|                   |                 |                  |               | DuraBore-10M™ 17-4 PH cores;   |
|                   |                 |                  |               | drives PROD_UNIVERSAL_PORTS,   |
|                   |                 |                  |               | DeepDrive tips, DrySpear,      |
|                   |                 |                  |               | CleanPass-Seq, FilterPass-250, |
|                   |                 |                  |               | SureMix-Geo™ non-clog mixers,  |
|                   |                 |                  |               | and PROD_166 MultiLift-4™.     |
+-------------------+-----------------+------------------+---------------+--------------------------------+
| **CD-150**        | Mid-Size Overlays| Pneumatic Piston | 100 - 250 GPH | Standardize fluid manifold with|
| Medium Proportioner| Dowel Grouting  | Mechanical Air   | (Fixed Ratio) | CD-250 RapidSwap™ & DuraBore™  |
+-------------------+-----------------+------------------+---------------+--------------------------------+
| **CD-15 / CD-30** | Structural Crack| Portable Piston  | 15 - 45 GPH   | Primary driver of LPP-250 and  |
| Crack Injection   | Injection (DOT) | Dual Action      | (1:1, 2:1,    | LPP-1000 universal master      |
|                   | Bridge Scaffolds| Radial T-Slot    |  3:1 drop-in) | cartons. Upgraded with         |
|                   |                 |                  |               | RatioShift-15™ sleeves,        |
|                   |                 |                  |               | Omni-Flex whips, FilterPass-250|
|                   |                 |                  |               | and RatioSentinel compliance.  |
+-------------------+-----------------+------------------+---------------+--------------------------------+
| **CP-5 Grouter**  | Soil Nailing,   | Progressive      | 5 GPM         | Harvest orders; minimize shop  |
| Pneumatic Grouter | Void Grouting   | Cavity / Piston  | Continuous    | time; no active R&D spend.     |
+-------------------+-----------------+------------------+---------------+--------------------------------+
```

---

## 34. Consumable Moat: In-House & Contract Molded Infrastructure

```
+----------------------------------------------------------------------------------------------------+
|                                    LILY'S 10 PROPRIETARY IN-HOUSE MOLDS                            |
+----+----------------------------------+-------------------+---------------+------------------------+
|Mold| Description                      | Resin Material    | Gross Margin  | Primary Market         |
+----+----------------------------------+-------------------+---------------+------------------------+
| #1 | Standard Surface Mount Port (LPP)| HDPE / Polypro    | 81.6% - 89.6% | Bridge & Universal Bulk|
| #2 | Low-Profile 90° Corner Port      | High-Impact Poly  | 79.2% - 87.5% | Retaining & Parapet Wall|
| #3 | Drill-In / Socket Port           | Engineered Nylon  | 69.5% - 75.0% | High-Pressure Sub-Slab |
| #4 | Entry Port Friction Cap (LPC)    | LDPE              | 80.5% - 88.0% | Jobsite Port Sealing   |
| #5 | Mixing Chamber Coupling Adapter  | Acetal / Delrin   | 71.0% - 78.0% | CD-250 Delivery System |
| #6 | Bayonet Static Mixer Shroud      | PA66-GF33         | 79.6% - 80.1% | SureMix & Geotechnical |
| #7 | Multi-Tier Check Valve Body      | Polypropylene     | 73.5% - 81.0% | Backflow Prevention    |
| #8 | 1:1 Dispenser Plunger Disc       | UHMW-PE           | 66.8% - 72.0% | CD-15 Proportioning    |
| #9 | 2:1 Dispenser Plunger Disc       | UHMW-PE           | 65.9% - 71.5% | CD-15 Proportioning    |
| #10| Custom High-Flow Deck Port       | Polypropylene     | 75.3% - 82.0% | HFST Bridge Overlays   |
+----+----------------------------------+-------------------+---------------+------------------------+
```

*Note on Speculative Tooling (Molds #11–13):* In strict compliance with Jack Fay's **$20,000 Year 1 discretionary capex ceiling**, speculative new tooling investments for Mold #11, Mold #12, and Mold #13 are **FROZEN in Year 1**. Lily's immediate consumable growth is driven 100% through high-volume bulk master carton optimization of existing Molds #1, #2, and #4 (`PROD_UNIVERSAL_PORTS_02`), generating pure incremental gross profit with zero tooling debt.

---

## 35. R&D Pipeline: Prioritized Horizon Roadmap

```
+--------------------------------------------------------------------------------------------------------+
|                                     LILY R&D EXECUTION HORIZON                                         |
+--------------------+-------------------------------------------+-----------+------------+--------------+
| Project Codename   | Scope & Deliverable                       | Timeline  | Target GM% | Shop Lead    |
+--------------------+-------------------------------------------+-----------+------------+--------------+
| **PROD_UNIVERSAL_  | Universal port packaging into 250 & 1,000 | Months 1-2| 81.6% Dist | Greg, Julian |
| PORTS_02: Master** | master cartons for White Cap / Sika placement|         | 89.0% Direct| & Dave Jepsen|
+--------------------+-------------------------------------------+-----------+------------+--------------+
| **PROD_22:         | Closed-loop pneumatic recirculating flush | Months 1-3| 72.4% ext. | Dave K. &    |
| DeckFlush™**       | kit for CD-250 rental fleet and sales.    |           | (Fleet ROI)| Julian P.    |
+--------------------+-------------------------------------------+-----------+------------+--------------+
| **PROD_25:         | Standardized commercial retrofit kit and  | Months 3-6| 74.7% Kit  | Dave K. &    |
| RapidSwap™ Wet-End**| factory rebuild cartridge exchange loop.  |           | 85.3% Exch | Julian P.    |
+--------------------+-------------------------------------------+-----------+------------+--------------+
| **PROD_32:         | Full-port oversized dry-break coupling    | Months 4-5| System-wide| Dave K. &    |
| Cold-Flow Spec**   | standard for cold-weather bridge epoxies. |           | Spec Floor | Julian P.    |
+--------------------+-------------------------------------------+-----------+------------+--------------+
| **PROD_48:         | Sealed non-resettable mechanical/NFC cycle| Months 4-6| 73.3% Ext. | Dave K. &    |
| StrokeTrack™**     | counter & shroud (<$85 landed cost).      |           | (Fleet ROI)| Julian P.    |
+--------------------+-------------------------------------------+-----------+------------+--------------+
| **PROD_56:         | Ratio-Lock™ pneumatic differential ratio- | Months    | 77.0% Kit  | Dave K. &    |
| Ratio-Lock™ Block**| interlock valve (<$210 cost, 75 PSI trip).| 8-10      | (DOT Spec) | Julian P.    |
+--------------------+-------------------------------------------+-----------+------------+--------------+
| **PROD_62:         | GeoConversion Spool & GeoLink™ 1:1 and 5:1| Months    | 74.1% Kit  | Dave K. &    |
| GeoConversion**    | kit for polyurethanes (8-12 GPM).         | 10-12     | 72.0% Rig  | Julian P.    |
+--------------------+-------------------------------------------+-----------+------------+--------------+
| **PROD_68:         | AeroShift™ air-logic spool & pilot modular| Months    | 76.4% Kit  | Dave K. &    |
| AeroShift™ Module**| quick-swap cartridge & $250 core exchange.| 11-13     | 86.0% Exch | Julian P.    |
+--------------------+-------------------------------------------+-----------+------------+--------------+
| **PROD_94:         | AeroShift FrostGuard™ sub-zero de-icing   | Months    | 77.3% Kit  | Dave K. &    |
| FrostGuard™**      | vortex muffler system (<$45 BOM cost).    | 12-14     | (Fleet ROI)| Julian P.    |
+--------------------+-------------------------------------------+-----------+------------+--------------+
| **PROD_74:         | Mold #6 retooling into SureMix-250™       | Months    | 79.6% Shrd | Jack Fay /   |
| SureMix Bayonet**  | bayonet shroud & SureCore-18™ consumable. | 12-14     | 72.4% Core | Wise Plastics|
+--------------------+-------------------------------------------+-----------+------------+--------------+
| **PROD_92:         | DeepDrive-15™ modular 1/2" Sched 80 lance | Months    | 78.9% Anvil| Dave K.,     |
| DeepDrive Lance**  | driving anvil & Mold #14 knock-off tip.   | 14-16     | 82.2% Tip  | Greg & Julian|
+--------------------+-------------------------------------------+-----------+------------+--------------+
| **PROD_103:        | CleanPass-250™ snap-on closed-loop flush  | Months    | 80.4% List | Dave K. &    |
| CleanPass-250™**   | bypass manifold & bung adapter ($38 COGS).| 15-17     | 71.7% Dist | Julian P.    |
+--------------------+-------------------------------------------+-----------+------------+--------------+
| **PROD_104:        | SafePurge-250™ closed-loop bio-citrus/    | Months    | 75.0% List | Jack Fay &   |
| SafePurge-250™**   | glycol fluid & pre-plumbed 2.5-gal carboy.| 16-18     | 80.0% Exch | Toll Blender |
+--------------------+-------------------------------------------+-----------+------------+--------------+
| **PROD_108:        | RatioShift-15™ modular quick-change ratio | Months    | 77.1% Kit  | Dave K. &    |
| RatioShift-15™**   | sleeve kit (1:1, 2:1, 3:1) for CD-15 pump.| 17-19     | 85.0% OEM  | Julian P.    |
+--------------------+-------------------------------------------+-----------+------------+--------------+
| **PROD_118:        | Omni-Flex™ 3,500 PSI micro-bore whip hose | Months    | 74.7% List | Dave K. &    |
| Omni-Flex™ Whip**  | benchtop hydraulic crimping workcell.     | 18-20     | 66.7% Dist | Julian P.    |
+--------------------+-------------------------------------------+-----------+------------+--------------+
| **PROD_120:        | DrySpear-250™ moisture-sealed desiccant   | Months    | 77.9% Kit  | Dave K. &    |
| DrySpear-250™**   | drum spear kit & indicating breather pack.| 19-21     | 82.3% Breth| Julian P.    |
+--------------------+-------------------------------------------+-----------+------------+--------------+
| **PROD_124:        | RatioSentinel-100™ mechanical dual-buret  | Months    | 73.4% List | Dave K. &    |
| RatioSentinel™**   | ratio verification manifold (<$450 COGS). | 20-22     | 62.2% Dist | Julian P.    |
+--------------------+-------------------------------------------+-----------+------------+--------------+
| **PROD_128:        | CleanPass-Seq™ air-logic timed purge      | Months    | 81.0% List | Dave K. &    |
| CleanPass-Seq™**   | sequencing valve for rapid-set urethanes. | 21-23     | 72.8% Dist | Julian P.    |
+--------------------+-------------------------------------------+-----------+------------+--------------+
| **PROD_130:        | GeoWhip-Bal™ handheld auto-balancing wand | Months    | 75.0% List | Dave K. &    |
| GeoWhip-Bal™**     | for 10+ GPM 1:1 and 5:1 void grouting.    | 22-24     | 64.4% Dist | Julian P.    |
+--------------------+-------------------------------------------+-----------+------------+--------------+
| **PROD_132:        | AeroShift™ tool-less drop-in directional  | Months    | 79.4% List | Dave K. &    |
| AeroShift™ Drop-In**| air logic field cartridge (<60s swap).   | 23-25     | 87.4% Exch | Julian P.    |
+--------------------+-------------------------------------------+-----------+------------+--------------+
| **PROD_134:        | DuraBore-2M™ autofrettaged billet fluid   | Months    | 83.2% List | Dave K. &    |
| DuraBore-2M™**     | manifold (>2.5M cycles, thread-bypass).   | 24-26     | 89.6% Exch | Julian P.    |
+--------------------+-------------------------------------------+-----------+------------+--------------+
| **PROD_136:        | DuraBore-10M™ severe-duty 17-4 PH H1150   | Months    | 82.9% List | Dave K. &    |
| 17-4 PH Billet**   | stainless billet core (>10M infinite cyc).| 25-27     | 90.3% Exch | Julian P.    |
+--------------------+-------------------------------------------+-----------+------------+--------------+
| **PROD_146:        | IsoGuard-500™ anhydrous isocyanate        | Months    | 73.5% List | Jack Fay &   |
| IsoGuard-500™**    | storage & conditioning fluid (Elgin toll).| 26-28     | 75.1% Pail | Toll Blender |
+--------------------+-------------------------------------------+-----------+------------+--------------+
| **PROD_150:        | FilterPass-250™ dual-stream de-grit block | Months    | 75.7% List | Dave K. &    |
| FilterPass-250™**  | & 80-mesh stainless screens (<$65 COGS).  | 27-29     | 80.0% Bsk  | Julian P.    |
+--------------------+-------------------------------------------+-----------+------------+--------------+
| **PROD_164:        | SureMix-Geo™ high-volume non-clog static  | Months    | 80.1% List | Dave K.,     |
| SureMix-Geo™**     | mixer with pneumatic purge (<$2.40 COGS). | 28-30     | 70.1% Dist | Greg & Julian|
+--------------------+-------------------------------------------+-----------+------------+--------------+
| **PROD_166:        | MultiLift-4™ balanced multi-point geo     | Months    | 77.1% List | Dave K. &    |
| MultiLift-4™**     | injection manifold ($88 landed COGS).     | 29-31     | 66.8% Dist | Julian P.    |
+--------------------+-------------------------------------------+-----------+------------+--------------+
| **PROD_172:        | RatioSentinel™ annual factory recert loop | Months    | 86.9% Svc  | Jack Fay &   |
| RatioSentinel Recert| & Station #1 calibration rig ($38.50 COGS)| 30-32     | 76.9% Rig  | Julian P.    |
+--------------------+-------------------------------------------+-----------+------------+--------------+
```

---

## 36. The Graveyard: Explicit Product & Strategic Rejections

```
+-------------------------------------------------------------------------------------------------------+
|                                    DOCUMENTED STRATEGIC AUTOPSIES                                     |
+-----------------------------+-----------------------+-------------------------------------------------+
| Proposed Concept            | Status                | Concrete Operational Reason for Rejection       |
+-----------------------------+-----------------------+-------------------------------------------------+
| **Outsourcing Molded Ports  | REJECTED /            | External custom molders charge $0.155-$0.185/pt |
| to Elgin / Contract Molders**| FATAL MARGIN LEAK     | compared to $0.055 in-house; requires $850 setup|
| (PROD_UNIVERSAL Outsourcing)|                       | charges and 50k MOQs; burns $37.8k cash per year|
|                             |                       | and idles Lily's paid-off Milacron press.       |
+-----------------------------+-----------------------+-------------------------------------------------+
| **Proprietary Latching Port | REJECTED /            | Restricting port necks to proprietary Lily wands|
| Lockouts (No Competitors)** | ANTI-GROWTH ERROR     | prevents 80% of civil applicators from buying;  |
| (Lockout Port Alternative)  |                       | contractors running Graco/ChemCo buy generic    |
|                             |                       | ports instead; universal compatibility is key.  |
+-----------------------------+-----------------------+-------------------------------------------------+
| **Forced E-Commerce Login   | REJECTED /            | Civil general contractors buy on corporate POs; |
| Portals for Port Orders**   | PROCUREMENT MISMATCH  | jobsite superintendents refuse to reset website |
| (Web Portal Cart Alternate) |                       | passwords; ordering must run via Net 30/60 POs, |
|                             |                       | phone desk, and distributor counter pick-up.    |
+-----------------------------+-----------------------+-------------------------------------------------+
| **Speculative New Tooling   | REJECTED /            | Sinks $31.8k on Mold #11 and $13.8k on Mold #12;|
| in Year 1 (Molds #11-#13)** | CAPEX CEILING VIOLATED| violates strict $20k Year 1 capex limit; freezes|
| (Early Mold Tooling Builds) |                       | working capital ahead of Q1 winter debt service.|
|                             |                       | Deferred to Year 2 cash-flow surplus.           |
+-----------------------------+-----------------------+-------------------------------------------------+
| **Outsourced Commercial     | REJECTED /            | External metrology service labs charge $450-$650|
| Metrology Calibration Labs**| FATAL TIME & MARGIN   | per unit; require 3-4 week queues; destroys 87% |
| (PROD_172 Outsourcing Alt)  |                       | gross margin; contractors refuse to wait a month|
|                             |                       | for testing turnaround during busy bridge season|
+-----------------------------+-----------------------+-------------------------------------------------+
| **Contractor Self-Cert Field| REJECTED /            | State DOT inspectors reject contractor self-cert|
| Sticker & Seal Tag Packs**  | REGULATORY DISASTER   | tags without certified factory traceability;    |
| (PROD_172 Self-Cert Alt)    |                       | applicators slap stickers on worn, leaking units|
|                             |                       | exposing Lily to catastrophic liability.        |
+-----------------------------+-----------------------+-------------------------------------------------+
| **Heated Polyurethane Slab  | REJECTED /            | Sinks 45+ shop hours into wiring/chassis work;  |
| Jacking Trailer Rig**       | UNVIABLE              | requires $40k UL 508A capex; requires 24/7      |
| ("AeroLift" Graco Clone)    |                       | national mobile field service Lily cannot staff;|
|                             |                       | compresses GM to <25%. Replaced by PROD_62      |
|                             |                       | unheated pneumatic GeoConversion kit (74% GM).  |
+-----------------------------+-----------------------+-------------------------------------------------+
| **Standard 1/2" Poppet      | REJECTED /            | Induces 182-246 PSI pressure drops with >3,500  |
| Dry-Break Couplers**        | UNVIABLE              | cP cold epoxy; causes motor stall, cavitation,  |
| (PROD_32 Autopsy)           |                       | and catastrophic off-ratio dispensing.          |
+-----------------------------+-----------------------+-------------------------------------------------+
```

---

## 37. 90-Day to 450-Day Execution Playbook for Jack Fay

```
+---------------------------------------------------------------------------------------------------+
|                                 TURNAROUND PRODUCT EXECUTION SPRINT                               |
+---------------------------------------------------------------------------------------------------+
| MONTH 1: UNIVERSAL BULK PACKAGING (PROD_UNIVERSAL_PORTS_02) & PROD_22 PROTOTYPING                 |
| • Week 1-2: Audit Molds #1, #2, and #4 with Greg; verify barrel heat zones and desiccant dryer.    |
|             Procure initial run of 200# single-wall (250-pk) and 275# double-wall (1,000-pk) boxes.|
|             Maggie prints GS1-128 barcode labels with White Cap formatting and Dave J QR code.    |
| • Week 3-4: Greg runs 50,000 LPP ports on Cincinnati Milacron press. Julian Perez sets up Station |
|             #4 packaging bench; packs first 50 master cartons of LPP-250 and 25 cartons of LPP-1000|
|             Dave Kling machines first three DF-101 aluminum flush manifold blocks on the Hurco.   |
+---------------------------------------------------------------------------------------------------+
| MONTH 2: COMMERCIAL DISTRIBUTOR ROLLOUT & FLEET DEPLOYMENT                                        |
| • Week 5-6: Dave Jepsen ships sample master cartons of LPP-250 and LPP-1000 to top 25 regional    |
|             White Cap concrete branches and Sika/Euclid regional technical reps.                  |
|             Deploy DeckFlush™ units inside 5 active rental CD-250 crates headed to IDOT projects. |
| • Week 7-8: Secure first stocking purchase orders from White Cap Midwest (5 pallets / 180,000 pts)|
|             Build and pressure-test 3 pilot RapidSwap™ conversion kits with Julian Perez.          |
|             Update Maggie's rental contract with the $750 DeckFlush Cleanliness Deposit.          |
+---------------------------------------------------------------------------------------------------+
| MONTH 3: RAPIDSWAP™ COMMERCIAL ROLLOUT & FLEET INTEGRATION                                        |
| • Week 9-10: 100% of internal rental fleet equipped with DeckFlush™ kits and RapidSwap™ wet-ends. |
| • Week 11: Launch the CD-250 RapidSwap™ Retrofit Kit ($3,450) and Exchange Program ($950).        |
|            Dave Jepsen initiates telephone blitz to top 50 historical CD-250 machine owners.      |
| • Week 12: Collect initial batch of DeckFlush™ rental returns; verify zero seized wet-ends.       |
+---------------------------------------------------------------------------------------------------+
| MONTH 4: COUPLER RETROFIT (PROD_32) & STROKETRACK™ (PROD_48) PROTOTYPING                          |
| • Week 13-14: Dave Kling updates Hurco CNC program for RS-203 manifold blocks to 3/4" NPT bore.    |
| • Week 15-16: Bench-test full-port 3/4" ball disconnects against chilled 4,500 cP resin at 38°F.  |
|               Issue TSB-2026-03. Machine initial prototype CC-303 StrokeTrack™ shrouds on Hurco.  |
+---------------------------------------------------------------------------------------------------+
| MONTH 5: STROKETRACK™ FLEET ROLLOUT (PROD_48) & BULK CARTON MIDWEST SCALE                         |
| • Week 17-18: Outfit 10 internal rental CD-250s with StrokeTrack™ telemetry shrouds ($78.70 COGS).|
|               Confirm speculative tooling (Molds #11-13) remains frozen to protect $20k capex cap.|
| • Week 19-20: Maggie logs mechanical checkout/checkin cycle readings in QuickBooks Desktop.       |
|               Review bulk master carton reorder rates from White Cap; fulfill 3 additional pallets.|
+---------------------------------------------------------------------------------------------------+
| MONTH 6: RATIO-LOCK™ (PROD_56) PROTOTYPING & DISTRIBUTOR CONQUEST EXPANSION                       |
| • Week 21-22: Dave Kling programs Hurco VMC for RL-101 manifold block and RL-102 sensing pistons.  |
| • Week 23-24: Validate cross-rig compatibility of LPP ports with Graco King and ChemCo pumps.     |
|               Invoice first $4,200 in rental StrokeTrack™ usage overage billings.                 |
+---------------------------------------------------------------------------------------------------+
| MONTH 7-8: RATIO-LOCK™ BENCH CALIBRATION & FIELD VALIDATION                                       |
| • Week 25-28: Julian Perez bench-calibrates prototype Ratio-Lock™ spool on Station #1 test bench.  |
|               Verify crisp air-dump cutoff at 75 ± 3 PSI differential. Deploy on IDOT bridges.    |
+---------------------------------------------------------------------------------------------------+
| MONTH 9-10: GEOCONVERSION (PROD_62) ENGINEERING & BENCH PROOF                                     |
| • Week 29-32: Dave Kling machines GL-512 bedplate and GL-513 4140 offset drive bridge on Hurco.   |
|               Run continuous 10 GPM water and surrogate fluid trials on shop floor.               |
+---------------------------------------------------------------------------------------------------+
| MONTH 11-12: GEOCONVERSION LAUNCH & AEROSHIFT™ (PROD_68) TOOLING                                  |
| • Week 33-36: Launch CD250-GEO-KIT. Close first 3 turnkey CD250-GEOMASTER orders ($24,500 ea).    |
|               Dave Kling machines pilot batch of 5 AS-602 sub-plates and AS-601 cartridges.       |
+---------------------------------------------------------------------------------------------------+
| MONTH 13-14: FROSTGUARD™ (PROD_94) BENCH PROOF & PACKER ROLLOUT                                   |
| • Week 37-40: Bench-test AeroShift FrostGuard™ diffuser on Station #2 at 22°F for 4 continuous hrs|
|               at 65 CPM. Confirm 0 PSI backpressure rise and zero spool ice accumulation.         |
| • Week 41-44: Commercial AeroShift™ Kit ($1,195) + FrostGuard™ winter option ($185 list) rollout. |
+---------------------------------------------------------------------------------------------------+
| MONTH 15-18: OMNI-FLEX™ (PROD_118) & DRYSPEAR-250™ (PROD_120) COMMISSIONING                       |
| • Week 45-52: Set up Station #3 micro-crimp benchtop cell ($3,450 capex); proof whips to 4,000 PSI|
|               Standardize DrySpear-250™ desiccant spears inside 100% of GeoMaster rental crates.  |
+---------------------------------------------------------------------------------------------------+
| MONTH 19-24: RATIOSENTINEL™ (PROD_124) & COMPLIANCE ANNUITY ROLLOUT                               |
| • Week 53-64: Standardize RatioSentinel™ verification manifolds on bridge rental deployments.     |
|               Commission Station #1 NIST-traceable calibration rig (`RS-CAL-100`); launch $295/yr|
|               annual factory recertification loop across active fleet and contractor accounts.    |
+---------------------------------------------------------------------------------------------------+
```

---

## 38. Master Summary: Resolution of Frontier Items

| Frontier Item | Core Strategic Resolution | Manufacturing & Economic Verification |
| :--- | :--- | :--- |
| **PROD_UNIVERSAL_PORTS_02**<br>Universal Bulk Master Cartons (250 & 1,000 Packs) | **APPROVED & DEPLOYED (ZERO CAPEX).** Packages Molds #1, #2, and #4 into standardized 250 (`LPP-250`) and 1,000 (`LPP-1000`) master cartons with GS1/UPC barcodes and QR reorder links for national placement at White Cap, Sika, and Euclid. Fully compatible with Graco, ChemCo, ChemGrout, and SealBoss dispensers. | • **In-House COGS:** $0.055 bare part / **$0.064 to $0.069 packaged** in Aurora (vs. $0.155–$0.185 at Elgin toll molders; saves **+$37.8k cash/yr**).<br>• **Wholesale Waterfall:** 40% discount ($0.348–$0.396/pt); 45% pallet tier ($0.319/pt).<br>• **Economics:** Direct List: $0.58–$0.66/pt (**89.0–89.6% GM**); Wholesale: **79.9% to 82.6% GM**; Distributor Branch Margin: **31.7% to 45.0%**.<br>• **Contribution:** **+$104.9k to $211.6k net gross profit/yr**; zero capex; protects $20k Y1 cap. |
| **PROD_22**<br>DeckFlush™ Purge Kit | **APPROVED & DEPLOYED.** Fully solves internal fleet fouling leak. Integrates closed-loop pneumatic flush inside crate lid. | • **COGS:** $384.50 (1.75 shop hrs).<br>• **Fleet Impact:** Fouling drops from 38.2% to 8.4% (78% drop); saves $18,067 and 294 shop hrs/yr.<br>• **Aftermarket:** $1,495 MSRP (72.4% GM). |
| **PROD_25**<br>RapidSwap™ Wet-End Retrofit & Exchange | **APPROVED & COMMERCIALIZED.** Standardizes quick-swap wet-end into a $3,450 retrofit kit for 150+ legacy rigs, unlocking an 85% GM cartridge rebuild annuity. | • **Kit Price:** $3,450.00 \| **BOM + Labor:** $872.50 (74.7% GM).<br>• **Rebuild Fee:** $950.00 \| **Shop Cost:** $140.00 (85.3% GM).<br>• **Year 1-2 Impact:** +$112k to $171k revenue; +$86k to $134k high-margin gross profit. |
| **PROD_32**<br>Cold-Weather Coupler Flow Limits | **APPROVED & SPECIFIED.** Replaces restricted 1/2" poppet dry-breaks ($>150\text{ PSI}$ drop) with **3/4" Full-Port Ball Disconnects** ($11.8\text{ PSI}$ drop) for cold-weather epoxies (>3,500 cP). | • **Pressure Drop Reduction:** 214.2 PSI down to 11.8 PSI (-94.5%).<br>• **Operational Benefit:** Prevents CD-250 motor stall, suction cavitation, and 20%+ stoichiometric off-ratio failures on bridge decks.<br>• **Shop Integration:** Hurco bored to 3/4" NPT (+2.5 mins); landed BOM held flat. |
| **PROD_48**<br>StrokeTrack™ Cycle-Counter & Shroud | **APPROVED & DEPLOYED.** Integrates sealed, non-resettable 6-digit mechanical counter + passive NFC tag in a CNC billet armor shroud on the RapidSwap™ bed-plate. | • **Landed Unit COGS:** **$78.70** (Clears <$85 ceiling).<br>• **Rental Billing:** Enables $0.20/gal excess usage billing (+ $38k to $46k/yr net rental profit).<br>• **Predictive Maintenance:** Automates 75k cycle seal alerts before bridge failures; saves 112 shop hrs/yr.<br>• **Aftermarket SKU:** $295.00 MSRP (73.3% GM). |
| **PROD_56**<br>Ratio-Lock™ Differential Ratio-Interlock | **APPROVED & ENGINEERED.** 100% mechanical, explosion-proof differential spool valve integrated into RapidSwap™ discharge manifold; trips air motor in <140 ms when $\Delta P > 75\text{ PSI}$ (>5% drift). | • **Landed Unit COGS:** **$206.00** (BOM: $186.20 \| Shop Labor: 35 mins / $19.80).<br>• **Regulatory Moat:** Meets IDOT 1020/1025, Caltrans 60-3.03, TxDOT DMS-6100 without electronics or batteries.<br>• **Commercial Impact:** $895.00 MSRP add-on (77.0% GM) \| Standard on $21.4k DOT rigs. |
| **PROD_62**<br>GeoConversion Spool & Linkage Kit (CD-250) | **APPROVED & ENGINEERED.** High-flow pneumatic conversion kit enabling CD-250 to pump hydrophobic expanding polyurethanes at 8–12 GPM across 1:1 and 5:1 ratios without stalling. | • **Landed Unit COGS:** **$1,280.00** (BOM: $1,040.00 \| Shop Labor: 4.25 hrs / $240.00).<br>• **Engineering Solution:** Quick-Exhaust vortex mufflers stop $-35^\circ\text{F}$ freeze-stalls; dual 20mm linear guide rails and offset 4140 drive bridge stop 5:1 racking bind.<br>• **Commercial Impact:** Retrofit Kit: $4,950 MSRP (74.1% GM); Turnkey Rig: $24,500 MSRP (72.0% GM); unlocks $45M geotechnical slab market. |
| **PROD_68**<br>AeroShift™ Air-Logic Spool & Pilot Exchange | **APPROVED & ENGINEERED.** Modular quick-swap pneumatic reversing valve cartridge with N52 bistable magnetic snap detents; mounts to permanent sub-plate, ending creep stalls and capturing $250 core-deposit loop. | • **Landed Unit COGS:** Conversion Kit: **$281.70** (1.92 shop hrs) \| Cartridge New: **$118.20** \| Reconditioning Cost: **$33.77** (25 mins labor).<br>• **Performance:** Eliminates creep-speed dead-center stalls (shift transit <2.5 ms); 3-minute field swap.<br>• **Commercial Impact:** Kit MSRP: $1,195.00 (76.4% GM); Exchange: $425.00 (plus $250 deposit) at **86.0% blended GM**; adds **+$96.9k Rev / +$81.4k GP/yr**. |
| **PROD_94**<br>AeroShift™ FrostGuard™ De-Icing System | **APPROVED & ENGINEERED.** Integrates annular supply heat-recovery jacket, G10 Garolite thermal break, and Delrin cyclonic vortex exhaust diffuser onto AeroShift sub-plate to stop $-38^\circ\text{F}$ rime ice seizure. | • **Landed Unit COGS:** **$42.00** (Materials: $34.20 \| Shop Labor: 12 mins / $7.80) vs <$45.00 ceiling.<br>• **Thermodynamic Impact:** Maintains spool body $\ge 38^\circ\text{F}$; cuts conductive chill by 98.4%; evacuates moisture before freezing.<br>• **Commercial Impact:** $185.00 contractor list (**77.3% GM**); standard on winter DOT & GeoMaster rigs; stops rental freezing calls. |
| **PROD_74**<br>Low-Restriction Bayonet Static Mixer (Mold #6 Retool) | **APPROVED & COMMERCIALIZED.** Retools Mold #6 at Wise Plastics into direct-latching PA66-GF33 SureMix-250™ shroud; pairs with SureCore-18™ low-drag disposable mixer cartridge. Natively clicks into SureClick & OmniLatch ports. | • **Tooling Retool Capex:** **$9,600.00** at Wise Plastics (35-day payback).<br>• **Hydraulic Impact:** Slashes cold-weather head loss by **48.5 PSI** (from 96.5 to 48.0 PSI at 40°F, 3,800 cP); stops whip bursts.<br>• **Consumable Unit COGS:** **$1.16** per mixer \| List: $4.20–$5.80.<br>• **Gross Margin:** **72.4% to 80.0% GM**; captures **+$135.5k Rev / +$100.3k GP/yr**. |
| **PROD_92**<br>DeepDrive-15™ Lance & Sacrificial Tip System | **APPROVED & COMMERCIALIZED.** Modular 1/2" Schedule 80 steel drive-rod driving anvil (4140 steel) and molded polymer sacrificial knock-off tip (Mold #14) with OmniLatch lance head adapter; replaces $45/ft German lances. | • **Landed Unit COGS:** Anvil (`DD-ANVIL`): **$51.80** \| Adapter (`DD-LOK`): **$24.80** \| Sacrificial Tip (`DD-TIP-10`): **$0.88** (Mold #14 in Aurora).<br>• **Tooling Capex:** $8,800 (Mold #14); **18.6-day payback**.<br>• **Economics:** Anvil: $245.00 (78.9% GM) \| Adapter: $145.00 (82.9% GM) \| Tip: $4.95 direct (**82.2% GM**), $3.95 dist (77.7% GM).<br>• **Commercial Impact:** Slashes contractor hole cost from $675 to $4.95; captures **+$172.8k GP/yr** at 80.2% blended GM. |
| **PROD_103**<br>CleanPass-250™ End-of-Shift Flush Manifold | **APPROVED & COMMERCIALIZED.** Snap-on closed-loop flush bypass manifold with dual 5-PSI check valves and sealed drum bung adapter; enables 90-sec solvent flush into hazmat jug without wrenching fittings. | • **Landed Unit COGS:** **$38.20** (BOM: $28.40 \| Shop Labor: 17 mins / $9.80).<br>• **Performance:** 90-second closed flush; zero open spraying; compliant with EPA NPDES Clean Water standards.<br>• **Commercial Impact:** $195.00 Contractor List (**80.4% GM**); $135.00 Distributor Wholesale (71.7% GM); adds **+$47.5k Rev / +$35.8k GP/yr** and stops fleet whip seizures. |
| **PROD_104**<br>SafePurge-250™ Bio-Citrus Closed-Loop Fluid | **APPROVED & FORMULATED.** Bio-citrus/glycol ether conditioning solvent in reusable 2.5-gal pre-plumbed carboys; flash point >205°F bypasses DOT Class 3 Hazmat shipping rules and EPA waterway discharge bans. | • **Landed Unit COGS:** **$12.00** per 2.5-gal carboy (BOM: $12.00 \| Shop Labor: 0 mins via IL toll blender).<br>• **Refill COGS:** **$7.20** per refill exchange.<br>• **Economics:** $48.00 list (**75.0% GM**); $36.00 refill exchange (**80.0% GM**); $32.00 wholesale (62.5% GM).<br>• **Commercial Impact:** Captures **+$107.3k Rev / +$78.5k recurring GP/yr**; mandatory on rentals, zero shop labor burden. |
| **PROD_108**<br>RatioShift-15™ Modular Quick-Change Ratio Sleeves | **APPROVED & ENGINEERED.** Drop-in modular cylinder sleeve, radial T-slot piston, and captive hand-collar conversion kit (1:1, 2:1, 3:1) for portable CD-15 crack injection chassis. | • **Landed Unit COGS:** **$194.80** (BOM: $137.60 \| Shop Labor: 77 mins / $57.20) vs $195.00 ceiling.<br>• **Performance:** 7.5-minute field ratio changeover; zero loose nuts dropped from scaffolds; proofed to 2,500 PSI.<br>• **Economics:** $850.00 Contractor List (**77.1% GM**); $595.00 Wholesale (67.3% GM); OEM standard on $6,250 CD-15 MultiRatio Pro (+ $1,105 GP/unit).<br>• **Commercial Impact:** Captures **+$121.3k Rev / +$94.2k GP/yr** across kits and new rig margins. |
| **PROD_118**<br>Omni-Flex™ 3,500 PSI Whip Hose Workcell | **APPROVED & WORKCELL COMMISSIONED.** In-house benchtop hydraulic crimping cell pairing Omni-Cam adapters with solvent-impermeable PA12 micro-bore hose; eliminates grease gun hose chemical swelling and blowouts. | • **Landed Unit COGS:** **$17.32** (BOM: $15.50 \| Shop Labor: 3.5 mins / $1.82).<br>• **Workcell Capex:** **$3,450.00** (D105-style bench crimper + micro-bore die sets).<br>• **Economics:** $68.50 Contractor List (**74.7% GM / $51.18 GP**); $52.00 Wholesale (**66.7% GM / $34.68 GP**); $295.00 5-Pack (**70.6% GM**).<br>• **Commercial Impact:** Captures **+$69.9k Rev / +$50.8k GP/yr**; breakeven in **54 days (1.8 months)**. |
| **PROD_120**<br>DrySpear-250™ Desiccant Drum Bung Spear Kit | **APPROVED & COMMERCIALIZED.** Standardized, sealed dual-drum suction spear kit with color-indicating silica desiccant breathers; prevents atmospheric moisture crystallization of MDI Part A in drums, stopping pump feed clogs. | • **Landed Unit COGS:** **$32.00** (BOM: $27.20 \| Shop Labor: 10 mins / $4.80) vs $32.00 target.<br>• **Performance:** Strips moisture to $<5\%$ RH (dew point $<-40^\circ\text{F}$); 3-micron filtration; eliminates polyurea crust.<br>• **Economics:** $145.00 Contractor List (**77.9% GM / $113.00 GP**); $98.00 Wholesale (67.3% GM); Breather 4-Pack: $48.00 list (**82.3% GM**).<br>• **Commercial Impact:** Captures **+$75.5k Rev / +$59.4k GP/yr**; packed inside all GeoMaster rentals, ending warranty cavitation disputes. |
| **PROD_124**<br>RatioSentinel-100™ Mechanical Verification Manifold | **APPROVED & SHOP-FABRICATED.** Armored dual-buret volumetric ratio test manifold with synchronized dual 3-way SS valves; gives DOT inspectors a 60-sec visual ratio certification (1:1 to 4:1) with zero scales or cups. | • **Landed Unit COGS:** **$368.50** (BOM: $312.50 \| Direct Shop Labor: 56 mins / $56.00) vs <$450.00 ceiling.<br>• **Performance:** Instantaneous 60-sec visual check (±3% pass/fail bands); zero wind sensitivity; closed-loop drain-down stops waterway EPA spills.<br>• **Economics:** $1,385.00 Contractor List (**73.4% GM / $1,016.50 GP**); $975.00 Wholesale (62.2% GM).<br>• **Commercial Impact:** Adds **+$245.5k Rev / +$185.0k GP/yr**; specified in DOT bridge provisions, locking out uncertified competitors. |
| **PROD_128**<br>CleanPass-Seq™ Anti-Crossover Purge Sequencer | **APPROVED & SHOP-FABRICATED.** 100% pneumatic air-logic timed dual-solvent/air-blast valve block; isolates streams and executes a 3-phase purge sequence to prevent 5-second rapid-setting geotechnical polyurethanes from flash-curing in bypass manifold. | • **Landed Unit COGS:** **$88.50** (BOM: $60.90 \| Direct Shop Labor: 37 mins / $27.60).<br>• **Performance:** Complete physical stream isolation (zero common mixing chamber); automated 3-phase cycle in 20 seconds.<br>• **Economics:** $465.00 Contractor List (**81.0% GM / $376.50 GP**); $325.00 Wholesale (72.8% GM).<br>• **Commercial Impact:** Adds **+$73.0k Rev / +$57.5k GP/yr**; permanently eliminates ruined rental bypass caps and contractor chisel teardowns. |
| **PROD_130**<br>GeoWhip-Bal™ Auto-Balancing Geotechnical Wand | **APPROVED & SHOP-MACHINED.** Billet aluminum dual-feed handheld dispensing wand with cross-referenced hydro-balancing spool; eliminates unequal hydraulic head surge during 10+ GPM 1:1 and 5:1 void grouting while adding only 1.55 lbs tool weight. | • **Landed Unit COGS:** **$158.50** fully loaded (BOM: $127.00 \| Direct Shop Labor: 51 mins / $31.50) vs <$160.00 ceiling.<br>• **Performance:** Equalizes fluid delivery ($\Delta P < 8\text{ PSI}$); stops unreacted lead slugs; total wand weight 3.65 lbs (+1.55 lbs vs bare wands); full 10+ GPM Cv.<br>• **Economics:** $635.00 Contractor List (**75.0% GM / $476.50 GP**); $445.00 Wholesale (64.4% GM).<br>• **Commercial Impact:** Adds **+$110.5k Rev / +$79.6k GP/yr**; standard pack-in on rental GeoMasters, eliminating slab failure callbacks. |
| **PROD_132**<br>AeroShift™ Drop-In Air Logic Field Cartridge | **APPROVED & SHOP-MACHINED.** Pre-timed, tool-less drop-in pneumatic directional spool cartridge pairing a permanent billet sub-plate with dual 304SS over-center cam latches; resolves dirty-air proportioner drive stalls in under 45 seconds without wrenches or tube replumbing. Rebuilt in Aurora Station #2/3. | • **Landed Unit COGS:** Cartridge New: **$112.50** \| Base Kit: **$110.97** \| Recondition Cost: **$24.50** (22 mins shop labor).<br>• **Performance:** 45-second field swap; zero tools; zero line re-plumbing; eliminates $1,500-$3,500/hr DOT bridge liquidated damages.<br>• **Economics:** Retrofit Kit: $1,495.00 List (**77.5% GM**); Spare Cartridge: $545.00 List (**79.4% GM**); Rebuild Exchange: $195.00 (**87.4% GM / $170.50 GP**).<br>• **Commercial Impact:** Adds **+$121.4k Rev / +$96.9k GP/yr**; standard pack-in across rentals, permanently ending emergency bridge stall calls. |
| **PROD_134**<br>DuraBore-2M™ Autofrettaged Billet Fluid Manifold | **APPROVED & SHOP-COMMISSIONED.** Benchtop 11,200 PSI hydrostatic autofrettage pulse on 6061-T651 billet blocks via SC Hydraulic intensifier; pairs with 4140 thread-bypass isolation mandrels, inducing -17.5 ksi compressive hoop stress at cross-bores without NPT thread distortion. | • **Landed Unit COGS:** New Block: **$142.50** (28 shop mins) \| Recondition Cost: **$28.80** (14 shop mins) \| Rig Capex: **$2,450.00**.<br>• **Performance:** Dynamic fatigue life expands from 500k to **>2,500,000 cycles** (+500%); zero NPT bell-mouthing; suppresses tensile micro-crack initiation.<br>• **Economics:** New Manifold: $850.00 List (**83.2% GM**); Core Exchange: $275.00 (**89.5% GM / $246.20 GP**); OEM price uplift: +$450/rig.<br>• **Commercial Impact:** Adds **+$59.1k Rev / +$53.2k GP/yr**; workcell payback in **18 days**; completely stops rental manifold fatigue weeping. |
| **PROD_136**<br>DuraBore-10M™ Severe-Duty 17-4 PH Stainless Core | **APPROVED & CNC-ROUTED.** Pre-hardened Condition H1150 17-4 PH stainless steel billet machined on Hurco VMC for high-turn rental units and geotechnical rigs; delivers >10M cycle infinite fatigue life, immune to water-hammer spikes and silica erosion. | • **Landed Unit COGS:** New Block: **$248.50** (Raw Machining/Material: **$220.05** vs <$350 ceiling) \| Recondition Cost: **$38.50** (24 shop mins) \| Tooling Capex: **$2,130.00**.<br>• **Performance:** Dynamic fatigue life expands to **>10,000,000 cycles (Infinite)**; 5,500 PSI surge proof; zero thread stripping; eliminates OPER_133 scrap ceiling.<br>• **Economics:** New Core: $1,450.00 List (**82.9% GM / $1,201.50 GP**); Core Exchange: $395.00 (**90.3% GM / $356.50 GP**); OEM GeoMaster standard.<br>• **Commercial Impact:** Adds **+$95.4k Rev / +$89.8k GP/yr**; payback in **8.7 days**; eliminates rental manifold scrapping forever. |
| **PROD_146**<br>IsoGuard-500™ Anhydrous Isocyanate Storage Fluid | **APPROVED & FORMULATED.** Anhydrous, non-phthalate ester conditioning fluid (DOA + Mesamoll®) with PTSI/TEOF chemical moisture scavengers compounded via Elgin partner; permanently prevents MDI moisture crystallization and check valve seizing down to -45°F during winter storage. | • **Landed Unit COGS:** **$13.80 per 1-gal jug** (Raw chemical: $11.43 \| Packaging: $1.77 \| Freight: $0.60) vs <$14.00 ceiling.<br>• **Performance:** Karl Fischer moisture $<50\text{ ppm}$; pour point $-45^\circ\text{F}$; closed-cup flash $>355^\circ\text{F}$ (Non-Hazmat); stops 100% of polyurea crusting.<br>• **Economics:** 1-Gal Jug: $52.00 List (**73.5% GM / $38.20 GP**); 5-Gal Pail: $235.00 List (**75.1% GM / $176.50 GP**); Wholesale: $36.40 (62.1% GM).<br>• **Commercial Impact:** Adds **+$108.3k Rev / +$81.1k recurring GP/yr**; saves $9.6k/yr in internal rental teardowns; 6.6-day payback. |
| **PROD_150**<br>FilterPass-250™ Dual-Stream De-Grit Screen Block | **APPROVED & SHOP-MACHINED.** Monolithic hardcoat billet aluminum dual-stream in-line screen block mounting upstream of RapidSwap and RatioShift manifolds; houses removable 316SS 80-mesh cylindrical baskets with knurled service caps. | • **Landed Unit COGS:** **$64.50** (BOM: $45.20 \| Shop Machining & Labor: 28.2 mins / $19.30) vs <$65.00 ceiling.<br>• **Performance:** Captures >177 µm drum rust, sand, and unmixed filler; <2.8 PSI drop at 5 GPM; 60-sec tool-less cleanout; drops seal scoring by 82%.<br>• **Economics:** $265.00 Contractor List (**75.7% GM / $200.50 GP**); $185.00 Wholesale (65.1% GM); Basket 4-Pack: $58.00 list (**80.0% GM**).<br>• **Commercial Impact:** Adds **+$132.4k Rev / +$102.4k recurring GP/yr**; saves $11.8k/yr in internal rental wet-end teardowns; 4.5-day payback. |
| **PROD_164**<br>SureMix-Geo™ Non-Clog Blowback Static Mixer | **APPROVED & TOOLING RETOOLED.** Large-bore 24-element static mixer adapting Mold #6 bayonet interface with an integrated FKM Viton duckbill pneumatic purge port; evacuates liquid resin via 90 PSI air blast in 0.75 seconds to prevent 5:1 rapid foam from curing during 30-sec pauses. | • **Landed Unit COGS:** **$2.38** (BOM: $2.06 \| Bench Assembly & Proof: $0.24 \| Pkg/Frt: $0.08) vs <$2.40 ceiling.<br>• **Performance:** 0.75-second purge clears bore; 16.7M striations for 5:1 mix; <42 PSI drop at 8 GPM; proofed to 2,800 PSI burst.<br>• **Economics:** $11.95 Contractor List (**80.1% GM / $9.57 GP**); $7.95 Wholesale in 25-packs (70.1% GM); 40,000+ units/yr scale.<br>• **Commercial Impact:** Adds **+$481.0k Rev / +$377.3k recurring GP/yr**; $9,650 capex pays back in **9.4 days**; stops rental mixer blowout disputes. |
| **PROD_166**<br>MultiLift-4™ Balanced Multi-Point Injection Manifold | **APPROVED & SHOP-MACHINED.** Billet aluminum unpowered 2-to-4 port distribution manifold with individual silicone-damped 0-1,000 PSI gauges and 75 PSI spring-loaded 17-7 PH backpressure trim cartridges; enables simultaneous planar lifting of warehouse concrete slabs across multiple boreholes without blowouts or proportioner stalling. | • **Landed Unit COGS:** **$88.00** (BOM: $59.45 \| Hurco Machining: $10.27 \| Julian Bench Assy & Hydro Test: $8.98 \| Pkg/Frt: $6.45) vs $88.00 target.<br>• **Performance:** Equalizes flow across differential backpressures; stops 95% void short-circuit channeling; individual port isolation; proofed to 1,500 PSI.<br>• **Economics:** $385.00 Contractor List (**77.1% GM / $297.00 GP**); $265.00 Wholesale (66.8% GM); 1,200 units/yr scale.<br>• **Commercial Impact:** Adds **+$414.0k Rev / +$303.6k recurring GP/yr**; $2,100 capex pays back in **2.5 days**; eliminates warehouse slab cracking callbacks. |
| **PROD_172**<br>RatioSentinel™ Annual Factory Recertification Loop | **APPROVED & SHOP-COMMISSIONED.** Turnkey $295/yr annual factory compliance loop and Station #1 NIST-traceable calibration rig (`RS-CAL-100`); provides full teardown, ultrasonic cleaning, Viton/PTFE seal overhaul, ±0.75% volumetric verification, tamper-evident embossed DOT tags, and certified submittal documentation. | • **Landed Unit COGS:** **$38.50** (Direct Labor: 22 mins / $14.12 \| Seal Kit: $12.50 \| Tamper Tag: $3.88 \| Packaging/Cert: $8.00) vs $295.00 list.<br>• **Performance:** Verifies ratio to within ±0.75% (exceeding DOT ±3% spec); tamper-proof aircraft wire tag locks out jobsite rejection; 48-hr turnaround.<br>• **Economics:** $295.00/yr Service (**86.9% GM / $256.50 GP**); Master Rig (`RS-CAL-MASTER`): $3,850.00 list (**76.9% GM / $2,960.00 GP**).<br>• **Commercial Impact:** Adds **+$109.2k Rev / +$94.9k recurring GP/yr** at scale; station rig capex ($1,659) pays back in **6.5 recertifications (6 days)**. |