from enum import Enum

class ScenarioClass(Enum):
    RELEASE = "release"
    ACTIVATION = "activation"
    MIGRATION = "migration"
    INCIDENT_RECOVERY = "incident_recovery"
    CONTINUITY_FAILOVER = "continuity_failover"
    SECURITY_BREACH = "security_breach"
    CONTRACT_BREAK = "contract_break"
    ENVIRONMENT_DRIFT = "environment_drift"
    CHANGE_COLLISION = "change_collision"
    CAPACITY_PRESSURE = "capacity_pressure"
    PORTFOLIO_PRIORITY = "portfolio_priority"
    CONSTITUTIONAL_META = "constitutional_meta"

class TaxonomyClass(Enum):
    BASELINE = "baseline"
    WHAT_IF = "what_if"
    COUNTERFACTUAL = "counterfactual"
    STRESS = "stress"
    RECOVERY = "recovery"
    DECISION = "decision"

class BaselineClass(Enum):
    CURRENT_STATE = "current_state"
    NO_ACTION = "no_action"
    PRIOR_RELEASE = "prior_release"
    PRIOR_POLICY = "prior_policy"

class AssumptionClass(Enum):
    BOUNDED = "bounded"
    EXTERNAL = "external"
    DEPENDENCY = "dependency"
    CORRELATION = "correlation"

class ShockClass(Enum):
    SINGLE = "single"
    COMPOUND = "compound"
    VENDOR = "vendor"
    LATENCY_LIQUIDITY = "latency_liquidity"
    POLICY = "policy"

class InterventionClass(Enum):
    ROLLBACK = "rollback"
    FAILOVER = "failover"
    FREEZE = "freeze"
    CAPACITY_ALLOCATION = "capacity_allocation"
    COMMUNICATION = "communication"

class BranchClass(Enum):
    EXPLICIT_CONDITION = "explicit_condition"
    MUTUALLY_EXCLUSIVE = "mutually_exclusive"
    UNCERTAIN = "uncertain"

class OutcomeClass(Enum):
    OPERATIONAL = "operational"
    CONSTITUTIONAL = "constitutional"
    RECOVERY = "recovery"
    BUSINESS = "business"

class RobustnessClass(Enum):
    ROBUST_BASELINE = "robust_baseline"
    ROBUST_MODERATE = "robust_moderate"
    BRITTLE_COMPOUND = "brittle_compound"
    RECOVERY_CAPABLE = "recovery_capable"

class StressClass(Enum):
    NORMAL_RULE = "normal_rule"
    EXCEPTION_HEAVY = "exception_heavy"
    WAIVER_HEAVY = "waiver_heavy"
    BLOCKER_ESCALATION = "blocker_escalation"

class EquivalenceVerdict(Enum):
    EQUIVALENT = "equivalent"
    PARTIAL = "partial"
    DIVERGENT = "divergent"

class TrustVerdict(Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
