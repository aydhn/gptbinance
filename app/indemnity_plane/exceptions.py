class IndemnityPlaneError(Exception):
    pass

class InvalidIndemnityObjectError(IndemnityPlaneError):
    pass

class InvalidCoveredLossError(IndemnityPlaneError):
    pass

class InvalidCoverageError(IndemnityPlaneError):
    pass

class InvalidExclusionError(IndemnityPlaneError):
    pass

class InvalidNoticeError(IndemnityPlaneError):
    pass

class InvalidReimbursementError(IndemnityPlaneError):
    pass

class IndemnityTheaterViolationError(IndemnityPlaneError):
    pass

class IndemnityStorageError(IndemnityPlaneError):
    pass
