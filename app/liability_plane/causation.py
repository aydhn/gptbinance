# Liability Plane Integration
def evaluate_misrepresentation_exposure(representation_id: str, registry, trust_engine):
    rep = registry.get(representation_id)
    if not rep:
        return {"exposure": "unknown"}
    verdict = trust_engine.evaluate(rep, [], [], [])
    if "Disclaimer laundering detected" in verdict.blockers:
        return {"exposure": "high", "reason": "Disclaimer laundering cannot erase misrepresentation liability."}
    return {"exposure": "low"}
