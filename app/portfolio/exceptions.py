class PortfolioError(Exception):
    """Base exception for portfolio module."""

    pass


class InvalidPortfolioConfig(PortfolioError):
    """Raised when portfolio configuration is invalid."""

    pass


class AllocationError(PortfolioError):
    """Raised when an error occurs during allocation."""

    pass


class RankingError(PortfolioError):
    """Raised when an error occurs during candidate ranking."""

    pass


class CorrelationEstimationError(PortfolioError):
    """Raised when correlation estimation fails."""

    pass


class ConcentrationViolation(PortfolioError):
    """Raised when a concentration limit is breached."""

    pass


class BudgetViolation(PortfolioError):
    """Raised when a budget limit is breached."""

    pass


class AdmissionControlError(PortfolioError):
    """Raised when an intent fails basic admission controls."""

    pass
