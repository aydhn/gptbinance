from enum import Enum

class TelemetryClass(Enum):
    METRIC = "METRIC"
    LOG = "LOG"
    TRACE = "TRACE"
    EVENT = "EVENT"
    DIAGNOSTIC = "DIAGNOSTIC"

class MetricClass(Enum):
    COUNTER = "COUNTER"
    GAUGE = "GAUGE"
    HISTOGRAM = "HISTOGRAM"
    SUMMARY = "SUMMARY"

class LogClass(Enum):
    STRUCTURED = "STRUCTURED"
    AUDIT = "AUDIT"
    ACCESS = "ACCESS"

class TraceClass(Enum):
    WORKFLOW = "WORKFLOW"
    EXECUTION = "EXECUTION"
    REQUEST = "REQUEST"

class EventClass(Enum):
    DOMAIN = "DOMAIN"
    LIFECYCLE = "LIFECYCLE"
    ALERT = "ALERT"

class ClockClass(Enum):
    EVENT_TIME = "EVENT_TIME"
    EMIT_TIME = "EMIT_TIME"
    INGEST_TIME = "INGEST_TIME"
    OBSERVE_TIME = "OBSERVE_TIME"

class SamplingClass(Enum):
    FULL = "FULL"
    DETERMINISTIC = "DETERMINISTIC"
    RATE = "RATE"
    ADAPTIVE = "ADAPTIVE"

class RetentionClass(Enum):
    HOT = "HOT"
    WARM = "WARM"
    ARCHIVE = "ARCHIVE"

class DiagnosticClass(Enum):
    SYMPTOM = "SYMPTOM"
    CONTRIBUTOR = "CONTRIBUTOR"
    ROOT_CAUSE = "ROOT_CAUSE"

class EquivalenceVerdict(Enum):
    EQUIVALENT = "EQUIVALENT"
    PARTIAL = "PARTIAL"
    DIVERGENT = "DIVERGENT"

class TrustVerdict(Enum):
    TRUSTED = "TRUSTED"
    CAUTION = "CAUTION"
    DEGRADED = "DEGRADED"
    BLOCKED = "BLOCKED"
    REVIEW_REQUIRED = "REVIEW_REQUIRED"
