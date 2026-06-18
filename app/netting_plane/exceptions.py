class NettingPlaneError(Exception):
    """Base exception for Netting Plane."""
    pass

class InvalidNettingObjectError(NettingPlaneError):
    pass

class InvalidMutualObligationError(NettingPlaneError):
    pass

class InvalidMutualityError(NettingPlaneError):
    pass

class InvalidValuationError(NettingPlaneError):
    pass

class InvalidSetoffRightError(NettingPlaneError):
    pass

class InvalidCloseoutAmountError(NettingPlaneError):
    pass

class NettingTheaterViolation(NettingPlaneError):
    """Raised when opaque mahsup, arithmetic-only zeroing or closeout-free legal zero is claimed."""
    pass

class NettingStorageError(NettingPlaneError):
    pass
