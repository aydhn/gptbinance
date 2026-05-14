def export_research_evidence(research_id: str):
    return {
        "research_id": research_id,
        "value_hypotheses_ref": "vh_1",
        "optionality_claims_ref": "opt_1",
        "cost_of_delay_inputs_ref": "cod_in_1",
        "status": "decision_linked" # Descriptive without linkage gives caveat
    }
