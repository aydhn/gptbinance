class EscrowPlaneError(Exception):
    pass

class InvalidEscrowObjectError(EscrowPlaneError):
    pass

class InvalidDepositedAssetError(EscrowPlaneError):
    pass

class InvalidReleaseConditionError(EscrowPlaneError):
    pass

class InvalidInstructionError(EscrowPlaneError):
    pass

class InvalidReleaseActionError(EscrowPlaneError):
    pass

class InvalidReversalError(EscrowPlaneError):
    pass

class EscrowTheaterViolationError(EscrowPlaneError):
    pass

class EscrowStorageError(EscrowPlaneError):
    pass
