from enum import Enum
class IdentityRunbook:
    pass


class ComplianceIntegrityRunbook:
    pass


class AttestationExpiryRunbook:
    pass


class TelemetryGapInvestigationRunbook:
    pass


class TraceLogCorrelationReviewRunbook:
    pass


class HiddenSamplingReviewRunbook:
    pass


class ClockSemanticsInvestigationRunbook:
    pass


class CardinalityCostReviewRunbook:
    pass


class TelemetryRetentionReviewRunbook:
    pass

class RunbookRef(str, Enum):
    DECISION_OPTION_SET_REVIEW = 'decision_option_set_review'