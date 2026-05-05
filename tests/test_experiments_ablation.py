from app.experiments.ablation import AblationManager


def test_ablation_manager():
    mgr = AblationManager()
    plan = mgr.create_plan("plan_1", ["risk_filter_A", "event_overlay_B"])
    assert "risk_filter_A" in plan.target_components
    assert plan.disable_methods["risk_filter_A"] == "disable_risk_filter_A"
