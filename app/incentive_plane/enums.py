from enum import Enum

class IncentiveClass(Enum):
    ASSURANCE_QUALITY = "assurance_quality"
    IMMUNITY_REVALIDATION = "immunity_revalidation"
    ADAPTATION_EFFECTIVENESS = "adaptation_effectiveness"
    DRIFT_ESCALATION = "drift_escalation"
    BENEFICIARY_PROTECTION = "beneficiary_protection"
    CONTROL_DISCIPLINE = "control_discipline"
    COMPLIANCE_REPORTING = "compliance_reporting"
    SURVEILLANCE_DILIGENCE = "surveillance_diligence"
    RELEASE_SAFETY = "release_safety"
    MIGRATION_INTEGRITY = "migration_integrity"
    FEDERATED_ALIGNMENT = "federated_alignment"
    CROSS_PLANE_BEHAVIOR = "cross_plane_behavior"

class SubjectClass(Enum):
    PERSON = "person"
    ROLE = "role"
    TEAM = "team"
    COMMITTEE = "committee"

class TargetClass(Enum):
    GOOD = "good"
    INCOMPLETE = "incomplete"
    OVER_BROAD = "over_broad"
    GAMEABLE = "gameable"

class LeverClass(Enum):
    POSITIVE = "positive"
    NEGATIVE = "negative"
    MIXED = "mixed"
    INEFFECTIVE = "ineffective"

class RewardClass(Enum):
    ALIGNED = "aligned"
    RISK_ADJUSTED = "risk_adjusted"
    DELAYED = "delayed"
    PERVERSE = "perverse"

class PenaltyClass(Enum):
    PROPORTIONAL = "proportional"
    UNDER_DETERRING = "under_deterring"
    OVER_DETERRING = "over_deterring"
    SYMBOLIC = "symbolic"

class FrictionClass(Enum):
    HEALTHY = "healthy"
    INSUFFICIENT = "insufficient"
    EXCESSIVE = "excessive"
    BYPASSABLE = "bypassable"

class ClawbackClass(Enum):
    VALID = "valid"
    CONDITIONAL = "conditional"
    WEAK = "weak"
    UNAPPLIED = "unapplied"

class ConflictClass(Enum):
    DIRECT = "direct"
    LATENT = "latent"
    BENEFICIARY = "beneficiary"
    HIDDEN = "hidden"

class GamingClass(Enum):
    REWARD_HACKING = "reward_hacking"
    METRIC_CHASING = "metric_chasing"
    THRESHOLD_SURFING = "threshold_surfing"
    ASSURANCE_FARMING = "assurance_farming"

class EquivalenceVerdict(Enum):
    EQUIVALENT = "equivalent"
    DIVERGENT = "divergent"
    BENEFICIARY_COST_DIVERGENT = "beneficiary_cost_divergent"

class TrustVerdict(Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
