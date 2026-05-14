class TelegramIdentityTemplate:
    pass


class TelegramComplianceTemplate:
    COMPLIANCE_MANIFEST_READY = "Compliance Manifest {manifest_id} is ready for review."

class TelegramObservabilityTemplate:
    MANIFEST_READY = "Observability Manifest {manifest_id} is ready."
    TRUST_DEGRADED = "Telemetry Trust Degraded: {telemetry_id}"
    GAP_DETECTED = "Telemetry Gap Detected: {gap_id}"
    HIDDEN_SAMPLING = "Hidden Sampling Detected: {telemetry_id}"

class TelegramTemplates:
    DECISION_MANIFEST_READY = 'Decision manifest {id} is ready'
    CRITICAL_DECISION_WITHOUT_OPTION_SET = 'Critical decision {id} has no option set'