import pytest
from app.decision_quality_plane.enums import DecisionClass, OptionClass, ConfidenceClass, TrustVerdict
from app.decision_quality_plane.models import (
    DecisionDefinition, OptionRecord, RationaleRecord, ConfidenceRecord,
    DecisionManifest, PremortemRecord, DecisionOutcomeRecord, OutcomeClass, CounterfactualReviewRecord,
    CalibrationRecord, CalibrationClass
)
from app.decision_quality_plane.registry import CanonicalDecisionRegistry
from app.decision_quality_plane.exceptions import InvalidOptionSetError, InvalidDecisionDefinitionError
from app.decision_quality_plane.trust import TrustVerdictEngine
from app.decision_quality_plane.quality import DecisionQualityChecker
from app.decision_quality_plane.repository import DecisionRepository
from app.decision_quality_plane.manifests import DecisionManifestBuilder

def test_decision_registry():
    registry = CanonicalDecisionRegistry()
    dec = DecisionDefinition(decision_id="D-101", decision_class=DecisionClass.RELEASE_ROLLOUT, owner="Alice", intent="Promote v2")
    registry.register(dec)
    assert registry.get("D-101").owner == "Alice"
    with pytest.raises(InvalidDecisionDefinitionError):
        registry.register(DecisionDefinition(decision_id="", decision_class=DecisionClass.RELEASE_ROLLOUT, owner="A", intent="B"))

def test_option_completeness():
    manifest = DecisionManifest(decision=DecisionDefinition(decision_id="D-1", decision_class=DecisionClass.FAILOVER, owner="B", intent="C"))
    manifest.options.append(OptionRecord(option_id="O-1", option_class=OptionClass.AGGRESSIVE, description="Rollout now", reversibility="Hard", blast_radius="High"))

    engine = TrustVerdictEngine()
    verdict = engine.evaluate(manifest)
    assert verdict.verdict == TrustVerdict.BLOCKED
    assert "options" in verdict.breakdown
    assert verdict.breakdown["options"] == "FAILED"

    manifest.options.append(OptionRecord(option_id="O-2", option_class=OptionClass.DEFER_NO_OP, description="Do nothing", reversibility="Easy", blast_radius="None"))
    verdict2 = engine.evaluate(manifest)
    assert verdict2.breakdown["options"] == "OK"

def test_trust_verdict_engine():
    dec = DecisionDefinition(decision_id="D-101", decision_class=DecisionClass.RELEASE_ROLLOUT, owner="Alice", intent="Promote v2")
    manifest = DecisionManifest(decision=dec)

    engine = TrustVerdictEngine()
    verdict = engine.evaluate(manifest)
    assert verdict.verdict == TrustVerdict.BLOCKED
    assert "options" in verdict.breakdown
    assert verdict.breakdown["options"] == "FAILED"

    manifest.options = [
        OptionRecord(option_id="O-1", option_class=OptionClass.AGGRESSIVE, description="Rollout now", reversibility="Hard", blast_radius="High"),
        OptionRecord(option_id="O-2", option_class=OptionClass.DEFER_NO_OP, description="Do nothing", reversibility="Easy", blast_radius="None")
    ]
    manifest.rationale = [RationaleRecord(rationale_id="R-1", chosen_option_id="O-1", rejected_option_ids=["O-2"], justification="Better", non_goals=[])]

    verdict2 = engine.evaluate(manifest)
    assert verdict2.verdict == TrustVerdict.BLOCKED # still missing assumptions and premortem

def test_quality_checker():
    manifest = DecisionManifestBuilder().build_empty("D-1", "A", "I", DecisionClass.RELEASE_ROLLOUT)
    checker = DecisionQualityChecker()
    res = checker.check(manifest)
    assert res["verdict"] == "NEEDS_IMPROVEMENT"
    assert "Missing options warning" in res["warnings"]
    assert "Hidden assumption warning" in res["warnings"]
    assert "Missing premortem warning" in res["warnings"]

def test_storage():
    repo = DecisionRepository()
    manifest = DecisionManifestBuilder().build_empty("D-1", "A", "I", DecisionClass.RELEASE_ROLLOUT)
    repo.save(manifest)
    assert repo.get("D-1") is not None

def test_outcome_and_counterfactual():
    manifest = DecisionManifestBuilder().build_empty("D-1", "A", "I", DecisionClass.RELEASE_ROLLOUT)
    manifest.outcome = DecisionOutcomeRecord(outcome_id="OUT-1", decision_id="D-1", outcome_class=OutcomeClass.SUCCESS, expected_vs_actual="Met", ambiguity_notes="None")

    checker = DecisionQualityChecker()
    res = checker.check(manifest)
    assert "Missing counterfactual warning" in res["warnings"]

    manifest.counterfactuals.append(CounterfactualReviewRecord(review_id="CR-1", decision_id="D-1", baseline_option_id="O-2", hypothetical_outcome="Would be worse", proof_notes="See sim"))
    res2 = checker.check(manifest)
    assert "Missing counterfactual warning" not in res2["warnings"]
