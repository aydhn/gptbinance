import pytest
from app.netting_plane.eligibility import EligibilityManager
from app.netting_plane.mutuality import MutualityEvaluator
from app.netting_plane.maturity import MaturityManager
from app.netting_plane.valuation import ValuationManager
from app.netting_plane.closeout import CloseoutEvaluator
from app.netting_plane.setoff_rights import SetoffRightsManager
from app.netting_plane.enums import MutualityClass, ValuationClass, SetoffClass

def test_eligibility():
    mgr = EligibilityManager()
    rec = mgr.evaluate({"eligibility_id": "elig-1", "status": "eligible"})
    assert rec.eligibility_id == "elig-1"
    assert rec.status == "eligible"

def test_mutuality():
    mgr = MutualityEvaluator()
    res = mgr.evaluate("mut-1", {"status": MutualityClass.FAILED_MUTUALITY})
    assert res["mutuality_id"] == "mut-1"
    assert res["status"] == MutualityClass.FAILED_MUTUALITY

def test_maturity():
    mgr = MaturityManager()
    rec = mgr.evaluate({"maturity_id": "mat-1", "status": "matured"})
    assert rec.maturity_id == "mat-1"
    assert rec.status == "matured"

def test_valuation():
    mgr = ValuationManager()
    rec = mgr.evaluate({"valuation_id": "val-1", "status": ValuationClass.STALE_VALUATION})
    assert rec.valuation_id == "val-1"
    assert rec.status == ValuationClass.STALE_VALUATION

def test_setoff_rights():
    mgr = SetoffRightsManager()
    rec = mgr.evaluate({"setoff_id": "set-1", "status": SetoffClass.BLOCKED_SETOFF_RIGHT})
    assert rec.setoff_id == "set-1"
    assert rec.status == SetoffClass.BLOCKED_SETOFF_RIGHT
