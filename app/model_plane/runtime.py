def evaluate_model_runtime(model_id: str):
    return {
        "model_id": model_id,
        "realized_inference_value_ref": "inf_val_1",
        "cost_per_inference_ref": "cpi_1",
        "latency_benefit_ref": "lat_ben_1",
        "risk_adjusted_uplift_ref": "rau_1",
        "status": "net_value_positive" # Lower latency but worse net value gives caution
    }
