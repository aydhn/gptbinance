class PerfError(Exception):
    """Base exception for all perf layer errors."""

    pass


class InvalidWorkloadDefinitionError(PerfError):
    pass


class InvalidResourceBudgetError(PerfError):
    pass


class InvalidLatencyBudgetError(PerfError):
    pass


class ProfilingError(PerfError):
    pass


class RegressionError(PerfError):
    pass


class HostQualificationError(PerfError):
    pass


class BottleneckAttributionError(PerfError):
    pass


class CapacityEvaluationError(PerfError):
    pass
