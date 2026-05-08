class PerformancePlaneError(Exception):
    pass


class InvalidBenchmarkDefinition(PerformancePlaneError):
    pass


class InvalidPerformanceWindow(PerformancePlaneError):
    pass


class InvalidReturnSurface(PerformancePlaneError):
    pass


class AttributionError(PerformancePlaneError):
    pass


class OpportunitySurfaceError(PerformancePlaneError):
    pass


class EquivalenceError(PerformancePlaneError):
    pass


class TrustVerdictError(PerformancePlaneError):
    pass


class ComparabilityViolation(PerformancePlaneError):
    pass


class PerformanceStorageError(PerformancePlaneError):
    pass
