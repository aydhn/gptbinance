class OptimizerError(Exception):
    pass


class InvalidSearchSpace(OptimizerError):
    pass


class InvalidParameterSpec(OptimizerError):
    pass


class InvalidTrialConfig(OptimizerError):
    pass


class ObjectiveScoringError(OptimizerError):
    pass


class RankingError(OptimizerError):
    pass


class OptimizerGuardViolation(OptimizerError):
    pass


class TrialExecutionError(OptimizerError):
    pass
