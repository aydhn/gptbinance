import pytest
from app.exception_plane.accountability import AccountabilityLinkageEvaluator
from app.exception_plane.models import ExceptionObject, ExceptionClass

def test_accountability_linkage_evaluator():
    evaluator = AccountabilityLinkageEvaluator()
    obj = ExceptionObject(exception_id="EX-100", exception_class=ExceptionClass.POLICY_WAIVER, owner="system", scope="global", deviation_posture="bounded", expiry_posture="enforced")
    res = evaluator.evaluate_linkage(obj)
    assert res.exception_id == "EX-100"
    assert res.is_accountability_safe == True
