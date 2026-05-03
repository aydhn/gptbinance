from enum import Enum, auto


class WorkloadType(str, Enum):
    FEATURE_BUILD = "FEATURE_BUILD"
    GOVERNANCE_REFRESH = "GOVERNANCE_REFRESH"
    ANALYTICS_BATCH = "ANALYTICS_BATCH"
    STRATEGY_EVAL = "STRATEGY_EVAL"
    REGIME_EVAL = "REGIME_EVAL"
    RISK_PORTFOLIO = "RISK_PORTFOLIO"
    ML_INFERENCE_BATCH = "ML_INFERENCE_BATCH"
    PAPER_RUNTIME_CYCLE = "PAPER_RUNTIME_CYCLE"
    TESTNET_EXECUTION_SMOKE = "TESTNET_EXECUTION_SMOKE"
    RELEASE_VERIFY = "RELEASE_VERIFY"


class ProfileScope(str, Enum):
    COMPONENT = "COMPONENT"
    WORKFLOW = "WORKFLOW"
    END_TO_END = "END_TO_END"


class ResourceType(str, Enum):
    CPU = "CPU"
    MEMORY = "MEMORY"
    DISK_IO = "DISK_IO"
    NETWORK = "NETWORK"


class BudgetSeverity(str, Enum):
    SOFT = "SOFT"
    HARD = "HARD"


class HostClass(str, Enum):
    LOCAL_MINIMAL = "LOCAL_MINIMAL"
    LOCAL_AVERAGE = "LOCAL_AVERAGE"
    LOCAL_ENHANCED = "LOCAL_ENHANCED"
    WORKSTATION_GPU_OPTIONAL = "WORKSTATION_GPU_OPTIONAL"


class RegressionSeverity(str, Enum):
    BENIGN = "BENIGN"
    MINOR = "MINOR"
    MAJOR = "MAJOR"
    CRITICAL = "CRITICAL"


class ReadinessVerdict(str, Enum):
    READY = "READY"
    CAUTION = "CAUTION"
    NOT_RECOMMENDED = "NOT_RECOMMENDED"


class LatencyPercentile(str, Enum):
    P50 = "P50"
    P95 = "P95"
    P99 = "P99"
    MAX = "MAX"


class BottleneckType(str, Enum):
    CPU_BOUND = "CPU_BOUND"
    MEMORY_BOUND = "MEMORY_BOUND"
    IO_BOUND = "IO_BOUND"
    NETWORK_BOUND = "NETWORK_BOUND"
    LOCK_CONTENTION = "LOCK_CONTENTION"
    UNKNOWN = "UNKNOWN"


class PerfVerdict(str, Enum):
    PASS = "PASS"
    FAIL = "FAIL"
    WARNING = "WARNING"
