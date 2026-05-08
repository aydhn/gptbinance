class IngestionContractValidator:
    def validate_cadence(self, expected_ms: int, actual_ms: int) -> bool:
        return actual_ms <= expected_ms * 1.5  # Tolerance

    def validate_completeness(self, expected_records: int, actual_records: int) -> bool:
        return actual_records >= expected_records
