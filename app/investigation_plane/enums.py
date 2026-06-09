from enum import Enum

class InvestigationClass(Enum):
    OVERSIGHT_TRIGGERED = "oversight_triggered"
    APPEAL_REMAND = "appeal_remand"
    EXCEPTION_ABUSE = "exception_abuse"
    SUSPENSION_BYPASS = "suspension_bypass"
    STEWARDSHIP_BURDEN = "stewardship_burden"
    LEGITIMACY_HARM = "legitimacy_harm"
    VIABILITY_ANOMALY = "viability_anomaly"
    AUTONOMY_INCIDENT = "autonomy_incident"
    ACCOUNTABILITY_BREACH = "accountability_breach"
    ASSURANCE_INTEGRITY = "assurance_integrity"
    FEDERATED_COMPLAINT = "federated_complaint"
    CROSS_PLANE_FACT_FINDING = "cross_plane_fact_finding"

class AllegationClass(Enum):
    CLEAR = "clear"
    WEAK = "weak"
    MALICIOUS_SIGNAL = "malicious_signal"
    UNSTRUCTURED = "unstructured"

class IntakeClass(Enum):
    VALID = "valid"
    INCOMPLETE = "incomplete"
    DELAYED = "delayed"
    SILENT_DISCARDED = "silent_discarded"

class TriageClass(Enum):
    URGENT = "urgent"
    STANDARD = "standard"
    DEPRIORITIZED = "deprioritized"
    BIASED = "biased"

class ScopeClass(Enum):
    BOUNDED = "bounded"
    EVOLVING = "evolving"
    OVERBROAD = "overbroad"
    TRUNCATED = "truncated"

class EvidenceClass(Enum):
    PRIMARY = "primary"
    SECONDARY = "secondary"
    TAINTED = "tainted"
    INADMISSIBLE = "inadmissible"

class CustodyClass(Enum):
    CLEAN = "clean"
    PARTIAL = "partial"
    BROKEN = "broken"
    UNDOCUMENTED_TRANSFER = "undocumented_transfer"

class InterviewClass(Enum):
    FAIR = "fair"
    LIMITED = "limited"
    COERCIVE_RISK = "coercive_risk"
    SKIPPED_KEY = "skipped_key"

class SubstantiationClass(Enum):
    SUBSTANTIATED = "substantiated"
    PARTIALLY_SUBSTANTIATED = "partially_substantiated"
    INCONCLUSIVE = "inconclusive"
    UNSUBSTANTIATED_CONCERNING = "unsubstantiated_concerning"

class DebtClass(Enum):
    BACKLOG = "backlog"
    PRESERVATION = "preservation"
    EXCULPATORY_REVIEW = "exculpatory_review"
    INTERVIEW_GAP = "interview_gap"
    CHAIN_BREAK = "chain_break"

class TrustVerdict(Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
