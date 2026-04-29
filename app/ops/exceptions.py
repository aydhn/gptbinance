class OpsError(Exception):
    pass


class ReadinessFailure(OpsError):
    pass


class SupervisorError(OpsError):
    pass


class RecoveryFailure(OpsError):
    pass


class MaintenanceViolation(OpsError):
    pass


class IncidentEscalationError(OpsError):
    pass


class GoLiveGateViolation(OpsError):
    pass


class StateHydrationError(OpsError):
    pass


class RuntimeControlError(OpsError):
    pass
