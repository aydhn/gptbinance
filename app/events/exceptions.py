class EventRiskError(Exception):
    pass


class InvalidEventSourceError(EventRiskError):
    pass


class InvalidEventRecordError(EventRiskError):
    pass


class EventNormalizationError(EventRiskError):
    pass


class StaleEventDataError(EventRiskError):
    pass


class EventGateError(EventRiskError):
    pass


class CooldownPolicyError(EventRiskError):
    pass


class BlackoutConflictError(EventRiskError):
    pass


class TimezoneNormalizationError(EventRiskError):
    pass


class EventOverlayError(EventRiskError):
    pass
