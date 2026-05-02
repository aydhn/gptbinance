class ObservabilityError(Exception):
    """Base exception for observability module."""

    pass


class InvalidMetricDefinition(ObservabilityError):
    """Raised when a metric definition is invalid."""

    pass


class InvalidAlertRule(ObservabilityError):
    """Raised when an alert rule configuration is invalid."""

    pass


class HealthAggregationError(ObservabilityError):
    """Raised when health aggregation fails."""

    pass


class AlertCorrelationError(ObservabilityError):
    """Raised when alert correlation encounters an error."""

    pass


class SloEvaluationError(ObservabilityError):
    """Raised when SLO evaluation fails."""

    pass


class TelemetryQueryError(ObservabilityError):
    """Raised when querying telemetry storage fails."""

    pass


class SuppressionError(ObservabilityError):
    """Raised during alert suppression operations."""

    pass


class EnrichmentError(ObservabilityError):
    """Raised during event/alert enrichment."""

    pass
