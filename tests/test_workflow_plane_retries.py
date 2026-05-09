from app.workflow_plane.retries import RetryManager
from app.workflow_plane.enums import RetryClass
from app.workflow_plane.exceptions import InvalidRetryError
import pytest

def test_retry_manager():
    mgr = RetryManager()
    rec = mgr.register_retry("run-1", "Timeout", 1, RetryClass.RETRYABLE)
    assert rec.retry_count == 1

    with pytest.raises(InvalidRetryError):
        mgr.register_retry("run-2", "Fatal", 1, RetryClass.NON_RETRYABLE)
