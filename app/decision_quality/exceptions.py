class DecisionQualityError(Exception):
    """Base exception for Decision Quality and Opportunity Forensics errors."""


class InvalidOpportunityRecord(DecisionQualityError):
    """Raised when an opportunity record is invalid or missing required data."""


class InvalidOutcomeWindow(DecisionQualityError):
    """Raised when an outcome window is not properly specified or mapped."""


class MissingFunnelLineage(DecisionQualityError):
    """Raised when the funnel lineage is broken or missing references."""


class DecisionComparisonError(DecisionQualityError):
    """Raised when trying to compare incompatible or incomplete decisions."""


class BlockReasonNormalizationError(DecisionQualityError):
    """Raised when block reason mapping or normalization fails."""


class FrictionAttributionError(DecisionQualityError):
    """Raised when friction source attribution fails."""


class HindsightPolicyError(DecisionQualityError):
    """Raised when a hindsight rule is violated (e.g. overclaiming without evidence)."""


class EvidenceInsufficiencyError(DecisionQualityError):
    """Raised when a quality verdict is attempted without enough evidence."""


class DecisionQualityStorageError(DecisionQualityError):
    """Raised when read/write operations to the decision quality store fail."""
