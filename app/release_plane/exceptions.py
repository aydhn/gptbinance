class ReleasePlaneError(Exception):
    pass

class InvalidReleaseDefinition(ReleasePlaneError):
    pass

class InvalidCandidateBundle(ReleasePlaneError):
    pass

class InvalidPinSet(ReleasePlaneError):
    pass

class CompatibilityViolation(ReleasePlaneError):
    pass

class RolloutViolation(ReleasePlaneError):
    pass

class RollbackViolation(ReleasePlaneError):
    pass

class HotfixViolation(ReleasePlaneError):
    pass

class EquivalenceError(ReleasePlaneError):
    pass

class ReleaseStorageError(ReleasePlaneError):
    pass
