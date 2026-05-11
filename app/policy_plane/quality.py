def assess_policy_quality(policy) -> dict:
    warnings = []
    if not policy.rules:
        warnings.append("No rules defined")
    return {"warnings": warnings, "quality": "good" if not warnings else "poor"}
