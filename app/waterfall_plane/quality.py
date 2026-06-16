def check_waterfall_quality(waterfall_id: str, data: dict) -> dict:
    warnings = []
    if data.get("hidden_seniority"):
        warnings.append("hidden_seniority_detected")
    if data.get("reserve_cosmetics"):
        warnings.append("reserve_cosmetics_detected")
    if data.get("overdistribution"):
        warnings.append("overdistribution_detected")
    return {
        "waterfall_id": waterfall_id,
        "warnings": warnings,
        "quality_score": 100 - (len(warnings) * 10)
    }
