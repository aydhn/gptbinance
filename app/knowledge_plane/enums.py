from enum import Enum

class KnowledgeClass(str, Enum):
    POLICY = "policy"
    STANDARD = "standard"
    RUNBOOK = "runbook"
    PLAYBOOK = "playbook"
    SOP = "sop"
    CHECKLIST = "checklist"
    MEMO = "memo"

class SourceClass(str, Enum):
    CANONICAL = "canonical"
    MIRRORED = "mirrored"
    SUPERSEDED = "superseded"
    LOCAL = "local"
    GENERATED = "generated"

class TaxonomyClass(str, Enum):
    POLICY = "policy"
    STANDARD = "standard"
    SOP = "sop"
    CHECKLIST = "checklist"
    RUNBOOK = "runbook"
    PLAYBOOK = "playbook"
    ARCHITECTURE_NOTE = "architecture_note"
    DECISION_MEMO = "decision_memo"
    TROUBLESHOOTING_NOTE = "troubleshooting_note"

class StandardClass(str, Enum):
    MANDATORY = "mandatory"
    ADVISORY = "advisory"

class RunbookClass(str, Enum):
    INCIDENT = "incident"
    RELEASE_ROLLBACK = "release_rollback"
    FAILOVER = "failover"
    OPERATIONAL_RECOVERY = "operational_recovery"

class PlaybookClass(str, Enum):
    ESCALATION = "escalation"
    SECURITY_RESPONSE = "security_response"
    RELEASE_MANAGEMENT = "release_management"
    MIGRATION = "migration"
    STAGED_EXECUTION = "staged_execution"

class ApplicabilityClass(str, Enum):
    ENVIRONMENT = "environment"
    ROLE = "role"
    WORKFLOW = "workflow"

class FreshnessClass(str, Enum):
    FRESH = "fresh"
    REVIEW_DUE = "review_due"
    STALE = "stale"
    EXPIRED = "expired"

class ReviewClass(str, Enum):
    SCHEDULED = "scheduled"
    TRIGGERED = "triggered"
    INCIDENT_TRIGGERED = "incident_triggered"
    RELEASE_TRIGGERED = "release_triggered"

class SupersessionClass(str, Enum):
    FULL = "full"
    PARTIAL = "partial"

class ConflictClass(str, Enum):
    OVERLAP = "overlap"
    CONTRADICTION = "contradiction"

class AdoptionClass(str, Enum):
    FULL = "full"
    PARTIAL = "partial"
    NONE = "none"

class AttestationClass(str, Enum):
    READ_AND_UNDERSTOOD = "read_and_understood"
    REVIEW_COMPLETE = "review_complete"
    DRILL_PROVEN = "drill_proven"

class EquivalenceVerdict(str, Enum):
    EQUIVALENT = "equivalent"
    DIVERGENT = "divergent"

class TrustVerdict(str, Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
