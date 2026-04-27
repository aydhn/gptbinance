class FeatureError(Exception):
    """Base exception for all feature-related errors."""

    pass


class FeatureGenerationError(FeatureError):
    """Raised when feature generation fails."""

    pass


class UnsupportedFeatureError(FeatureError):
    """Raised when a requested feature is not supported/registered."""

    pass


class InvalidFeatureSpecError(FeatureError):
    """Raised when feature specifications are invalid."""

    pass


class AlignmentError(FeatureError):
    """Raised when MTF alignment fails."""

    pass


class LeakageError(FeatureError):
    """Raised when potential data leakage (lookahead bias) is detected."""

    pass


class DivergenceComputationError(FeatureError):
    """Raised when divergence computation fails."""

    pass


class InsufficientHistoryError(FeatureError):
    """Raised when there is not enough history to calculate a feature."""

    pass
