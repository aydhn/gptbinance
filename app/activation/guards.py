from app.capacity_plane.trust import evaluate_capacity_trust
def check_activation_capacity_guard():
    trust = evaluate_capacity_trust()
    if trust.verdict.value == "blocked":
        return {"status": "BLOCKED"}
    return {"status": "PASSED"}
