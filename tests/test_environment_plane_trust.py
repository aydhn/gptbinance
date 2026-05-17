import pytest
from app.environment_plane.trust import BasicTrustEvaluator
from app.environment_plane.objects import create_environment_object
from app.environment_plane.enums import EnvironmentClass, TrustVerdict
from app.environment_plane.drift import record_drift
from app.environment_plane.contamination import record_contamination
from app.environment_plane.enums import ContaminationClass

def test_evaluate_trust():
    env = create_environment_object("test-env", EnvironmentClass.STAGING, "owner", "desc")
    evaluator = BasicTrustEvaluator()

    verdict = evaluator.evaluate(env)
    assert verdict.verdict == TrustVerdict.TRUSTED

    env.drifts.append(record_drift("HIGH", "desc"))
    verdict = evaluator.evaluate(env)
    assert verdict.verdict == TrustVerdict.CAUTION

    env.contaminations.append(record_contamination(ContaminationClass.SHARED_STATE, "HIGH", "all"))
    verdict = evaluator.evaluate(env)
    assert verdict.verdict == TrustVerdict.BLOCKED
