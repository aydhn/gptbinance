from enum import Enum

class DisputeClass(Enum):
    RIGHTS_CLAIM = "rights_claim"
    ENFORCEMENT_APPEAL = "enforcement_appeal"
    LIABILITY_ALLOCATION = "liability_allocation"
    REMEDY_SUFFICIENCY = "remedy_sufficiency"
    CONTRACT_BREACH = "contract_breach"
    COMPLIANCE_FINDING = "compliance_finding"
    FINALITY_REOPEN = "finality_reopen"
    AUTHORITY_MISUSE = "authority_misuse"
    SECURITY_ACTION = "security_action"
    RELEASE_REGRESSION = "release_regression"
    FEDERATED_SCOPE = "federated_scope"

class ComplaintClass(Enum):
    INFORMAL = "informal"
    FORMAL = "formal"
    BENEFICIARY = "beneficiary"
    REGULATOR = "regulator"

class ClaimClass(Enum):
    ASSERTED = "asserted"
    ADMITTED = "admitted"
    CONTESTED = "contested"
    WITHDRAWN = "withdrawn"

class ContestClass(Enum):
    DIRECT = "direct"
    CROSS_FINDING = "cross_finding"
    SCOPE = "scope"
    PROCEDURE = "procedure"

class IssueClass(Enum):
    MERITS = "merits"
    PROCEDURAL = "procedural"
    SCOPE = "scope"
    REMEDIAL = "remedial"

class BurdenClass(Enum):
    PRODUCTION = "production"
    PERSUASION = "persuasion"
    SHIFTED = "shifted"
    UNRESOLVED = "unresolved"

class ReviewStandard(Enum):
    DE_NOVO = "de_novo"
    DEFERENTIAL = "deferential"
    CLEAR_ERROR = "clear_error"
    ABUSE_OF_DISCRETION = "abuse_of_discretion"

class AdmissibilityClass(Enum):
    ADMISSIBLE = "admissible"
    INADMISSIBLE = "inadmissible"
    CONDITIONALLY_ADMISSIBLE = "conditionally_admissible"
    DISPUTED = "disputed"

class RulingClass(Enum):
    PROCEDURAL = "procedural"
    MERITS = "merits"
    APPELLATE = "appellate"
    STAYED = "stayed"

class DispositionClass(Enum):
    RESOLVED_ON_MERITS = "resolved_on_merits"
    SETTLED_UNDER_CONTEST = "settled_under_contest"
    DISMISSED = "dismissed"
    REMANDED = "remanded"

class AppealClass(Enum):
    FILED = "filed"
    ADMITTED = "admitted"
    DENIED = "denied"
    PENDING = "pending"

class EquivalenceVerdict(Enum):
    EQUIVALENT = "equivalent"
    PARTIAL = "partial"
    DIVERGENT = "divergent"

class DisputeTrustVerdict(Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
