import pytest
from app.release_plane.hotfixes import HotfixManager
from app.release_plane.enums import HotfixClass
from app.release_plane.exceptions import HotfixViolation

def test_governed_hotfix_creation():
    manager = HotfixManager()
    hf = manager.create_hotfix("cand-1", HotfixClass.TEMPORARY_PATCH, {"venue": "binance"}, "JIRA-123")
    assert hf.review_debt == "JIRA-123"

def test_reject_unbounded_hotfix():
    manager = HotfixManager()
    with pytest.raises(HotfixViolation):
         manager.create_hotfix("cand-1", HotfixClass.PERMANENT_FIX, {}, "JIRA-123")

def test_reject_undocumented_debt_hotfix():
    manager = HotfixManager()
    with pytest.raises(HotfixViolation):
         manager.create_hotfix("cand-1", HotfixClass.PERMANENT_FIX, {"venue": "binance"}, "")
