class DriftPlaneError(Exception):
    """Base exception for drift plane errors."""
    pass

class InvalidDriftObjectError(DriftPlaneError):
    pass

class InvalidBaselineError(DriftPlaneError):
    pass

class InvalidDriftSignalError(DriftPlaneError):
    pass

class InvalidThresholdBreachError(DriftPlaneError):
    pass

class InvalidRecurrenceTriggerError(DriftPlaneError):
    pass

class InvalidRenormalizationPathError(DriftPlaneError):
    pass

class DriftTheaterViolation(DriftPlaneError):
    pass

class DriftStorageError(DriftPlaneError):
    pass
