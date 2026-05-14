def evaluate_allocation_intent(intent_id: str):
    return {
        "intent_id": intent_id,
        "expected_value_ref": "exp_val_1",
        "opportunity_cost_delta_ref": "ocd_1",
        "capital_efficiency_delta_ref": "ced_1",
        "status": "baseline_supported" # Allocation without portfolio-value baseline gives caution
    }
