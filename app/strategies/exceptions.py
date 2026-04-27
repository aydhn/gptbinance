class StrategyError(Exception):
    """Base exception for strategy-related errors."""

    pass


class InvalidStrategySpecError(StrategyError):
    """Raised when a strategy specification is invalid."""

    pass


class MissingFeatureError(StrategyError):
    """Raised when a required feature is missing for evaluation."""

    pass


class RuleEvaluationError(StrategyError):
    """Raised when a rule evaluation fails unexpectedly."""

    pass


class ConflictResolutionError(StrategyError):
    """Raised when conflict resolution fails."""

    pass


class CooldownViolationError(StrategyError):
    """Raised when attempting to generate signal during a cooldown period."""

    pass
