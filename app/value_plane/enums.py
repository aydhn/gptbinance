from enum import Enum

class ValueClass(str, Enum):
    STRATEGY_VALUE = "strategy_value"
    RELEASE_VALUE = "release_value"
    RELIABILITY_INVESTMENT_VALUE = "reliability_investment_value"
    SECURITY_HARDENING_VALUE = "security_hardening_value"
    CONTINUITY_INVESTMENT_VALUE = "continuity_investment_value"
    FEATURE_VALUE = "feature_value"
    MODEL_UPGRADE_VALUE = "model_upgrade_value"
    WORKFLOW_AUTOMATION_VALUE = "workflow_automation_value"
    OBSERVABILITY_VALUE = "observability_value"
    COST_OPTIMIZATION_VALUE = "cost_optimization_value"
    CAPACITY_EXPANSION_VALUE = "capacity_expansion_value"
    EXPERIMENT_LEARNING_VALUE = "experiment_learning_value"

class ObjectiveClass(str, Enum):
    GROWTH = "growth"
    RISK_REDUCTION = "risk_reduction"
    RELIABILITY = "reliability"
    LATENCY_OR_FRESHNESS = "latency_or_freshness"
    CAPITAL_EFFICIENCY = "capital_efficiency"
    STRATEGIC_OPTIONALITY = "strategic_optionality"

class KpiClass(str, Enum):
    LEADING = "leading"
    LAGGING = "lagging"

class BenefitClass(str, Enum):
    REVENUE_LIKE = "revenue_like"
    AVOIDED_LOSS = "avoided_loss"
    SPEED_PRODUCTIVITY = "speed_productivity"
    QUALITY_RELIABILITY = "quality_reliability"
    COMPLIANCE_SECURITY_PROTECTION = "compliance_security_protection"
    CAPABILITY_OPTIONALITY = "capability_optionality"

class ImpactClass(str, Enum):
    EXPECTED = "expected"
    REALIZED_SHORT_TERM = "realized_short_term"
    REALIZED_MEDIUM_TERM = "realized_medium_term"
    REALIZED_OPERATIONAL = "realized_operational"
    REALIZED_PROTECTIVE = "realized_protective"
    REALIZED_OPTIONALITY = "realized_optionality"

class BaselineClass(str, Enum):
    HISTORICAL = "historical"
    PEER = "peer"
    NO_ACTION = "no_action"
    PRIOR_RELEASE = "prior_release"
    PRIOR_STRATEGY = "prior_strategy"

class AttributionClass(str, Enum):
    STRATEGY = "strategy"
    RELEASE = "release"
    FEATURE = "feature"
    WORKFLOW = "workflow"

class RoiClass(str, Enum):
    GROSS_ROI = "gross_roi"
    NET_ROI = "net_roi"

class TradeoffClass(str, Enum):
    COST_VS_RELIABILITY = "cost_vs_reliability"
    SPEED_VS_CERTAINTY = "speed_vs_certainty"
    RISK_VS_UPSIDE = "risk_vs_upside"
    SHORT_TERM_VS_LONG_TERM = "short_term_vs_long_term"
    LOCAL_OPTIMIZATION_VS_PORTFOLIO = "local_optimization_vs_portfolio"

class VarianceClass(str, Enum):
    EXPECTED_VS_REALIZED = "expected_vs_realized"
    BASELINE_DRIFT = "baseline_drift"
    ATTRIBUTION_VARIANCE = "attribution_variance"
    KPI_VALUE_DISCONNECT = "kpi_value_disconnect"
    ANOMALY_VARIANCE = "anomaly_variance"
    STRUCTURAL_VARIANCE = "structural_variance"

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
