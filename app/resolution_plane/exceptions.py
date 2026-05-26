class ResolutionPlaneError(Exception):
    pass

class InvalidResolutionObjectError(ResolutionPlaneError):
    pass

class InvalidBridgeError(ResolutionPlaneError):
    pass

class InvalidTransferPerimeterError(ResolutionPlaneError):
    pass

class InvalidContinuityMapError(ResolutionPlaneError):
    pass

class InvalidWriteDownError(ResolutionPlaneError):
    pass

class InvalidConversionError(ResolutionPlaneError):
    pass

class ContinuityGapViolationError(ResolutionPlaneError):
    pass

class ResolutionStorageError(ResolutionPlaneError):
    pass
