class SuccessionPlaneError(Exception):
    pass

class InvalidSuccessionObject(SuccessionPlaneError):
    pass

class InvalidSuccessorCandidate(SuccessionPlaneError):
    pass

class InvalidEligibilityAssessment(SuccessionPlaneError):
    pass

class InvalidAuthorityTransfer(SuccessionPlaneError):
    pass

class InvalidOverlapWindow(SuccessionPlaneError):
    pass

class InvalidContinuityMap(SuccessionPlaneError):
    pass

class SuccessionTheaterViolation(SuccessionPlaneError):
    pass

class SuccessionStorageError(SuccessionPlaneError):
    pass
