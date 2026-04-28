class BacktestError(Exception):
    """Base exception for backtest errors."""

    pass


class InvalidBacktestConfigError(BacktestError):
    """Configuration is invalid."""

    pass


class FillSimulationError(BacktestError):
    """Error during fill simulation."""

    pass


class ReplayMismatchError(BacktestError):
    """Data mismatch during replay."""

    pass


class PositionStateError(BacktestError):
    """Invalid position state transition."""

    pass


class PerformanceCalculationError(BacktestError):
    """Error calculating performance metrics."""

    pass
