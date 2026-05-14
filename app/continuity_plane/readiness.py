def evaluate_continuity_readiness(cont_id: str):
    return {
        "cont_id": cont_id,
        "avoided_downtime_value_ref": "avoid_down_1",
        "cost_of_delay_avoided_ref": "cod_av_1",
        "optionality_gain_ref": "opt_gain_1",
        "status": "value_thesis_present" # Spend without thesis gives caution
    }
