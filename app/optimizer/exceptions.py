class OptimizerError(Exception):
    """Base exception for the optimizer layer."""
    pass

class InvalidSearchSpaceError(OptimizerError):
    """Raised when the search space configuration is invalid."""
    pass

class InvalidParameterSpecError(OptimizerError):
    """Raised when a parameter specification is invalid."""
    pass

class InvalidTrialConfigError(OptimizerError):
    """Raised when trial configuration is invalid."""
    pass

class ObjectiveScoringError(OptimizerError):
    """Raised when there is an error during objective scoring."""
    pass

class RankingError(OptimizerError):
    """Raised when an error occurs during the ranking phase."""
    pass

class OptimizerGuardViolation(OptimizerError):
    """Raised when a critical optimizer guard is violated."""
    pass

class TrialExecutionError(OptimizerError):
    """Raised when a trial fails to execute."""
    pass
