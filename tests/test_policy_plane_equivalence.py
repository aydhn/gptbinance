import pytest
from app.policy_plane.equivalence import compare_environments
from app.policy_plane.enums import EquivalenceVerdict, ActionClass
from app.policy_plane.models import PolicyAction


def test_compare_environments():
    action = PolicyAction(action_class=ActionClass.EXECUTE)
    envs = ["paper", "live"]
    report = compare_environments(action, envs)

    assert report is not None
    assert report.verdict == EquivalenceVerdict.EQUIVALENT
    assert report.environments_compared == envs
