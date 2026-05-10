import pytest
from app.postmortem_plane.verification import ActionVerifier
from app.postmortem_plane.enums import VerificationClass, EffectivenessClass
from app.postmortem_plane.exceptions import VerificationViolationError

def test_action_verifier():
    v = ActionVerifier.verify("V-1", VerificationClass.IMPLEMENTED, "PR merged")
    assert v.verification_id == "V-1"

    with pytest.raises(VerificationViolationError):
        ActionVerifier.verify("V-2", VerificationClass.EFFECTIVENESS, "It feels better")
