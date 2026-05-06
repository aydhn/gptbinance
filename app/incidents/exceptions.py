class IncidentCommandError(Exception):
    pass


class InvalidIncidentRecord(IncidentCommandError):
    pass


class IncidentScopeViolation(IncidentCommandError):
    pass


class EvidenceFreezeError(IncidentCommandError):
    pass


class InvalidContainmentPlan(IncidentCommandError):
    pass


class RecoveryPlanningError(IncidentCommandError):
    pass
