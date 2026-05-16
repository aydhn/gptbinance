from enum import Enum, auto

class PortfolioObjectClass(Enum):
    INITIATIVE = auto()
    WORKSTREAM = auto()
    ROADMAP_ITEM = auto()
    EXPERIMENT = auto()
    MAINTENANCE = auto()
    DEBT_REDUCTION = auto()
    RESEARCH = auto()

class PortfolioThemeClass(Enum):
    STRATEGIC = auto()
    PROTECTIVE = auto()
    EXPLORATORY = auto()
    EFFICIENCY = auto()
    CAPABILITY = auto()
    COMPLIANCE = auto()

class InvestmentBucketClass(Enum):
    CORE_DELIVERY = auto()
    RESILIENCE_PROTECTION = auto()
    EXPLORATION = auto()
    MAINTENANCE_DEBT = auto()
    MANDATORY_COMPLIANCE = auto()

class CommitmentClass(Enum):
    INVESTIGATED = auto()
    PRIORITIZED = auto()
    PLANNED = auto()
    FUNDED = auto()
    STAFFED = auto()
    CAPACITY_RESERVED = auto()
    EXECUTION_READY = auto()

class FundingClass(Enum):
    UNFUNDED = auto()
    STAGE_DISCOVERY = auto()
    STAGE_PILOT = auto()
    STAGE_CANARY = auto()
    STAGE_EXPANSION = auto()
    STAGE_SUSTAIN = auto()
    FULLY_FUNDED = auto()

class WIPClass(Enum):
    WITHIN_LIMITS = auto()
    SATURATED = auto()
    OVER_LIMIT = auto()

class PortfolioStateClass(Enum):
    PROPOSED = auto()
    UNDER_REVIEW = auto()
    PRIORITIZED = auto()
    COMMITTED = auto()
    ON_HOLD = auto()
    FROZEN = auto()
    KILLED = auto()
    DEFERRED = auto()
    COMPLETED = auto()

class PortfolioTrustVerdict(Enum):
    TRUSTED = auto()
    CAUTION = auto()
    DEGRADED = auto()
    BLOCKED = auto()
    REVIEW_REQUIRED = auto()

class PortfolioEquivalenceVerdict(Enum):
    EQUIVALENT = auto()
    PARTIALLY_DIVERGENT = auto()
    DIVERGENT = auto()

class DependencyConstraintClass(Enum):
    HARD_PREREQUISITE = auto()
    SOFT_PREREQUISITE = auto()
    PLATFORM_ENABLER = auto()
    MIGRATION_REQUIRED = auto()

class RoadmapHorizon(Enum):
    NOW = auto()
    NEXT = auto()
    LATER = auto()
    TENTATIVE = auto()

class ReadinessClass(Enum):
    READY = auto()
    BLOCKED = auto()
    CONDITIONALLY_READY = auto()
