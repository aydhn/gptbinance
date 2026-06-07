import pytest
from app.exception_plane.scenario import ScenarioLinkageEvaluator
from app.exception_plane.models import ExceptionObject, ExceptionClass

def test_scenario_linkage_evaluator():
    evaluator = ScenarioLinkageEvaluator()
    obj = ExceptionObject(exception_id="EX-100", exception_class=ExceptionClass.POLICY_WAIVER, owner="system", scope="global", deviation_posture="bounded", expiry_posture="enforced")
    res = evaluator.evaluate_linkage(obj)
    assert res.exception_id == "EX-100"
    assert res.is_scenario_safe == True
