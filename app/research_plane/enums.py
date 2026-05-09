import enum


class ResearchClass(enum.Enum):
    REGIME_OBSERVATION = "regime_observation"
    SIGNAL_IDEA = "signal_idea"
    EXECUTION_HYPOTHESIS = "execution_hypothesis"
    RISK_OBSERVATION = "risk_observation"
    DATA_QUALITY_HYPOTHESIS = "data_quality_hypothesis"
    FEATURE_HYPOTHESIS = "feature_hypothesis"
    MODEL_BEHAVIOR_HYPOTHESIS = "model_behavior_hypothesis"
    ALLOCATION_SIZING_HYPOTHESIS = "allocation_sizing_hypothesis"
    STRATEGY_THESIS_CANDIDATE = "strategy_thesis_candidate"
    BENCHMARK_ANOMALY_RESEARCH = "benchmark_anomaly_research"
    EXPLORATORY = "exploratory"


class QuestionClass(enum.Enum):
    CAUSAL = "causal"
    CORRELATIONAL = "correlational"
    DESCRIPTIVE = "descriptive"
    MECHANISTIC = "mechanistic"


class EvidenceClass(enum.Enum):
    SUPPORTIVE = "supportive"
    CONTRADICTORY = "contradictory"
    WEAK = "weak"
    INDIRECT = "indirect"
    SIMULATION_BACKED = "simulation_backed"
    RUNTIME_OBSERVED = "runtime_observed"


class ContradictionClass(enum.Enum):
    DIRECT = "direct"
    PARTIAL = "partial"
    REGIME_SPECIFIC = "regime_specific"
    DATA_QUALITY_BASED = "data_quality_based"
    EXECUTION_DRIVEN = "execution_driven"


class ConfidenceClass(enum.Enum):
    SPECULATIVE = "speculative"
    PLAUSIBLE = "plausible"
    EVIDENCE_SUPPORTED = "evidence_supported"
    EXPERIMENT_READY = "experiment_ready"
    STRATEGY_CANDIDATE = "strategy_candidate"
    INVALIDATED = "invalidated"
    ARCHIVED = "archived"


class ReadinessClass(enum.Enum):
    NOT_READY = "not_ready"
    DATA_READY = "data_ready"
    MODEL_READY = "model_ready"
    EXECUTION_READY = "execution_ready"
    EXPERIMENT_READY = "experiment_ready"


class InvalidationClass(enum.Enum):
    DUE_TO_EVIDENCE = "due_to_evidence"
    DUE_TO_REGIME_MISMATCH = "due_to_regime_mismatch"
    DUE_TO_IMPOSSIBILITY = "due_to_impossibility"
    DUE_TO_OVERLAP = "due_to_overlap"
    DUE_TO_DATA_QUALITY = "due_to_data_quality"


class OverlapSeverity(enum.Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class EquivalenceVerdict(enum.Enum):
    EQUIVALENT = "equivalent"
    PARTIAL_EQUIVALENCE = "partial_equivalence"
    DIVERGENT = "divergent"
    INCOMPARABLE = "incomparable"


class TrustVerdict(enum.Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
