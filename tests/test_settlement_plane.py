from app.settlement_plane.registry import CanonicalSettlementRegistry
from app.settlement_plane.models import SettlementObject
from app.settlement_plane.enums import SettlementClass, EquivalenceVerdict
from app.settlement_plane.equivalence import SettlementEquivalenceEvaluator
from app.settlement_plane.trust import SettlementTrustEvaluator


def test_registry_registration():
    registry = CanonicalSettlementRegistry()
    obj = SettlementObject(
        id="settlement_001",
        settlement_class=SettlementClass.CLEARING_SETTLEMENT,
        owner="clearing_system",
        scope_refs=["trade_123"],
        matching_posture="clean_match",
        finality_posture="clean_finality"
    )
    registry.register_settlement(obj)
    retrieved = registry.get_settlement("settlement_001")
    assert retrieved.id == "settlement_001"


def test_equivalence_evaluator():
    evaluator = SettlementEquivalenceEvaluator()
    replay = {"instruction": "A", "ssi": "B", "matching": "C", "finality": "D"}
    live = {"instruction": "A", "ssi": "B", "matching": "C", "finality": "D"}
    report = evaluator.evaluate(replay, live)
    assert report.verdict == EquivalenceVerdict.EQUIVALENT


def test_trust_evaluator():
    evaluator = SettlementTrustEvaluator()
    factors = {
        "instruction_clarity": True,
        "ssi_sufficiency": True,
        "matching_sufficiency": True,
        "funding_sufficiency": True,
        "finality_sufficiency": True
    }
    verdict = evaluator.evaluate("settlement_001", factors)
    assert verdict.verdict.value == "trusted"
