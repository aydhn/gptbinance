class LiabilityPlaneError(Exception):
    pass

class InvalidLiabilityObjectError(LiabilityPlaneError):
    pass

class InvalidCausationRecordError(LiabilityPlaneError):
    pass

class InvalidFaultAssessmentError(LiabilityPlaneError):
    pass

class InvalidIndemnityError(LiabilityPlaneError):
    pass

class InvalidExonerationError(LiabilityPlaneError):
    pass

class InvalidLimitationError(LiabilityPlaneError):
    pass

class LiabilityOverreachViolation(LiabilityPlaneError):
    pass

class LiabilityStorageError(LiabilityPlaneError):
    pass
