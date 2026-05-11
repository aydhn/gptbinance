import pytest
from app.policy_plane.invariants import (
    create_environment_separation_invariant,
    create_no_bypassable_invariant,
)
from app.policy_plane.enums import InvariantClass


def test_environment_separation_invariant():
    inv = create_environment_separation_invariant("Env must be isolated", "Checked")
    assert inv.invariant_class == InvariantClass.ENVIRONMENT_SEPARATION


def test_no_bypassable_invariant():
    inv = create_no_bypassable_invariant("Cannot bypass", "Checked")
    assert inv.invariant_class == InvariantClass.NON_BYPASSABLE
