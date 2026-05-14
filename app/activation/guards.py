def check_activation_guards(activation_id: str):
    # Requires explicit value objective, acceptable downside and stop-value-loss criteria
    return {
        "activation_id": activation_id,
        "value_objective_ref": "obj_growth_2",
        "acceptable_downside_ref": "trd_downside_1",
        "stop_value_loss_criteria": "var_loss_threshold",
        "trust_verdict": "trusted" # Produces blocker/caution semantics without these
    }
