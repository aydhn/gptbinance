class StressRiskError(Exception):
    pass


class InvalidScenarioDefinitionError(StressRiskError):
    pass


class InvalidShockVectorError(StressRiskError):
    pass


class StressComputationError(StressRiskError):
    pass


class BudgetEvaluationError(StressRiskError):
    pass


class CorrelationStressError(StressRiskError):
    pass


class LiquidityStressError(StressRiskError):
    pass


class TailLossEstimationError(StressRiskError):
    pass


class ScopeMismatchError(StressRiskError):
    pass


class ScenarioCalibrationError(StressRiskError):
    pass
