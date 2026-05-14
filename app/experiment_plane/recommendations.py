def generate_experiment_recommendation(experiment_id: str):
    return {
        "experiment_id": experiment_id,
        "winner_uplift_ref": "uplift_1",
        "loser_learning_value_ref": "learn_1",
        "counterfactual_baseline_ref": "cf_base_1",
        "status": "validated" # Winner claim without realized incremental value evidence gives caution
    }
