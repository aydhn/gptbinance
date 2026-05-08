class StrategyPlaneError(Exception):
    pass


class InvalidStrategyDefinition(StrategyPlaneError):
    pass


class InvalidThesisContract(StrategyPlaneError):
    pass


class InvalidSignalContract(StrategyPlaneError):
    pass


class InvalidLifecycleTransition(StrategyPlaneError):
    pass


class PromotionError(StrategyPlaneError):
    pass


class FreezeViolation(StrategyPlaneError):
    pass


class RetirementViolation(StrategyPlaneError):
    pass


class EquivalenceError(StrategyPlaneError):
    pass


class StrategyStorageError(StrategyPlaneError):
    pass
