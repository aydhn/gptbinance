class ValidationError(Exception):
    """Base class for validation layer exceptions."""

    pass


class InvalidBenchmarkSpecError(ValidationError):
    """Raised when benchmark spec is invalid."""

    pass


class InvalidAblationSpecError(ValidationError):
    """Raised when ablation spec is invalid."""

    pass


class InvalidComparisonInputError(ValidationError):
    """Raised when input to comparison is invalid."""

    pass


class SampleSplitError(ValidationError):
    """Raised on sample split logic failures."""

    pass


class ResearchHonestyViolationError(ValidationError):
    """Raised when strict research honesty bounds are breached."""

    pass


class RobustnessEvaluationError(ValidationError):
    """Raised when robustness check fails."""

    pass
