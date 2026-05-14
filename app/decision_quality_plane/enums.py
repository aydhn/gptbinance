from enum import Enum

class DecisionClass(str, Enum):
    STRATEGY_PROMOTION = "strategy_promotion"
    RELEASE_ROLLOUT = "release_rollout"
    ACTIVATION_PROGRESSION = "activation_progression"
    RISK_OVERRIDE = "risk_override"
    ALLOCATION_REGIME = "allocation_regime"
    EXECUTION_INTERVENTION = "execution_intervention"
    WORKFLOW_RERUN = "workflow_rerun"
    INCIDENT_CONTAINMENT = "incident_containment"
    FAILOVER = "failover"
    MIGRATION_CUTOVER = "migration_cutover"
    EXPERIMENT_WINNER = "experiment_winner"
    CAPITAL_REALLOCATION = "capital_reallocation"

class RecommendationClass(str, Enum):
    MODEL_DRIVEN = "model_driven"
    RESEARCH_DRIVEN = "research_driven"
    EXPERIMENT_DRIVEN = "experiment_driven"
    OPERATOR_DRIVEN = "operator_driven"
    POLICY_BOUNDED = "policy_bounded"

class OptionClass(str, Enum):
    BASE_CASE = "base_case"
    CONSERVATIVE = "conservative"
    AGGRESSIVE = "aggressive"
    DEFER_NO_OP = "defer_no_op"
    ROLLBACK = "rollback"
    STOP_TRADING = "stop_trading"

class EvidenceClass(str, Enum):
    RESEARCH = "research"
    SIMULATION = "simulation"
    EXPERIMENT = "experiment"
    MARKET_TRUTH = "market_truth"
    RISK_PERFORMANCE = "risk_performance"

class AssumptionClass(str, Enum):
    MARKET_STATE = "market_state"
    LIQUIDITY = "liquidity"
    RELIABILITY = "reliability"
    DEPENDENCY = "dependency"

class UncertaintyClass(str, Enum):
    MODEL = "model"
    DATA = "data"
    MARKET = "market"
    OPERATIONAL = "operational"
    STRUCTURAL = "structural"

class ConfidenceClass(str, Enum):
    VERY_HIGH = "very_high"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    VERY_LOW = "very_low"
    UNKNOWN = "unknown"

class OutcomeClass(str, Enum):
    SUCCESS = "success"
    PARTIAL_SUCCESS = "partial_success"
    FAILURE = "failure"
    AMBIGUOUS = "ambiguous"
    PENDING = "pending"

class CalibrationClass(str, Enum):
    CALIBRATED = "calibrated"
    OVERCONFIDENT = "overconfident"
    UNDERCONFIDENT = "underconfident"

class EquivalenceVerdict(str, Enum):
    EQUIVALENT = "equivalent"
    PARTIAL = "partial"
    DIVERGENT = "divergent"

class TrustVerdict(str, Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
