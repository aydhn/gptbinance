import pytest
from app.exception_plane.sunset import SunsetLinkageEvaluator
from app.exception_plane.models import ExceptionObject, ExceptionClass

def test_sunset_linkage_evaluator():
    evaluator = SunsetLinkageEvaluator()
    obj = ExceptionObject(exception_id="EX-100", exception_class=ExceptionClass.POLICY_WAIVER, owner="system", scope="global", deviation_posture="bounded", expiry_posture="enforced")
    res = evaluator.evaluate_linkage(obj)
    assert res.exception_id == "EX-100"
    assert res.is_sunset_safe == True
