class ContinuityPlaneError(Exception):
    pass

class InvalidContinuityDefinition(ContinuityPlaneError):
    pass

class InvalidObjective(ContinuityPlaneError):
    pass

class InvalidBackupPolicy(ContinuityPlaneError):
    pass

class InvalidSnapshotRecord(ContinuityPlaneError):
    pass

class RestoreVerificationViolation(ContinuityPlaneError):
    pass

class FailoverViolation(ContinuityPlaneError):
    pass

class FailbackViolation(ContinuityPlaneError):
    pass

class SplitBrainViolation(ContinuityPlaneError):
    pass

class ContinuityStorageError(ContinuityPlaneError):
    pass
