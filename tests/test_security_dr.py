from app.security.dr import DisasterRecoveryManager


def test_dr_plan():
    drm = DisasterRecoveryManager()
    plan = drm.generate_plan("State Corruption")
    assert plan.scenario == "State Corruption"
    assert len(plan.steps) > 0
