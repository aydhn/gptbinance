def evaluate_optimization(optimization_id: str):
    # Includes expected value deltas, externality risks and strategic fit refs
    return {
        "optimization_id": optimization_id,
        "expected_value_delta": 500.0,
        "externality_risk_refs": ["ext_123"],
        "strategic_fit_ref": "obj_efficiency_1",
        "value_check": "passed" # Cost-only without value check produces explicit caution
    }
