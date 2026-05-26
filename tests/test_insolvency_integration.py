import pytest
from app.insolvency_plane.repository import InsolvencyRepository

def test_recovery_finalization():
    from app.recovery_plane.finalization import RecoveryFinalization
    repo = InsolvencyRepository()
    rec = RecoveryFinalization()
    # It should not throw errors
    rec.check_finalization("rec-1", repo)
    assert True

def test_policy_invariants():
    from app.policy_kernel.invariants import PolicyInvariants
    repo = InsolvencyRepository()
    pol = PolicyInvariants()
    pol.check_invariants(repo)
    assert True
