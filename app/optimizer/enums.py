from enum import Enum

class SearchMode(str, Enum):
    GRID = "grid"
    RANDOM = "random"

class ParameterType(str, Enum):
    INT = "int"
    FLOAT = "float"
    CATEGORICAL = "categorical"

class ObjectiveComponent(str, Enum):
    EXPECTANCY = "expectancy"
    DRAWDOWN = "drawdown"
    TRADE_COUNT = "trade_count"
    BENCHMARK_RELATIVE = "benchmark_relative"
    HONESTY_PENALTY = "honesty_penalty"
    ROBUSTNESS_PENALTY = "robustness_penalty"

class RankingVerdict(str, Enum):
    TOP_CANDIDATE = "top_candidate"
    ACCEPTABLE = "acceptable"
    REJECTED = "rejected"

class PruningVerdict(str, Enum):
    KEEP = "keep"
    PRUNE = "prune"

class GuardSeverity(str, Enum):
    INFO = "info"
    WARNING = "warning"
    CRITICAL = "critical"
    FAIL = "fail"

class OptimizerStatus(str, Enum):
    INITIALIZED = "initialized"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"

class ExperimentStage(str, Enum):
    SETUP = "setup"
    GENERATION = "generation"
    EXECUTION = "execution"
    EVALUATION = "evaluation"
    RANKING = "ranking"
    COMPLETED = "completed"
