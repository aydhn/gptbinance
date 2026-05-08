from app.execution_plane.retries import RetryPolicyEngine


def test_retry_policy():
    assert RetryPolicyEngine.can_retry("network_timeout", attempts_count=1) is True
    assert RetryPolicyEngine.can_retry("insufficient_funds", attempts_count=1) is False
    assert RetryPolicyEngine.can_retry("network_timeout", attempts_count=3) is False
