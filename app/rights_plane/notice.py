# Rights Plane Integration
def verify_meaningful_notice(representation_id: str, registry, trust_engine):
    rep = registry.get(representation_id)
    if not rep:
        return {"status": "blocked", "reason": "No representation found"}
    verdict = trust_engine.evaluate(rep, [], [], [])
    if verdict.verdict in ["blocked", "caution"]:
        return {"status": "caution", "reason": "Meaningful notice right not satisfied due to representation defects."}
    return {"status": "trusted", "reason": "Notice satisfied"}
