from enum import Enum

class AdversarialClass(str, Enum):
    METRIC_GAMING = "metric_gaming"
    EVIDENCE_POISONING = "evidence_poisoning"
    REVIEW_EVASION = "review_evasion"
    THRESHOLD_GAMING = "threshold_gaming"
    SEMANTIC_LAUNDERING = "semantic_laundering"
    TIMING_MANIPULATION = "timing_manipulation"
    AUTONOMY_MASKING = "autonomy_masking"
    FEDERATED_ABUSE = "federated_abuse"
    IDENTITY_BORROWING = "identity_borrowing"
    CONTRACT_ABUSE = "contract_abuse"
    CONTROL_CIRCUMVENTION = "control_circumvention"
    CROSS_PLANE_STRATEGIC_ABUSE = "cross_plane_strategic_abuse"
    UNKNOWN = "unknown"

class ActorClass(str, Enum):
    HUMAN_OPERATOR = "human_operator"
    AUTONOMOUS_AGENT = "autonomous_agent"
    PARTNER = "partner"
    VENDOR = "vendor"
    INSIDER = "insider"
    FEDERATED = "federated"
    SYSTEM_WORKFLOW = "system_workflow"

class IncentiveClass(str, Enum):
    SPEED = "speed"
    METRIC_IMPROVEMENT = "metric_improvement"
    CONCEALMENT = "concealment"
    COST_AVOIDANCE = "cost_avoidance"
    STATUS_REWARD = "status_reward"
    BURDEN_SHIFTING = "burden_shifting"

class SurfaceClass(str, Enum):
    APPROVAL = "approval"
    THRESHOLD = "threshold"
    SEMANTIC = "semantic"
    EVIDENCE = "evidence"
    AUTONOMY = "autonomy"
    FEDERATION = "federation"

class ExploitClass(str, Enum):
    DIRECT = "direct"
    CHAINED = "chained"
    LATENT = "latent"
    OPPORTUNISTIC = "opportunistic"

class EvasionClass(str, Enum):
    REVIEW_EVASION = "review_evasion"
    AUDIT_EVASION = "audit_evasion"
    THRESHOLD_EVASION = "threshold_evasion"
    DETECTION_EVASION = "detection_evasion"

class GamingClass(str, Enum):
    METRIC_GAMING = "metric_gaming"
    THRESHOLD_GAMING = "threshold_gaming"
    REVIEW_COMPLETION_GAMING = "review_completion_gaming"
    READINESS_GAMING = "readiness_gaming"

class PoisoningClass(str, Enum):
    DATA_POISONING = "data_poisoning"
    EVIDENCE_POISONING = "evidence_poisoning"
    REVIEW_POISONING = "review_poisoning"
    MODEL_FEEDBACK_POISONING = "model_feedback_poisoning"

class SuspicionClass(str, Enum):
    WEAK = "weak"
    MATERIAL = "material"
    ESCALATING = "escalating"
    DISPROVEN = "disproven"

class ConfirmationClass(str, Enum):
    PARTIAL = "partial"
    CONFIRMED_EXPLOIT = "confirmed_exploit"
    EXPLOIT_FAMILY = "exploit_family"

class EquivalenceVerdict(str, Enum):
    EQUIVALENT = "equivalent"
    PARTIAL_EQUIVALENCE = "partial_equivalence"
    DIVERGENT = "divergent"
    UNKNOWN = "unknown"

class TrustVerdict(str, Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
