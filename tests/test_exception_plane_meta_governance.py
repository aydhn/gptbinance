import pytest
from app.exception_plane.meta_governance import MetaGovernanceLinkageEvaluator
from app.exception_plane.models import ExceptionObject, ExceptionClass

def test_meta_governance_linkage_evaluator():
    evaluator = MetaGovernanceLinkageEvaluator()
    obj = ExceptionObject(exception_id="EX-100", exception_class=ExceptionClass.POLICY_WAIVER, owner="system", scope="global", deviation_posture="bounded", expiry_posture="enforced")
    res = evaluator.evaluate_linkage(obj)
    assert res.exception_id == "EX-100"
    assert res.is_meta_governance_safe == True
