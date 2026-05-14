def check_value_quality(value_object, objectives, benefits, baselines, attribution, tradeoffs):
    # Dummy implementation for tests/CLI
    warnings = []
    if not baselines:
        warnings.append("baseline_missing")
    if not tradeoffs:
        warnings.append("tradeoff_missing")
    if not attribution:
        warnings.append("attribution_missing")
    return {"status": "ok" if not warnings else "degraded", "warnings": warnings}
