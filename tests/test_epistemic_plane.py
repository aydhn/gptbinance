import pytest
from app.epistemic_plane.models import *
from app.epistemic_plane.registry import CanonicalEpistemicRegistry
from app.epistemic_plane.exceptions import *

def test_epistemic_registry():
    registry = CanonicalEpistemicRegistry()
    fact = FactRecord(epistemic_id="fact-1", owner="sys", scope="test", fact_description="A observed fact", observed=True, proof_notes="None")
    registry.register(fact)
    assert registry.get("fact-1").epistemic_id == "fact-1"

def test_epistemic_trust():
    from app.epistemic_plane.trust import TrustManager
    tm = TrustManager()
    v = tm.evaluate_trust("claim-1")
    assert v.verdict == EpistemicTrustVerdict.TRUSTED

def test_epistemic_equivalence():
    from app.epistemic_plane.enums import EpistemicEquivalenceVerdict
    report = EpistemicEquivalenceReport(verdict=EpistemicEquivalenceVerdict.EQUIVALENT, divergence_sources=[])
    assert report.verdict == "equivalent"
