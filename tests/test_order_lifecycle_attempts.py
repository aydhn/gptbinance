from app.order_lifecycle.attempts import AttemptManager
from app.order_lifecycle.enums import LifecycleState
import pytest
from app.order_lifecycle.exceptions import DuplicateSubmitError


def test_create_attempt():
    mgr = AttemptManager()
    att = mgr.create_attempt("plan123", "leg456", "int789", {"test": 1})
    assert att is not None
    assert att.state.current_state == LifecycleState.CREATED
    assert att.lineage.compiled_leg_id == "leg456"


def test_duplicate_attempt_blocks():
    mgr = AttemptManager()
    mgr.create_attempt("plan123", "leg456", "int789", {"test": 1})
    with pytest.raises(DuplicateSubmitError):
        mgr.create_attempt("plan123", "leg456", "int789", {"test": 1})
