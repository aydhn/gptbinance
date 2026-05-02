class ResilienceError(Exception):
    pass


class InvalidExperimentDefinitionError(ResilienceError):
    pass


class InvalidFaultInjectionSpecError(ResilienceError):
    pass


class InvalidStressProfileError(ResilienceError):
    pass


class GateViolationError(ResilienceError):
    pass


class AssertionFailureError(ResilienceError):
    pass


class UnsafeScopeError(ResilienceError):
    pass


class RollbackCleanupError(ResilienceError):
    pass


class TelemetryCaptureError(ResilienceError):
    pass
