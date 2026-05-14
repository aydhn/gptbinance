# Cost plane evaluation integration
def issue_cheaper_riskier_tradeoff(cheaper_but_riskier: bool):
    if cheaper_but_riskier:
        return {"trade_off_notes": "Cheaper but riskier option"}
    return {}
