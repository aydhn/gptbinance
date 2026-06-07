import pytest
from app.exception_plane.drift_integration import DriftIntegrationLinkageEvaluator
from app.exception_plane.models import ExceptionObject, ExceptionClass

def test_drift_integration_linkage_evaluator():
    evaluator = DriftIntegrationLinkageEvaluator()
    obj = ExceptionObject(exception_id="EX-100", exception_class=ExceptionClass.POLICY_WAIVER, owner="system", scope="global", deviation_posture="bounded", expiry_posture="enforced")
    res = evaluator.evaluate_linkage(obj)
    assert res.exception_id == "EX-100"
    assert res.is_drift_integration_safe == True
