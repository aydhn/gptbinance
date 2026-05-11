import pytest
from app.policy_plane.verdicts import create_allow_verdict, create_deny_verdict
from app.policy_plane.enums import VerdictClass


def test_allow_verdict():
    verdict = create_allow_verdict("Reason", "Proof")
    assert verdict.verdict_class == VerdictClass.ALLOW


def test_deny_verdict():
    verdict = create_deny_verdict("Reason", "Proof")
    assert verdict.verdict_class == VerdictClass.DENY
