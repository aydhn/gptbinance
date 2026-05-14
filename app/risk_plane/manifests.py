def generate_risk_manifest(risk_id: str):
    return {
        "risk_id": risk_id,
        "avoided_loss_ref": "al_1",
        "drawdown_reduction_ref": "dr_1",
        "exposure_reduction_ref": "er_1",
        "status": "business_relevant" # Raw risk reduction without relevance gives caution
    }
