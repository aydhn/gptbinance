from app.data_governance.models import DataQualityRule
from app.data_governance.enums import QualitySeverity


class QualityRuleRegistry:
    def __init__(self):
        self.rules = {
            "duplicate_primary_keys": DataQualityRule(
                rule_name="duplicate_primary_keys",
                description="Checks for duplicate records based on primary key.",
                severity=QualitySeverity.CRITICAL,
            ),
            "missing_critical_timestamps": DataQualityRule(
                rule_name="missing_critical_timestamps",
                description="Checks for missing or null timestamps.",
                severity=QualitySeverity.CRITICAL,
            ),
            "timestamp_monotonicity": DataQualityRule(
                rule_name="timestamp_monotonicity",
                description="Checks if timestamps are strictly monotonically increasing.",
                severity=QualitySeverity.HIGH,
            ),
            "impossible_values": DataQualityRule(
                rule_name="impossible_values",
                description="Checks for impossible numerical values like negative price/volume.",
                severity=QualitySeverity.CRITICAL,
            ),
            "stale_snapshot": DataQualityRule(
                rule_name="stale_snapshot",
                description="Checks if the snapshot age exceeds expected limits.",
                severity=QualitySeverity.MEDIUM,
            ),
            "missing_provenance": DataQualityRule(
                rule_name="missing_provenance",
                description="Checks if lineage or provenance metadata is missing.",
                severity=QualitySeverity.HIGH,
            ),
            "unknown_schema_version": DataQualityRule(
                rule_name="unknown_schema_version",
                description="Checks if the dataset uses an unknown schema version.",
                severity=QualitySeverity.CRITICAL,
            ),
        }

    def get_rule(self, name: str) -> DataQualityRule:
        return self.rules.get(name)
