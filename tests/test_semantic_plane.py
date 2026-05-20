import pytest
from app.semantic_plane.registry import CanonicalSemanticRegistry
from app.semantic_plane.models import (
    TermRecord, SemanticConflictRecord, MetricRecord,
    ThresholdRecord, AliasRecord, CanonicalDefinitionRecord
)
from app.semantic_plane.enums import TermClass, ConflictClass, MetricClass, ThresholdClass, AliasClass
from app.semantic_plane.exceptions import (
    InvalidSemanticObjectError, InvalidThresholdSemanticsError
)
from app.semantic_plane.trust import DefaultTrustEvaluator
from app.semantic_plane.state import StateSemanticManager
from app.semantic_plane.contracts import ContractSemanticManager

def test_semantic_registry_integrity():
    registry = CanonicalSemanticRegistry()
    term = TermRecord(
        term_id="term_1",
        name="Gross Profit",
        term_class=TermClass.CANONICAL,
        canonical_definition=CanonicalDefinitionRecord(
            definition_id="def_1", semantic_id="term_1", authoritative_text="Total revenue minus cost of goods sold."
        )
    )
    registry.register_term(term)
    assert registry.get_term("term_1").name == "Gross Profit"

def test_semantic_same_name_conflict():
    registry = CanonicalSemanticRegistry()
    term1 = TermRecord(term_id="t1", name="Ready", term_class=TermClass.CANONICAL)
    term2 = TermRecord(term_id="t2", name="Ready", term_class=TermClass.LOCAL_JARGON)

    registry.register_term(term1)
    registry.register_term(term2)

    # Should automatically register a SAME_NAME_DIFFERENT_MEANING conflict
    assert len(registry.conflicts) == 1
    conflict = list(registry.conflicts.values())[0]
    assert conflict.conflict_class == ConflictClass.SAME_NAME_DIFFERENT_MEANING

def test_invalid_semantic_object_rejection():
    registry = CanonicalSemanticRegistry()
    with pytest.raises(InvalidSemanticObjectError):
        registry.register_term(TermRecord(term_id="", name="Bad", term_class=TermClass.CANONICAL))

def test_threshold_semantics_enforcement():
    from app.semantic_plane.thresholds import ThresholdManager
    registry = CanonicalSemanticRegistry()
    mgr = ThresholdManager(registry)

    # Missing implication notes
    with pytest.raises(InvalidThresholdSemanticsError):
        mgr.register_threshold(ThresholdRecord(
            threshold_id="th_1", semantic_id="m_1", threshold_class=ThresholdClass.BLOCKER, implication_notes=""
        ))

def test_trust_evaluator_with_conflict():
    registry = CanonicalSemanticRegistry()
    term1 = TermRecord(term_id="t1", name="Latency", term_class=TermClass.CANONICAL)
    term2 = TermRecord(term_id="t2", name="Latency", term_class=TermClass.LOCAL_JARGON)
    registry.register_term(term1)
    registry.register_term(term2) # Causes conflict

    evaluator = DefaultTrustEvaluator(registry)
    # t2 caused a conflict registered under its ID
    verdict = evaluator.evaluate("t2")
    assert verdict.verdict.value == "blocked"
    assert "Unresolved semantic conflict" in verdict.blockers[0]

def test_state_plane_integration():
    registry = CanonicalSemanticRegistry()
    mgr = StateSemanticManager(registry)

    # Unregistered label
    is_valid = mgr.validate_state_label("unverified_label")
    assert not is_valid
    assert len(registry.conflicts) == 1
    assert list(registry.conflicts.values())[0].conflict_class == ConflictClass.SEMANTIC_SPLIT_BRAIN

def test_contract_plane_integration():
    registry = CanonicalSemanticRegistry()
    registry.register_term(TermRecord(term_id="t1", name="valid_field", term_class=TermClass.CANONICAL))

    mgr = ContractSemanticManager(registry)
    cautions = mgr.verify_payload_semantics(["valid_field", "rogue_field"])

    assert len(cautions) == 1
    assert "rogue_field" in cautions[0]
