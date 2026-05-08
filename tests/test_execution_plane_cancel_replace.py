import pytest
from app.execution_plane.cancel_replace import CancelReplaceManager
from app.execution_plane.exceptions import CancelReplaceViolationError


def test_cancel_replace_chain():
    manager = CancelReplaceManager()
    chain = manager.initiate_chain("s1")

    manager.add_replacement("s1", "s2")
    assert "s2" in manager._chains["s1"].replaced_spec_ids

    manager.mark_ambiguous("s1", "network_error")
    with pytest.raises(CancelReplaceViolationError):
        manager.add_replacement("s1", "s3")
