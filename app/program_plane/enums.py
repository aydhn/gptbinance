from enum import Enum

class ProgramClass(str, Enum):
    RELEASE_DELIVERY = "release_delivery"
    MIGRATION_DELIVERY = "migration_delivery"
    SECURITY_REMEDIATION = "security_remediation"
    RELIABILITY_HARDENING = "reliability_hardening"
    CONTINUITY_ENABLEMENT = "continuity_enablement"
    PLATFORM_REFACTOR = "platform_refactor"
    WORKFLOW_AUTOMATION = "workflow_automation"
    MODEL_UPGRADE = "model_upgrade"
    FEATURE_ROLLOUT = "feature_rollout"
    OBSERVABILITY_IMPROVEMENT = "observability_improvement"
    COMPLIANCE_CLOSURE = "compliance_closure"
    STRATEGIC_RESEARCH_GRADUATION = "strategic_research_graduation"

class MilestoneClass(str, Enum):
    DESIGN = "design"
    DEPENDENCY_UNBLOCK = "dependency_unblock"
    INTEGRATION = "integration"
    RELEASE_READY = "release_ready"
    ACTIVATION_SAFE = "activation_safe"

class DeliverableClass(str, Enum):
    CODE = "code"
    CONFIG = "config"
    DATA = "data"
    MODEL = "model"
    REVIEW = "review"
    RELEASE_BUNDLE = "release_bundle"
    EVIDENCE = "evidence"

class DependencyClass(str, Enum):
    HARD = "hard"
    SOFT = "soft"
    SEQUENCE = "sequence"
    ACCEPTANCE = "acceptance"
    RESOURCE = "resource"

class BlockerClass(str, Enum):
    HARD = "hard"
    SOFT = "soft"
    REVIEW = "review"
    CAPACITY = "capacity"
    POLICY = "policy"

class HandoffClass(str, Enum):
    REQUESTED = "requested"
    READY_FOR_HANDOFF = "ready_for_handoff"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    STALE = "stale"

class CadenceClass(str, Enum):
    WEEKLY_DELIVERY = "weekly_delivery"
    REVIEW = "review"
    DEPENDENCY_SYNC = "dependency_sync"
    ESCALATION = "escalation"

class SlipClass(str, Enum):
    MILESTONE_SLIP = "milestone_slip"
    CASCADING_SLIP = "cascading_slip"
    ABSORBED_SLIP = "absorbed_slip"
    DEADLINE_MISS = "deadline_miss"
    CRITICAL_PATH_SLIP = "critical_path_slip"

class EscalationClass(str, Enum):
    BLOCKER = "blocker"
    DEADLINE = "deadline"
    DEPENDENCY_OWNER = "dependency_owner"
    STAFFING = "staffing"
    CROSS_PROGRAM = "cross_program"

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
