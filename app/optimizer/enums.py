from enum import Enum


class SearchMode(Enum):
    GRID = "grid"
    RANDOM_SEEDED = "random_seeded"
    BOUNDED_COMBINATIONAL = "bounded_combinational"


class ParameterType(Enum):
    INT = "int"
    FLOAT = "float"
    CATEGORICAL = "categorical"


class ObjectiveComponent(Enum):
    EXPECTANCY = "expectancy"
    PROFIT_FACTOR = "profit_factor"
    DRAWDOWN_PENALTY = "drawdown_penalty"
    LOW_TRADE_COUNT_PENALTY = "low_trade_count_penalty"
    BENCHMARK_RELATIVE_STRENGTH = "benchmark_relative_strength"
    HONESTY_PENALTY = "honesty_penalty"
    ROBUSTNESS_PENALTY = "robustness_penalty"
    COMPLEXITY_PENALTY = "complexity_penalty"


class RankingVerdict(Enum):
    TOP_TIER = "top_tier"
    ACCEPTABLE = "acceptable"
    MARGINAL = "marginal"
    REJECTED = "rejected"


class PruningVerdict(Enum):
    KEEP = "keep"
    PRUNE_GUARDS = "prune_guards"
    PRUNE_PERFORMANCE = "prune_performance"


class GuardSeverity(Enum):
    INFO = "info"
    CAUTION = "caution"
    WARNING = "warning"
    FAIL = "fail"


class OptimizerStatus(Enum):
    INITIALIZED = "initialized"
    GENERATING_CANDIDATES = "generating_candidates"
    RUNNING_TRIALS = "running_trials"
    RANKING = "ranking"
    COMPLETED = "completed"
    FAILED = "failed"


class ExperimentStage(Enum):
    CANDIDATE_GENERATION = "candidate_generation"
    TRIAL_EXECUTION = "trial_execution"
    OBJECTIVE_SCORING = "objective_scoring"
    GUARD_EVALUATION = "guard_evaluation"
    RANKING = "ranking"
