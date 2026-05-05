import pytest
from app.activation.evidence import EvidenceCollector


def test_evidence_collector():
    bundle = EvidenceCollector.collect("intent-1", "board-ref-1")
    assert bundle.intent_id == "intent-1"
    assert bundle.board_decision_ref == "board-ref-1"
    assert len(bundle.policy_proof_refs) > 0
