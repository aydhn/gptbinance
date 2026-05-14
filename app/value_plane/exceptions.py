class ValuePlaneError(Exception):
    pass

class InvalidValueObject(ValuePlaneError):
    pass

class InvalidObjectiveDefinition(ValuePlaneError):
    pass

class InvalidKpiDefinition(ValuePlaneError):
    pass

class InvalidBenefitHypothesis(ValuePlaneError):
    pass

class InvalidBaselineOrCounterfactual(ValuePlaneError):
    pass

class InvalidAttribution(ValuePlaneError):
    pass

class InvalidRoiRecord(ValuePlaneError):
    pass

class ValueVarianceViolation(ValuePlaneError):
    pass

class ValueStorageError(ValuePlaneError):
    pass
