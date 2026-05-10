class IncidentPlaneError(Exception):
    pass

class InvalidStatusTransition(IncidentPlaneError):
    pass

class InvalidClosureState(IncidentPlaneError):
    pass

class InvalidSeverityEscalation(IncidentPlaneError):
    pass

class MissingRecoveryVerification(IncidentPlaneError):
    pass
