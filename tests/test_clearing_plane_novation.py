import pytest
from app.clearing_plane.novation import NovationManager
from app.clearing_plane.exceptions import InvalidNovationError

def test_strict_novation_clean():
    manager = NovationManager()
    manager.register("rec_1", {"accepted_by_ccp": True, "has_bilateral_residue": False})
    res = manager.evaluate("rec_1")
    assert res["status"] == "strict_novation_clean"

def test_fake_novation_raises_error():
    manager = NovationManager()
    manager.register("rec_2", {"accepted_by_ccp": True, "has_bilateral_residue": True})
    with pytest.raises(InvalidNovationError):
        manager.evaluate("rec_2")
