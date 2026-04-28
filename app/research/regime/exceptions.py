class RegimeError(Exception):
    """Base exception for regime-related errors."""

    pass


class InsufficientRegimeDataError(RegimeError):
    """Raised when there is not enough historical data to calculate a regime."""

    pass


class InvalidRegimeSpecError(RegimeError):
    """Raised when a regime specification is invalid."""

    pass


class TransitionDetectionError(RegimeError):
    """Raised when transition detection logic fails."""

    pass


class MTFRegimeAlignmentError(RegimeError):
    """Raised when multi-timeframe regime alignment fails or leaks."""

    pass


class RegimeLeakageError(RegimeError):
    """Raised when lookahead bias or future data leakage is detected in regime generation."""

    pass
