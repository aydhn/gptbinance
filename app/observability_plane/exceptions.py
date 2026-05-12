class ObservabilityPlaneError(Exception):
    """Base exception for observability plane."""
    pass

class InvalidTelemetryDefinitionError(ObservabilityPlaneError):
    pass

class InvalidSchemaContractError(ObservabilityPlaneError):
    pass

class InvalidDimensionOrTagError(ObservabilityPlaneError):
    pass

class InvalidClockSemanticsError(ObservabilityPlaneError):
    pass

class InvalidSamplingDefinitionError(ObservabilityPlaneError):
    pass

class RetentionViolationError(ObservabilityPlaneError):
    pass

class CorrelationViolationError(ObservabilityPlaneError):
    pass

class EquivalenceError(ObservabilityPlaneError):
    pass

class ObservabilityStorageError(ObservabilityPlaneError):
    pass
