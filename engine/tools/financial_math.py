"""
Financial calculation and underwriting engine for Lily Corp acquisition.
Executes deterministic financial math for DSCR, SDE, and loan sizing.
"""

from typing import Dict, Any, List


def calculate_loan_payment(principal: float, annual_interest_rate: float, years: int = 10) -> Dict[str, float]:
    """Calculate monthly and annual debt service on fully amortizing loan."""
    if principal <= 0:
        return {"monthly_payment": 0.0, "annual_payment": 0.0, "total_interest": 0.0}
    r = annual_interest_rate / 12.0
    n = years * 12
    monthly = principal * (r * ((1 + r) ** n)) / (((1 + r) ** n) - 1)
    annual = monthly * 12
    total_paid = monthly * n
    total_interest = total_paid - principal
    return {
        "principal": principal,
        "rate": annual_interest_rate,
        "years": years,
        "monthly_payment": round(monthly, 2),
        "annual_payment": round(annual, 2),
        "total_interest": round(total_interest, 2)
    }


def calculate_dscr(cfads: float, annual_debt_service: float) -> float:
    """Calculate Debt Service Coverage Ratio (DSCR)."""
    if annual_debt_service <= 0:
        return 999.0
    return round(cfads / annual_debt_service, 2)


def evaluate_underwriting_scenario(
    purchase_price: float,
    equity_down: float,
    sba_senior_loan: float,
    sba_interest_rate: float,
    seller_note: float,
    seller_note_standby_months: int,
    seller_note_interest_rate: float,
    seller_note_term_years: int,
    nnn_lease_annual: float,
    buyer_salary_annual: float,
    base_year_loss: float,
    depreciation_interest: float,
    officer_addbacks: float,
    inventory_writedown_addback: float = 0.0
) -> Dict[str, Any]:
    """
    Computes post-closing Cash Flow Available for Debt Service (CFADS) and DSCR
    under SBA Oct 1 2026 guidelines.
    """
    # Gross unadjusted cash flow from tax return base
    gross_cash_flow = base_year_loss + depreciation_interest + officer_addbacks + inventory_writedown_addback

    # Mandatory SBA Deductions
    cfads = gross_cash_flow - nnn_lease_annual - buyer_salary_annual

    # Senior SBA debt service
    sba_debt = calculate_loan_payment(sba_senior_loan, sba_interest_rate, years=10)

    # Seller note debt service (if on standby for >= 24 mos, annual debt service in Year 1-2 is $0)
    if seller_note_standby_months >= 24:
        seller_debt = {"monthly_payment": 0.0, "annual_payment": 0.0}
    else:
        seller_debt = calculate_loan_payment(seller_note, seller_note_interest_rate, years=seller_note_term_years)

    total_annual_debt_service = sba_debt["annual_payment"] + seller_debt["annual_payment"]
    dscr = calculate_dscr(cfads, total_annual_debt_service)

    net_cash_flow = cfads - total_annual_debt_service

    return {
        "purchase_price": purchase_price,
        "sba_senior_loan": sba_senior_loan,
        "sba_annual_debt_service": sba_debt["annual_payment"],
        "seller_note": seller_note,
        "seller_note_annual_debt_service": seller_debt["annual_payment"],
        "total_annual_debt_service": total_annual_debt_service,
        "cfads": round(cfads, 2),
        "dscr": dscr,
        "dscr_passes_sba_1_25": dscr >= 1.25,
        "net_annual_cash_flow": round(net_cash_flow, 2),
        "net_monthly_cash_flow": round(net_cash_flow / 12.0, 2)
    }


def breakeven_analysis(fixed_costs: float, variable_cost_pct: float) -> Dict[str, float]:
    """
    Calculates revenue required to cover fixed overhead and debt service
    given variable COGS rate.
    """
    contribution_margin = 1.0 - variable_cost_pct
    if contribution_margin <= 0:
        return {"breakeven_revenue": 0.0, "safety_margin_pct": 0.0}
    breakeven = fixed_costs / contribution_margin
    return {
        "variable_cost_pct": round(variable_cost_pct * 100, 1),
        "contribution_margin_pct": round(contribution_margin * 100, 1),
        "fixed_costs": round(fixed_costs, 2),
        "breakeven_revenue": round(breakeven, 2)
    }


if __name__ == "__main__":
    print("--- 2024 Underwriting Baseline ---")
    scenario_2024 = evaluate_underwriting_scenario(
        purchase_price=1250000,
        equity_down=125000,
        sba_senior_loan=500000,
        sba_interest_rate=0.095,
        seller_note=625000,
        seller_note_standby_months=24,
        seller_note_interest_rate=0.07,
        seller_note_term_years=10,
        nnn_lease_annual=68000,
        buyer_salary_annual=100000,
        base_year_loss=-16612,
        depreciation_interest=8805,
        officer_addbacks=251092,
        inventory_writedown_addback=0.0
    )
    for k, v in scenario_2024.items():
        print(f"  {k}: {v}")

    print("\n--- 2025 Underwriting Baseline (With $200k Inv Add-Back) ---")
    scenario_2025 = evaluate_underwriting_scenario(
        purchase_price=1250000,
        equity_down=125000,
        sba_senior_loan=500000,
        sba_interest_rate=0.095,
        seller_note=625000,
        seller_note_standby_months=24,
        seller_note_interest_rate=0.07,
        seller_note_term_years=10,
        nnn_lease_annual=68000,
        buyer_salary_annual=100000,
        base_year_loss=-134891,
        depreciation_interest=6526,
        officer_addbacks=265087,
        inventory_writedown_addback=200387
    )
    for k, v in scenario_2025.items():
        print(f"  {k}: {v}")
