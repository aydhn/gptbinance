from app.automation.models import RetryPolicy
from app.automation.enums import RetryVerdict


def evaluate_retry(policy: RetryPolicy, attempt: int, error_class: str) -> RetryVerdict:
    """Determine if a job should be retried."""
    if policy.retryable_exceptions and error_class not in policy.retryable_exceptions:
        return RetryVerdict.NON_RETRYABLE

    if attempt >= policy.max_attempts:
        return RetryVerdict.EXHAUSTED

    return RetryVerdict.RETRY


def calculate_backoff(policy: RetryPolicy, attempt: int) -> int:
    """Calculate backoff seconds before next retry."""
    if policy.exponential:
        return policy.backoff_seconds * (2 ** (attempt - 1))
    return policy.backoff_seconds
