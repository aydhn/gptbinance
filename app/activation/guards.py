from app.capacity_plane.trust import evaluate_capacity_trust
def check_activation_capacity_guard():
    trust = evaluate_capacity_trust()
    if trust.verdict.value == "blocked":
        return {"status": "BLOCKED"}
    return {"status": "PASSED"}



# Cost plane evaluation integration
def verify_activation_budget(budget_headroom_ok: bool, sustainable_ue: bool):
    if not budget_headroom_ok or not sustainable_ue:
         return "blocked"
    return "pass"
