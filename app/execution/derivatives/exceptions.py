class DerivativeExecutionError(Exception):
    """Base exception for derivative execution errors."""

    pass


class InvalidLeverageChange(DerivativeExecutionError):
    pass


class InvalidMarginModeTransition(DerivativeExecutionError):
    pass


class ReduceOnlyViolation(DerivativeExecutionError):
    pass


class LiquidationRiskBreach(DerivativeExecutionError):
    pass


class FundingSyncError(DerivativeExecutionError):
    pass


class BorrowSyncError(DerivativeExecutionError):
    pass
