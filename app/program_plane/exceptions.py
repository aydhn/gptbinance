class ProgramPlaneError(Exception):
    pass

class InvalidProgramObject(ProgramPlaneError):
    pass

class InvalidMilestoneDefinition(ProgramPlaneError):
    pass

class InvalidDependencyEdge(ProgramPlaneError):
    pass

class InvalidBlockerState(ProgramPlaneError):
    pass

class InvalidHandoffState(ProgramPlaneError):
    pass

class InvalidCriticalPathRecord(ProgramPlaneError):
    pass

class InvalidReplanRecord(ProgramPlaneError):
    pass

class EscalationViolation(ProgramPlaneError):
    pass

class ProgramStorageError(ProgramPlaneError):
    pass
