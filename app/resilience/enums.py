from enum import Enum


class ExperimentType(str, Enum):
    FAULT_INJECTION = "fault_injection"
    STRESS_TEST = "stress_test"
    DEGRADATION_TEST = "degradation_test"


class FaultType(str, Enum):
    LATENCY_INJECTION = "latency_injection"
    STALE_DATA_INJECTION = "stale_data_injection"
    EXCEPTION_BURST = "exception_burst"
    TIMEOUT_SIMULATION = "timeout_simulation"
    MALFORMED_PAYLOAD = "malformed_payload"
    WRITE_FAILURE = "write_failure"
    PARTIAL_READ_FAILURE = "partial_read_failure"
    NOTIFIER_DROP = "notifier_drop"
    CHECKSUM_MISMATCH = "checksum_mismatch"
    DRIFT_SPIKE = "drift_spike"
    SAFE_STUB_CONFIG = "safe_stub_config"


class TargetComponent(str, Enum):
    DATA_STREAM = "data_stream"
    EXECUTION_GATEWAY = "execution_gateway"
    SCHEDULER = "scheduler"
    STORAGE = "storage"
    NOTIFIER = "notifier"
    RECONCILIATION = "reconciliation"
    INTEGRITY_CHECKER = "integrity_checker"
    ML_INFERENCE = "ml_inference"
    PORTFOLIO_MANAGER = "portfolio_manager"


class StressType(str, Enum):
    MODERATE_EVENT_BURST = "moderate_event_burst"
    HEAVY_EVENT_BURST = "heavy_event_burst"
    QUEUE_PRESSURE = "queue_pressure"
    ALERT_BURST = "alert_burst"
    LARGE_BATCH_SIMULATION = "large_batch_simulation"


class AssertionVerdict(str, Enum):
    PASS = "pass"
    FAIL = "fail"
    SKIPPED = "skipped"
    ERROR = "error"


class ResilienceSeverity(str, Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFO = "info"


class GateVerdict(str, Enum):
    ALLOW = "allow"
    BLOCK = "block"
    CAUTION = "caution"


class DegradationMode(str, Enum):
    HALT = "halt"
    DRAIN = "drain"
    PAUSE = "pause"
    SAFE_FALLBACK = "safe_fallback"
    IGNORE = "ignore"


class ExperimentStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    GATED = "gated"
    ASSERTING = "asserting"
    RECOVERING = "recovering"
    COMPLETED = "completed"
    FAILED = "failed"
    ABORTED = "aborted"


class SafeScope(str, Enum):
    SIMULATION = "simulation"
    PAPER = "paper"
    TESTNET = "testnet"
    SHADOW = "shadow"
