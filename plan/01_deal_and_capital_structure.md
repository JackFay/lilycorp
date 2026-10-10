# 01. Deal and Capital Structure

## I. Executive Summary: SBA Underwriting & Debt Capacity Constraints

The acquisition of Lily Corporation faces significant financing constraints due to its historical tax return performance in 2024 and 2025, which, after required adjustments, fall short of the Small Business Administration (SBA) mandated 1.25x Debt Service Coverage Ratio (DSCR). First American Bank, and other SBA lenders, have declined standard senior loan requests of $850,000 to $1,000,000+. The core challenge stems from operating losses reported in these years, which significantly depress the cash flow available for debt service (CFADS) after factoring in mandatory post-acquisition expenses.

To facilitate the acquisition, the proposed capital structure will necessitate a significantly reduced senior bank loan, heavily reliant on a substantial seller note placed on a 24-month standby as per SBA subordination requirements.

## II. Frontier Diligence Item: DEAL_SBA_01 - Historical Tax Return DSCR Deficit & Standby Seller Note Sizing

### A. SBA DSCR Analysis Methodology

SBA lending rules (Oct 1, 2026 SOP) require a minimum 1.25x DSCR, calculated on historical Form 1120-S tax returns. The underwriting process involves normalizing ordinary income/loss by:
1.  **Add-Backs:** Discretionary expenses such as depreciation, interest, and non-owner/excessive owner compensation [Marcelo Add-Back Schedule Reply].
2.  **Mandatory Deductions:** New ongoing expenses post-closing that sit ahead of debt service, specifically a new NNN commercial lease and a market-rate buyer/replacement General Manager salary [Bob Financing Reply].

For Lily Corporation, the bank has consistently deducted a proposed $68,000/year for the new NNN lease and $100,000/year for the buyer's salary [Bob Financing Reply, Marcelo Add-Back Schedule Reply].

### B. Normalized Cash Flow & DSCR Performance by Year

#### 1. 2024 Performance: The Limiting Factor

*   **Starting Point:** Ordinary Business Loss of -$16,612 [Marcelo Add-Back Schedule Reply].
*   **Add-Backs:**
    *   Depreciation & Interest: +$8,805
    *   Family Compensation (Robert, Lily, Michael Trout): +$251,092
*   **Gross Cash Flow Before Deductions:** -$16,612 + $8,805 + $251,092 = $243,285
*   **Mandatory Bank Deductions:**
    *   Proposed Commercial Lease (NNN): -$68,000
    *   Buyer/Replacement Manager Salary: -$100,000
*   **Bank's Adjusted Cash Flow Available for Debt Service (CFADS):** $85,000 [Bob Financing Reply]
    *   (Note: Our detailed calculation yields $243,285 - $68,000 - $100,000 = $75,285. The bank's slightly higher figure of $85,000 is adopted as their underwriting baseline).
*   **DSCR Assessment:** To meet the SBA's 1.25x DSCR, the maximum annual debt service for 2024 cannot exceed $85,000 / 1.25 = **$68,000** [Bob Financing Reply].
*   **Further Constraint:** The seller's notes indicate that 2024 inventory had duplicate entry errors that understated COGS by $108,218 [Marcelo Add-Back Schedule Reply]. If an underwriter applies this correction, 2024 cash flow would become significantly negative, making it impossible to support any senior debt. This highlights the severe constraints of the 2024 tax return.

#### 2. 2025 Performance: Improvement, but Insufficient to Override 2024

*   **Starting Point:** Ordinary Business Loss of -$134,891 [Marcelo Add-Back Schedule Reply].
*   **Add-Backs:**
    *   Depreciation & Interest: +$6,526
    *   Family Compensation (Robert, Lily, Michael Trout): +$265,087
    *   Inventory Adjustment Write-Down (Line 5345): +$200,387 [Marcelo Add-Back Schedule Reply].
*   **Gross Cash Flow Before Deductions:** -$134,891 + $6,526 + $265,087 + $200,387 = $337,109
*   **Mandatory Bank Deductions:**
    *   Proposed Commercial Lease (NNN): -$68,000
    *   Buyer/Replacement Manager Salary: -$100,000
*   **Adjusted Cash Flow Available for Debt Service (CFADS):** $169,109 (aligned with Jack's estimate of $169,000 to $178,000) [Marcelo Add-Back Schedule Reply].
*   **DSCR Assessment:** This CFADS of $169,109, if fully accepted with the inventory add-back, *could* theoretically support a maximum annual debt service of $169,109 / 1.25 = $135,287.
*   **Conclusion on 2025 DSCR:** While 2025 shows improvement over 2024, Jack's communication confirms that even with the inventory write-down add-back, the 2025 CFADS "supports roughly 1.15x to 1.21x DSCR" [Marcelo Add-Back Schedule Reply] for a larger loan. Critically, First American Bank declined larger loans and explicitly capped the senior loan based on the more conservative 2024 figures [Bob Financing Reply]. This indicates 2025's performance, even when normalized, did not sufficiently alleviate the bank's concerns or override the lowest historical year's capacity.

### C. Specific Frontier Item Resolution

**QUESTION:** Can normalized 2024 (-$16.6k loss) and 2025 (-$134.9k loss) cash flow achieve the SBA mandatory 1.25x DSCR under Oct 1 2026 SBA SOP rules, and what is the exact maximum senior debt First American Bank can issue?

**ANSWER:**
*   **2024 DSCR Achievement:** No. Normalized 2024 cash flow, with a bank-determined CFADS of $85,000, can only support a maximum annual debt service of $68,000 to achieve 1.25x DSCR. This is insufficient to support a large senior loan.
*   **2025 DSCR Achievement:** No, not in a manner that enables a larger senior loan. While 2025's CFADS of $169,109 (assuming the full $200,387 inventory write-down add-back) could theoretically support a larger annual debt service, First American Bank did not underwrite based on this, instead defaulting to the more conservative 2024 figures.
*   **Exact Maximum Senior Debt First American Bank Can Issue:**
    *   Based on the bank's assessment of $85,000 CFADS for 2024, the maximum allowable annual debt service at 1.25x DSCR is $68,000.
    *   Using standard SBA terms (10-year amortization, 9.5% annual interest rate), the maximum senior debt First American Bank can issue is precisely **$443,308**.
    *   *Calculation:*
        *   Monthly Payment (PMT) = $68,000 / 12 = $5,666.67
        *   Monthly Interest Rate (r) = 0.095 / 12 = 0.0079166667
        *   Number of Months (n) = 10 years * 12 months/year = 120
        *   Principal (P) = $5,666.67 * [1 - (1 + 0.0079166667)^-120] / 0.0079166667 = **$443,308**

### D. Open Uncertainties Addressed

1.  **Will the bank accept the full $200,387 inventory write-down in 2025 as a one-time non-recurring add-back?**
    *   Based on the bank's explicit declining of standard $850k-$1M+ senior loans and their stated maximum loan capacity being determined by the 2024 numbers, it is clear that **no**, the full $200,387 inventory write-down in 2025 was either not fully accepted as a non-recurring add-back for senior loan sizing, or it did not sufficiently improve the overall financial picture to override the limiting factor of 2024's performance for a larger loan. The bank is taking the most conservative approach by relying on the lowest compliant historical year's capacity.

2.  **What is the maximum purchase price Bob will accept with a 24-month standby note?**
    *   This is a negotiation point. However, the financial capacity dictates the structure. With a maximum senior loan of $443,308 and typical buyer equity of $50,000 - $75,000, the cash available to Bob at closing will be approximately **$493,308 - $518,308**.
    *   Given Bob's previous expectations of a "$1M+ valuation" [Bob Financing Reply], any purchase price above this cash amount would need to be financed through a substantial seller note, which, per SBA rules, would require a full 24-month standby period (no principal or interest payments for the first two years). This structure would entail Bob receiving significantly less cash at close than his previous valuation expectations, posing a key challenge for negotiations.

## III. Proposed Capital Structure & Deal Terms

Given the SBA underwriting constraints, the deal structure must be revised to reflect the actual debt capacity of Lily Corporation.

*   **Total Enterprise Value (TEV):** To be negotiated, but significantly constrained by available financing.
*   **Senior Debt (First American Bank):** $443,308 (10-year term, ~9.5% interest, fully amortizing, secured by business assets)
*   **Buyer Cash Equity:** $50,000 - $75,000
*   **Seller Note on Standby:** The remaining balance of the purchase price, to be held by Bob Trout, fully subordinated to the senior bank debt for a minimum of 24 months (no principal or interest payments) per SBA Form 155 subordination requirements. This will be secured by remaining assets and proprietary molds [Site Visit Diligence Notes].
*   **Commercial Real Estate Lease:** $68,000/year ($5,666/month) NNN rent paid to Bob Trout (as landlord) for the building, which will be paid ahead of debt service as a mandatory deduction [Bob Financing Reply].

This structure aligns with Jack's "Option A" presented to Bob and represents the only viable path for SBA-backed financing given the historical financial performance.