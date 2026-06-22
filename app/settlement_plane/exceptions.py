class SettlementPlaneError(Exception):
    pass


class InvalidSettlementObjectError(SettlementPlaneError):
    pass


class InvalidInstructionError(SettlementPlaneError):
    pass


class InvalidSSIError(SettlementPlaneError):
    pass


class InvalidMatchingPostureError(SettlementPlaneError):
    pass


class InvalidFinalityPostureError(SettlementPlaneError):
    pass


class InvalidReversalError(SettlementPlaneError):
    pass


class SettlementTheaterViolationError(SettlementPlaneError):
    pass


class SettlementStorageError(SettlementPlaneError):
    pass


class InvalidSettlementError(SettlementPlaneError):
    pass


class DefectiveSettlementError(SettlementPlaneError):
    pass


class SettlementComparisonError(SettlementPlaneError):
    pass


class InvalidCarveOutError(SettlementPlaneError):
    pass
