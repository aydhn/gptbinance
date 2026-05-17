class EnvironmentPlaneError(Exception):
    pass

class InvalidEnvironmentObjectError(EnvironmentPlaneError):
    pass

class InvalidTopologyRecordError(EnvironmentPlaneError):
    pass

class InvalidParityRecordError(EnvironmentPlaneError):
    pass

class InvalidPromotionPathError(EnvironmentPlaneError):
    pass

class InvalidIsolationRecordError(EnvironmentPlaneError):
    pass

class InvalidBoundaryRecordError(EnvironmentPlaneError):
    pass

class ContaminationViolationError(EnvironmentPlaneError):
    pass

class DriftViolationError(EnvironmentPlaneError):
    pass

class EnvironmentStorageError(EnvironmentPlaneError):
    pass
