from enum import Enum

class AccountabilityClass(str, Enum):
    ASSURANCE_FAILURE = "assurance_failure"
    STALE_SURVEILLANCE = "stale_surveillance"
    OVERRIDE_ABUSE = "override_abuse"
    ADAPTATION_FAILURE = "adaptation_failure"
    DRIFT_ESCALATION_FAILURE = "drift_escalation_failure"
    BENEFICIARY_HARM = "beneficiary_harm"
    CONTROL_CREEP = "control_creep"
    COMPLIANCE_OMISSION = "compliance_omission"
    RELEASE_REGRESSION = "release_regression"
    MIGRATION_RELAPSE = "migration_relapse"
    FEDERATED_GAP = "federated_gap"
    CROSS_PLANE_DUTY_CONSEQUENCE = "cross_plane_duty_consequence"

class SubjectClass(str, Enum):
    PERSON = "person"
    ROLE = "role"
    COMMITTEE = "committee"
    SYSTEM_OWNER = "system_owner"

class DutyClass(str, Enum):
    ACTIVE = "active"
    TIME_BOUND = "time_bound"
    STANDING = "standing"
    AMBIGUOUS = "ambiguous"

class BreachClass(str, Enum):
    MATERIAL = "material"
    PROCEDURAL = "procedural"
    BENEFICIARY_IMPACT = "beneficiary_impact"
    HIDDEN = "hidden"

class EscalationClass(str, Enum):
    LATE = "late"
    MISSING = "missing"
    INSUFFICIENT = "insufficient"
    BURIED = "buried"

class SanctionClass(str, Enum):
    WARNING = "warning"
    ACCESS_RESTRICTION = "access_restriction"
    ROLE_SUSPENSION = "role_suspension"
    SEVERE = "severe"

class RemediationClass(str, Enum):
    CORRECTIVE = "corrective"
    MONITORING = "monitoring"
    RETRAINING = "retraining"
    INCOMPLETE = "incomplete"

class AppealClass(str, Enum):
    VALID = "valid"
    PENDING = "pending"
    FRIVOLOUS = "frivolous"
    BLOCKED = "blocked"

class ReinstatementClass(str, Enum):
    JUSTIFIED = "justified"
    CONDITIONAL = "conditional"
    PREMATURE = "premature"
    MISSING_CRITERIA = "missing_criteria"

class EquivalenceVerdict(str, Enum):
    EQUIVALENT = "equivalent"
    DIVERGENT = "divergent"

class TrustVerdict(str, Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
