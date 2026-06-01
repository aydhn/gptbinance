class AdaptationPlaneError(Exception):
    pass

class InvalidAdaptationObject(AdaptationPlaneError):
    pass

class InvalidRootCauseHypothesis(AdaptationPlaneError):
    pass

class InvalidCountermeasure(AdaptationPlaneError):
    pass

class InvalidRecalibration(AdaptationPlaneError):
    pass

class InvalidVerificationWindow(AdaptationPlaneError):
    pass

class InvalidFitnessRestoration(AdaptationPlaneError):
    pass

class AdaptationTheaterViolation(AdaptationPlaneError):
    pass

class AdaptationStorageError(AdaptationPlaneError):
    pass
