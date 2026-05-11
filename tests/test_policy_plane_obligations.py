import pytest
from app.policy_plane.obligations import (
    create_must_attach_evidence_obligation,
    create_must_wait_for_approval_obligation,
)
from app.policy_plane.enums import ObligationClass


def test_must_attach_evidence_obligation():
    obl = create_must_attach_evidence_obligation("Evidence required")
    assert obl.obligation_class == ObligationClass.MUST_ATTACH_EVIDENCE


def test_must_wait_for_approval_obligation():
    obl = create_must_wait_for_approval_obligation("Approval required")
    assert obl.obligation_class == ObligationClass.MUST_WAIT_FOR_APPROVAL
