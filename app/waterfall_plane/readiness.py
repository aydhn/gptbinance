def assess_waterfall_readiness(waterfall_id: str, metrics: dict) -> dict:
    return {
        "waterfall_id": waterfall_id,
        "is_ready": metrics.get("is_ready", False),
        "issues": metrics.get("issues", [])
    }
