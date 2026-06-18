import pytest
from app.clearing_plane.trust import TrustManager
from app.clearing_plane.enums import TrustVerdict

def test_trusted_verdict():
    manager = TrustManager()
    manager.register("rec_1", {
        "trade_clarity": True,
        "novation_sufficiency": True,
        "segregation_integrity": True,
        "margin_sufficiency": True,
        "default_management_ready": True
    })
    res = manager.evaluate("rec_1")
    assert res["verdict"] == TrustVerdict.TRUSTED

def test_degraded_verdict():
    manager = TrustManager()
    manager.register("rec_2", {
        "trade_clarity": True,
        "novation_sufficiency": True,
        "segregation_integrity": True,
        "margin_sufficiency": False,
        "default_management_ready": True
    })
    res = manager.evaluate("rec_2")
    assert res["verdict"] == TrustVerdict.DEGRADED
