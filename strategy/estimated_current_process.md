# Lily Corp: Estimated Current ("AS-IS") Order Process

> **Diligence Note:** This workflow is an **operational reconstruction** reverse-engineered from Lily Corp’s employee job descriptions, financial notes, QuickBooks Desktop exports, and standard 1980s industrial manufacturing practices.  
> **Critical Finding:** Lily Corp currently has **no formal written Standard Operating Procedures (SOPs)**. The entire order fulfillment lifecycle currently runs on unwritten tribal knowledge across 5 employees.

---

## 1. The 7-Step Order Lifecycle

```
[1. Inbound Request] ──► [2. Quoting] ──► [3. Manual QB Entry] ──► [4. Paper Handoff]
Phone, Email, or Fax     Bob / Dave J     Maggie / Dave J          Office to Shop
                                                                         │
[7. Billing & AR]    ◄── [6. Shipping] ◄── [5. Pick & Pack]   ◄────────┘
Maggie M                 UPS WorldShip     Dave K / Julian
```

### Step 1: Inbound Customer Request (Unstructured & Fragmented)
* **Channels:**
  * Phone calls to the main Aurora office landline (8:00 AM – 4:30 PM CST).
  * Direct emails to individual inboxes (`rtrout@lilycorp.com`, Dave J, or Maggie).
  * Faxed or emailed PDF Purchase Orders from contractor purchasing departments.
* **Friction:** No central ticketing system, shared inbox, or CRM. If Bob is traveling or leading an educational seminar, emails sent to him sit unaddressed.

### Step 2: Quoting & Pricing
* **Standard Consumables (Mixers, Ports, Fittings):**
  * Handled by Dave J or Maggie.
  * Pricing is looked up manually from historical QuickBooks invoices or printed contractor price sheets.
* **Capital Equipment, Custom Dispensers & Rentals:**
  * Exclusively handled by **Bob Trout** (or Dave J).
  * Requires custom calculation of pressure ratios, hose lengths, and motor specs.
  * Quotes are typed into Word/Excel/QuickBooks and emailed or faxed back to the customer.

### Step 3: Order Entry & Payment (QuickBooks Desktop)
* **Manual Data Entry:** Maggie or Dave J manually keys customer name, jobsite shipping address, PO number, and part numbers into **QuickBooks Desktop** (hosted locally on an office PC).
* **Payment Processing:**
  * **Credit Card:** Maggie takes the 16-digit card number over the phone or off an authorization form and manually runs it through an external merchant terminal or QuickBooks Merchant portal.
  * **Net-30 Terms:** Marked on open account based on historical customer relationship.

### Step 4: The Physical Paper Handoff (Office to Shop Floor)
* Maggie prints a physical paper **Sales Order / Pick Ticket** on an office printer.
* The paper ticket is physically walked from the front office into the back shop and placed in a wire inbox, clip, or tray at **Dave K’s** or **Julian’s** workbench.

### Step 5: Warehouse Picking, Assembly & Fulfillment
* **Stock Parts:** Dave K or Julian walks the shelf aisles to pull parts from bins. **There are no barcodes or digital scanners**—picking relies entirely on visual recognition and tribal memory.
* **Equipment Assembly & Rentals:** Julian or Greg builds the pump/dispenser, conducts bench pressure testing, or preps a rental unit from the fleet.
* **Stockouts:** Because QuickBooks inventory isn't live on the floor, stockouts are only discovered when someone looks into an empty bin. Dave K must then verbally notify the office, initiate a vendor PO, or start the injection mold machine.  
  *(Note: This manual PO/receiving gap caused the $108,218 duplicate inventory entry error in 2024).*

### Step 6: Shipping & Label Generation (Standalone Terminal)
* Once packed or crated, the package is moved to a shipping station running a standalone **UPS WorldShip** or FedEx Ship Manager application.
* **Second Data Re-entry:** Dave K or Julian manually re-types the recipient address, contact name, and customer PO number into the UPS computer.
* The shipping label is applied, and the paper pick ticket—with a handwritten UPS tracking number—is walked back to Maggie’s desk.

### Step 7: Post-Ship Billing & Invoicing (Maggie)
* Maggie pulls up the sales order in QuickBooks Desktop, marks it fulfilled, manually enters the actual UPS freight charge (Line 5340 Freight Out), and converts it to an Invoice.
* She emails or USPS-mails the invoice to the customer’s AP department.
* If a customer calls asking for tracking, the front office must walk to the back to check physical clipboards or look up WorldShip logs manually.

---

## 2. Personnel Responsibility Matrix

| Employee | Title / Primary Role | Touchpoint in the Order Lifecycle |
| :--- | :--- | :--- |
| **Bob Trout** | President | Takes phone orders; calculates custom equipment/rental quotes; handles key account relationships. |
| **Dave J** | Sales, IT, Technical Support | Handles customer tech inquiries; quotes standard & custom orders; enters orders into QuickBooks. |
| **Maggie M** | Office Manager | Order entry into QuickBooks; credit card processing; prints pick tickets; sends invoices; manages AR collections. |
| **Dave K** | Shipping/Receiving & Purchasing | Receives paper pick tickets; pulls parts; packs boxes; types labels in UPS WorldShip; alerts on stockouts. |
| **Julian P** | New Equipment Assembly | Builds new equipment orders; benches tests; assists with packing and crate preparation. |
| **Greg E** | Maintenance & Rentals | Preps and tests rental equipment; runs mold machine to restock molded plastic parts. |

---

## 3. Core Friction Points & Vulnerabilities

1. **Triple Data Entry:** Order information is manually keyed three separate times:
   $$\text{Customer Email/PO} \longrightarrow \text{QuickBooks Desktop} \longrightarrow \text{UPS WorldShip}$$
2. **Key-Man Bottleneck:** Equipment sales, custom quotes, and seminar-driven orders freeze if Bob is out of the office.
3. **Office vs. Shop Floor Blindspot:** No live inventory synchronization. Front-desk staff cannot tell a customer with 100% certainty if an item is in stock without walking into the warehouse.
4. **Restricted Ordering Window:** Zero self-service. Contractors starting jobsites at 6:00 AM CST cannot place an order or check order status until the office opens at 8:00 AM.
5. **Human Error Surface:** Verbal phone orders and handwritten paper notes create frequent part number mismatches, wrong fitting sizes, and dispute risks.

---

## 4. Due Diligence Questions for Site Visit (Bob & Maggie)

Use these targeted questions during your on-site walkthrough to confirm the actual mechanics:

1. *"When a customer calls or emails to order 500 ports or a rental rig, what are the exact steps to get that into the system?"*
2. *"Can you show me the physical handoff between the front office and Dave K in the warehouse?"*
3. *"How does Dave K know what to pull from the shelves—do you use printed pick lists or verbal orders?"*
4. *"How do tracking numbers get from the shipping computer back into QuickBooks and out to the customer?"*
5. *"How do you handle credit cards—are numbers stored on file, re-entered each time, or run through QuickBooks Merchant?"*
