import pytest
from app.exception_plane.epistemic import EpistemicLinkageEvaluator
from app.exception_plane.models import ExceptionObject, ExceptionClass

def test_epistemic_linkage_evaluator():
    evaluator = EpistemicLinkageEvaluator()
    obj = ExceptionObject(exception_id="EX-100", exception_class=ExceptionClass.POLICY_WAIVER, owner="system", scope="global", deviation_posture="bounded", expiry_posture="enforced")
    res = evaluator.evaluate_linkage(obj)
    assert res.exception_id == "EX-100"
    assert res.is_epistemic_safe == True
