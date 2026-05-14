from enum import Enum

class CostClass(str, Enum):
    FIXED = "fixed"
    VARIABLE = "variable"
    USAGE_BASED = "usage_based"
    FEE_BASED = "fee_based"

class SpendClass(str, Enum):
    ACTUAL = "actual"
    ACCRUED = "accrued"
    ESTIMATED = "estimated"
    PENDING = "pending"
    COMMITTED = "committed"

class FeeClass(str, Enum):
    EXCHANGE_FEE = "exchange_fee"
    MARKET_DATA_FEE = "market_data_fee"
    EGRESS_FEE = "egress_fee"
    VENDOR_API_FEE = "vendor_api_fee"
    NETWORK_ROUTING_FEE = "network_routing_fee"

class BudgetClass(str, Enum):
    HARD = "hard"
    SOFT = "soft"
    ADVISORY = "advisory"
    TEAM = "team"
    WORKLOAD = "workload"

class GuardrailClass(str, Enum):
    MAX_BURN = "max_burn"
    QUOTA_COST = "quota_cost"
    UNIT_COST = "unit_cost"
    BUDGET_EXHAUSTION = "budget_exhaustion"
    EXPERIMENTAL_SPEND = "experimental_spend"

class AllocationClass(str, Enum):
    DIRECT = "direct"
    WEIGHTED = "weighted"
    USAGE = "usage"
    RESERVATION = "reservation"
    SHARED_OVERHEAD = "shared_overhead"

class AmortizationClass(str, Enum):
    RESERVED_CAPACITY = "reserved_capacity"
    UPFRONT_COMMITMENT = "upfront_commitment"
    MODEL_TRAINING = "model_training"
    MIGRATION_ONE_OFF = "migration_one_off"
    STANDBY_INVESTMENT = "standby_investment"

class UnitEconomicsClass(str, Enum):
    PER_INFERENCE = "per_inference"
    PER_ORDER = "per_order"
    PER_WORKFLOW = "per_workflow"
    PER_RELEASE = "per_release"
    PER_STRATEGY_COHORT = "per_strategy_cohort"
    PER_DATA_GIGABYTE = "per_data_gigabyte"

class VarianceClass(str, Enum):
    BUDGET_VARIANCE = "budget_variance"
    FORECAST_VARIANCE = "forecast_variance"
    UNIT_ECONOMICS_VARIANCE = "unit_economics_variance"
    SEASONAL_VARIANCE = "seasonal_variance"

class CostEquivalenceVerdict(str, Enum):
    EQUIVALENT = "equivalent"
    PARTIAL_EQUIVALENT = "partial_equivalent"
    DIVERGENT = "divergent"
    UNKNOWN = "unknown"

class CostTrustVerdict(str, Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
