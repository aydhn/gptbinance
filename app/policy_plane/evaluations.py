def evaluate_high_risk_action(action_id: str, interpretation_registry) -> dict:
    obj = interpretation_registry.get(action_id)
    if not obj:
        return {"status": "DENY", "reason": "Missing interpretation evidence for high-risk action"}

    trust = obj.get_trust_report()
    if trust.verdict.name == 'BLOCKED':
        return {"status": "DENY", "reason": "Unresolved Material Ambiguity in governing texts"}

    return {"status": "ALLOW"}
