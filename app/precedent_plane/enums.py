from enum import Enum

class PrecedentClass(Enum):
    CONSTITUTIONAL = "constitutional"
    CONTRACTUAL = "contractual"
    POLICY = "policy"
    COMPLIANCE = "compliance"
    REMEDY = "remedy"
    JURISDICTION = "jurisdiction"
    LOCAL = "local"
    FEDERATED = "federated"
    CROSS_PLANE_CASE_CONSISTENCY = "cross_plane_case_consistency"
    CUSTOMER_HARM = "customer_harm"
    AUTONOMY_OVERRIDE = "autonomy_override"
    INCIDENT_CLOSURE = "incident_closure"
    COMMITMENT_BREACH = "commitment_breach"
    RELEASE_GATE = "release_gate"
    MIGRATION_ACCEPTANCE = "migration_acceptance"

class CaseClass(Enum):
    RESOLVED = "resolved"
    OPEN = "open"
    SUPERSEDED = "superseded"
    DISPUTED = "disputed"

class HoldingClass(Enum):
    CONTROLLING = "controlling"
    NARROW = "narrow"
    BROAD = "broad"
    CONDITIONAL = "conditional"

class RationaleClass(Enum):
    PRIMARY = "primary"
    SUPPORTING = "supporting"
    POLICY = "policy"
    REMEDY = "remedy"

class FactorClass(Enum):
    MATERIAL = "material"
    DISQUALIFYING = "disqualifying"
    BENEFICIARY = "beneficiary"
    ENVIRONMENT = "environment"

class ApplicabilityClass(Enum):
    DIRECTLY_APPLICABLE = "directly_applicable"
    CONDITIONALLY_APPLICABLE = "conditionally_applicable"
    NOT_APPLICABLE = "not_applicable"
    UNCERTAIN = "uncertain"

class AuthorityClass(Enum):
    CONSTITUTIONALLY_BINDING = "constitutionally_binding"
    CONTRACTUALLY_BINDING = "contractually_binding"
    POLICY_BINDING = "policy_binding"
    SCOPE_BOUND_BINDING = "scope_bound_binding"
    LOCAL_PERSUASIVE = "local_persuasive"
    FEDERATED_PERSUASIVE = "federated_persuasive"
    SCENARIO_PERSUASIVE = "scenario_persuasive"
    WEAK_PERSUASIVE = "weak_persuasive"

class AnalogyClass(Enum):
    CLOSE = "close"
    PARTIAL = "partial"
    SCOPE_LIMITED = "scope_limited"
    FAKE = "fake"

class DistinctionClass(Enum):
    MATERIAL = "material"
    SCOPE = "scope"
    BENEFICIARY = "beneficiary"
    TEMPORAL = "temporal"

class CarveoutClass(Enum):
    NARROW = "narrow"
    TENANT = "tenant"
    ENVIRONMENT = "environment"
    BENEFICIARY = "beneficiary"

class ExceptionClass(Enum):
    EXCEPTIONAL_ALLOWANCE = "exceptional_allowance"
    EMERGENCY = "emergency"
    ONE_OFF = "one_off"
    INVALID_REPEATED = "invalid_repeated"

class ConflictClass(Enum):
    OUTCOME = "outcome"
    HOLDING = "holding"
    RATIONALE = "rationale"
    SCOPE = "scope"

class HierarchyClass(Enum):
    CONSTITUTIONAL_OVER_POLICY = "constitutional_over_policy"
    CONTRACTUAL_OVER_HABIT = "contractual_over_habit"
    LOCAL_VS_FEDERATED = "local_vs_federated"

class ConsistencyClass(Enum):
    CONSISTENT = "consistent"
    INCONSISTENT_VALID_DISTINCTION = "inconsistent_valid_distinction"
    INCONSISTENT_NO_BASIS = "inconsistent_no_basis"

class PrecedentTrustVerdict(Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"

class PrecedentEquivalenceVerdict(Enum):
    EQUIVALENT = "equivalent"
    DIVERGENT = "divergent"
