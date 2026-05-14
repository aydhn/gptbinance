def evaluate_security_readiness(sec_id: str):
    return {
        "sec_id": sec_id,
        "protective_value_ref": "prot_val_1",
        "avoided_loss_estimates_ref": "al_est_1",
        "hardening_trade_off_refs": ["trd_hard_1"],
        "status": "threat_value_related" # Costly hardening without threat-value relation gives caution
    }
