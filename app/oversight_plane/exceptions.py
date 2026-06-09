class OversightPlaneError(Exception):
    pass

class InvalidOversightObjectError(OversightPlaneError):
    pass

class InvalidSupervisoryMandateError(OversightPlaneError):
    pass

class InvalidOversightScopeError(OversightPlaneError):
    pass

class InvalidFindingError(OversightPlaneError):
    pass

class InvalidMaterialityThresholdError(OversightPlaneError):
    pass

class InvalidDirectiveError(OversightPlaneError):
    pass

class OversightTheaterViolationError(OversightPlaneError):
    pass

class OversightStorageError(OversightPlaneError):
    pass
