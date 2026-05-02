import pytest
from app.security.secrets import SecretResolver
from app.security.models import SecretRef
from app.security.enums import SecretStatus


def test_secret_resolution_missing():
    resolver = SecretResolver()
    res = resolver.resolve(SecretRef(key="NON_EXISTENT_KEY"))
    assert res.status == SecretStatus.MISSING
    assert res.value is None


def test_secret_resolution_env(monkeypatch):
    monkeypatch.setenv("DUMMY_KEY", "dummy_val")
    resolver = SecretResolver()
    res = resolver.resolve(SecretRef(key="DUMMY_KEY"))
    assert res.status == SecretStatus.SAFE
    assert res.value == "dummy_val"
