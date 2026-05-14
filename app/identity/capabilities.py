from enum import Enum
CAPABILITIES = [
    "inspect_policy_manifest",
    "review_policy_conflicts",
    "request_policy_waiver",
    "approve_policy_waiver",
    "review_policy_coverage",
    "inspect_observability_manifest",
    "review_telemetry_schema",
    "review_sampling_changes",
    "review_retention_policy",
    "review_diagnostic_signal_quality"
]

class IdentityCapabilityMigrationRef:
    def inspect_migration_manifest(self):
        pass

class Capability(str, Enum):
    INSPECT_DECISION_MANIFEST = 'inspect_decision_manifest'