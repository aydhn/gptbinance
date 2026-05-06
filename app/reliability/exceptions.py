class ReliabilityTowerError(Exception):
    pass


class InvalidSLODefinition(ReliabilityTowerError):
    pass


class InvalidErrorBudget(ReliabilityTowerError):
    pass


class BurnRateError(ReliabilityTowerError):
    pass


class ScorecardError(ReliabilityTowerError):
    pass


class ReadinessDecayError(ReliabilityTowerError):
    pass


class FreezeRecommendationError(ReliabilityTowerError):
    pass


class StaleReliabilityEvidenceError(ReliabilityTowerError):
    pass


class TrendEvaluationError(ReliabilityTowerError):
    pass


class ReliabilityStorageError(ReliabilityTowerError):
    pass
