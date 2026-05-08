class RetryPolicyEngine:
    @staticmethod
    def can_retry(reject_reason: str, attempts_count: int, max_budget: int = 3) -> bool:
        if attempts_count >= max_budget:
            return False

        non_retryable = [
            "insufficient_funds",
            "invalid_symbol",
            "venue_filter_violation",
        ]

        for nr in non_retryable:
            if nr in reject_reason.lower():
                return False

        return True

    @staticmethod
    def get_backoff_ms(attempts_count: int) -> int:
        return 1000 * (2**attempts_count)
