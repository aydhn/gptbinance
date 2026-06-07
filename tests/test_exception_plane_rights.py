import pytest
from app.exception_plane.rights import RightsLinkageEvaluator
from app.exception_plane.models import ExceptionObject, ExceptionClass

def test_rights_linkage_evaluator():
    evaluator = RightsLinkageEvaluator()
    obj = ExceptionObject(exception_id="EX-100", exception_class=ExceptionClass.POLICY_WAIVER, owner="system", scope="global", deviation_posture="bounded", expiry_posture="enforced")
    res = evaluator.evaluate_linkage(obj)
    assert res.exception_id == "EX-100"
    assert res.is_rights_safe == True
