def check_release_operating_model(release_candidate):
    if not release_candidate.get("accountable_chain"):
        return {"status": "BLOCKED", "reason": "No accountable operator chain for release."}
    if not release_candidate.get("reviewer_independence"):
        return {"status": "CAUTION", "reason": "Release under broken reviewer independence."}
    return {"status": "READY"}
