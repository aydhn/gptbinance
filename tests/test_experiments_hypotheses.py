import pytest
from app.experiments.hypotheses import HypothesisRegistry, FindingToHypothesisCompiler
from app.experiments.enums import HypothesisClass
from app.experiments.exceptions import InvalidHypothesisError


def test_hypothesis_registry_and_compiler():
    registry = HypothesisRegistry()
    compiler = FindingToHypothesisCompiler()

    finding = {"finding_id": "f_001", "summary": "friction issue", "domain": "policy"}
    h = compiler.compile(
        finding, HypothesisClass.POLICY_FRICTION_EXCESSIVE_IN_REGIME, "test rationale"
    )
    h_id = registry.register(h)

    fetched = registry.get(h_id)
    assert fetched.h_class == HypothesisClass.POLICY_FRICTION_EXCESSIVE_IN_REGIME
    assert len(fetched.affected_domains) == 1

    with pytest.raises(InvalidHypothesisError):
        registry.get("nonexistent")
