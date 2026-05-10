import pytest
from app.policy_plane.scopes import ScopeCalculus


def test_scope_calculus():
    allowed = {"env": "live", "stage": "prod"}
    req_match = {"env": "live", "stage": "prod", "user": "admin"}
    req_mismatch = {"env": "paper", "stage": "prod"}

    assert ScopeCalculus.is_within_scope(req_match, allowed)
    assert not ScopeCalculus.is_within_scope(req_mismatch, allowed)
