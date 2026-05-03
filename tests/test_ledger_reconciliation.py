from app.ledger.reconciliation import ReconciliationEngine
from app.ledger.enums import ScopeType, ReconciliationVerdict


def test_reconciliation_match():
    engine = ReconciliationEngine()
    result = engine.reconcile({"USDT": 100.0}, {"USDT": 100.0}, ScopeType.PAPER)
    assert result.verdict == ReconciliationVerdict.MATCH
    assert len(result.differences) == 0


def test_reconciliation_mismatch():
    engine = ReconciliationEngine()
    result = engine.reconcile({"USDT": 100.0}, {"USDT": 105.0}, ScopeType.PAPER)
    assert result.verdict == ReconciliationVerdict.MISMATCH
    assert len(result.differences) == 1
    assert result.differences[0].delta == 5.0
