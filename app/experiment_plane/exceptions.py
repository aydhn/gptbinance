class ExperimentPlaneError(Exception):
    pass


class InvalidExperimentDefinitionError(ExperimentPlaneError):
    pass


class InvalidArmConfigurationError(ExperimentPlaneError):
    pass


class InvalidBaselineControlError(ExperimentPlaneError):
    pass


class FairnessViolationError(ExperimentPlaneError):
    pass


class StoppingRuleViolationError(ExperimentPlaneError):
    pass


class RecommendationError(ExperimentPlaneError):
    pass


class EquivalenceError(ExperimentPlaneError):
    pass


class TrustVerdictError(ExperimentPlaneError):
    pass


class ExperimentStorageError(ExperimentPlaneError):
    pass
