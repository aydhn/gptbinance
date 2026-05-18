from enum import Enum

class ConstitutionClass(str, Enum):
    RELEASE = "release"
    ACTIVATION = "activation"
    MIGRATION = "migration"
    INCIDENT = "incident"
    SECURITY_COMPLIANCE = "security_compliance"
    CONTINUITY_RELIABILITY = "continuity_reliability"
    CHANGE_CONTRACT = "change_contract"
    ENVIRONMENT_ASSURANCE = "environment_assurance"
    STATE_INTEGRITY = "state_integrity"
    OPERATING_MODEL_KNOWLEDGE = "operating_model_knowledge"
    PORTFOLIO_PROGRAM = "portfolio_program"
    CROSS_PLANE_META = "cross_plane_meta"

class RuleTaxonomy(str, Enum):
    BLOCKER = "blocker"
    CAUTION = "caution"
    REVIEW_REQUIRED = "review_required"
    VETO = "veto"
    WAIVER_ELIGIBLE = "waiver_eligible"
    OVERRIDE_PROHIBITED = "override_prohibited"

class VerdictClass(str, Enum):
    PASS = "pass"
    PASS_WITH_CAUTION = "pass_with_caution"
    ELIGIBLE_WITH_WAIVER = "eligible_with_waiver"
    REVIEW_REQUIRED = "review_required"
    BLOCKED = "blocked"

class TrustVerdict(str, Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"

class PrecedenceClass(str, Enum):
    PLANE_PRECEDENCE = "plane_precedence"
    DOMAIN_PRECEDENCE = "domain_precedence"
    ACTION_PRECEDENCE = "action_precedence"

class AuthorityClass(str, Enum):
    DOMAIN_AUTHORITY = "domain_authority"
    OBJECT_AUTHORITY = "object_authority"
    ACTION_AUTHORITY = "action_authority"

class ConflictClass(str, Enum):
    BLOCKER_VS_TRUSTED = "blocker_vs_trusted"
    CAUTION_ACCUMULATION = "caution_accumulation"
    AUTHORITY_CONFLICT = "authority_conflict"
    STALE_VS_FRESH = "stale_vs_fresh"

class WaiverClass(str, Enum):
    SCOPE_BOUND = "scope_bound"
    TIME_BOUND = "time_bound"
    EVIDENCE_BACKED = "evidence_backed"

class OverrideClass(str, Enum):
    EMERGENCY = "emergency"
    AUDITED = "audited"

class EligibilityClass(str, Enum):
    RELEASE = "release"
    ACTIVATION = "activation"
    MIGRATION = "migration"
    EMERGENCY_ACTION = "emergency_action"

class EquivalenceVerdict(str, Enum):
    EQUIVALENT = "equivalent"
    PARTIAL = "partial"
    DIVERGENT = "divergent"
