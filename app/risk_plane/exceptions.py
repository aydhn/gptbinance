class RiskPlaneError(Exception):
    pass


class InvalidRiskLimitError(RiskPlaneError):
    pass


class InvalidRiskStateError(RiskPlaneError):
    pass


class InvalidBreachRecordError(RiskPlaneError):
    pass


class ResponseIntentError(RiskPlaneError):
    pass


class CooldownViolationError(RiskPlaneError):
    pass


class LiquidationProximityError(RiskPlaneError):
    pass


class EquivalenceError(RiskPlaneError):
    pass


class TrustVerdictError(RiskPlaneError):
    pass


class RiskStorageError(RiskPlaneError):
    pass
