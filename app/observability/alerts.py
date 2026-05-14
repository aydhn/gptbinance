from enum import Enum
class IdentityAlert:
    pass


class ComplianceTrustDegradedAlert:
    pass


class ExpiredAttestationAlert:
    pass


class TelemetryGapDetectedAlert:
    pass


class TelemetryTrustDegradedAlert:
    pass


class HiddenSamplingDetectedAlert:
    pass


class ClockSkewCriticalAlert:
    pass


class CardinalityExplosionAlert:
    pass


class DiagnosticCorrelationBrokenAlert:
    pass

class AlertFamily(str, Enum):
    HIDDEN_ASSUMPTION_DETECTED = 'hidden_assumption_detected'
    OVERCONFIDENCE_PATTERN_DETECTED = 'overconfidence_pattern_detected'