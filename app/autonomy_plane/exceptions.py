class AutonomyPlaneError(Exception):
    pass

class InvalidAutonomyObject(AutonomyPlaneError):
    pass

class InvalidAgentRecord(AutonomyPlaneError):
    pass

class InvalidTaskScope(AutonomyPlaneError):
    pass

class InvalidCapability(AutonomyPlaneError):
    pass

class InvalidPermissionGrant(AutonomyPlaneError):
    pass

class InvalidDelegation(AutonomyPlaneError):
    pass

class InvalidApproval(AutonomyPlaneError):
    pass

class GuardrailViolation(AutonomyPlaneError):
    pass

class HaltViolation(AutonomyPlaneError):
    pass

class AutonomyStorageError(AutonomyPlaneError):
    pass
