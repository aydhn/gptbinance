
import pytest
from app.accountability_plane.breaches import BreachesManager
from app.accountability_plane.sanctions import SanctionsManager
from app.accountability_plane.restitution import RestitutionManager
from app.accountability_plane.exceptions import InvalidBreachFindingError, AccountabilityTheaterViolation, RestitutionGapError
from app.accountability_plane.enums import BreachClass

def test_breach_requires_evidence():
    manager = BreachesManager()
    with pytest.raises(InvalidBreachFindingError):
        manager.register_breach("B1", "D1", BreachClass.MATERIAL, [])

def test_valid_breach():
    manager = BreachesManager()
    b = manager.register_breach("B2", "D1", BreachClass.MATERIAL, ["EVIDENCE-1"])
    assert b.breach_id == "B2"

def test_symbolic_sanction_prohibited():
    manager = SanctionsManager()
    with pytest.raises(AccountabilityTheaterViolation):
        manager.apply_sanction("S1", "B1", "SUB-1", "TIER-1", is_symbolic=True)

def test_restitution_resolution_requires_evidence():
    manager = RestitutionManager()
    r = manager.assign_restitution("R1", "B1")
    assert not r.is_resolved
    with pytest.raises(RestitutionGapError):
        manager.mark_resolved("R1", "")

    r2 = manager.mark_resolved("R1", "EVIDENCE-PAID")
    assert r2.is_resolved
