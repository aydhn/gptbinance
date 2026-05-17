import pytest
from app.environment_plane.secrets import define_secret_scope

def test_define_secret_scope():
    sec = define_secret_scope("Non-live", "Mocked keys")
    assert sec.scope_description == "Non-live"
    assert sec.proof_notes == "Mocked keys"
