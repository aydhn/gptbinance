class AnalyticsError(Exception):
    """Base exception for analytics module."""

    pass


class InvalidAnalyticsConfigError(AnalyticsError):
    pass


class AttributionError(AnalyticsError):
    pass


class DivergenceAnalysisError(AnalyticsError):
    pass


class JournalIntegrityError(AnalyticsError):
    pass


class ExecutionQualityError(AnalyticsError):
    pass


class AnomalyDetectionError(AnalyticsError):
    pass


class ReportingError(AnalyticsError):
    pass
