def check_quality(settlement_id: str, factors: dict):
    warnings = []
    if factors.get("overrelease"):
        warnings.append("overrelease warning")
    if factors.get("theater"):
        warnings.append("settlement theater warning")
    return {"settlement_id": settlement_id, "quality_warnings": warnings}
