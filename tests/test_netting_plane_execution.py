import pytest
from app.netting_plane.residuals import ResidualsManager
from app.netting_plane.mistaken_setoff import MistakenSetoffManager
from app.netting_plane.trust import TrustEngine
from app.netting_plane.equivalence import EquivalenceManager
from app.netting_plane.enums import ResidualClass, TrustVerdict, EquivalenceVerdict

def test_residuals():
    mgr = ResidualsManager()
    rec = mgr.evaluate({"residual_id": "res-1", "status": ResidualClass.HIDDEN_RESIDUAL_EXPOSURE})
    assert rec.residual_id == "res-1"
    assert rec.status == ResidualClass.HIDDEN_RESIDUAL_EXPOSURE

def test_mistaken_setoff():
    mgr = MistakenSetoffManager()
    rec = mgr.evaluate({"mistaken_id": "ms-1", "posture": "suspected"})
    assert rec.mistaken_id == "ms-1"
    assert rec.posture == "suspected"

def test_trust_engine():
    engine = TrustEngine()
    verdict = engine.evaluate("net-555", {})
    assert verdict["verdict"] == TrustVerdict.TRUSTED
    assert verdict["residual_cleanliness"] is True

def test_equivalence():
    mgr = EquivalenceManager()
    rep = mgr.evaluate({"report_id": "eq-1", "divergence_sources": ["valuation mismatch"]})
    assert rep.verdict == EquivalenceVerdict.DIVERGENT

    rep2 = mgr.evaluate({"report_id": "eq-2", "divergence_sources": []})
    assert rep2.verdict == EquivalenceVerdict.FULLY_EQUIVALENT
