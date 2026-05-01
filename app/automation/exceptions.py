class AutomationError(Exception):
    """Base exception for automation layer."""


class InvalidJobDefinitionError(AutomationError):
    pass


class InvalidWorkflowDefinitionError(AutomationError):
    pass


class ScheduleParseError(AutomationError):
    pass


class DependencyError(AutomationError):
    pass


class PreconditionFailureError(AutomationError):
    pass


class DuplicateRunError(AutomationError):
    pass


class RetryExhaustionError(AutomationError):
    pass


class AutomationPauseError(AutomationError):
    pass


class CalendarError(AutomationError):
    pass
