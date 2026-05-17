from enum import Enum, auto

class EnvironmentClass(Enum):
    LOCAL_DEV = auto()
    CI_TEST = auto()
    INTEGRATION = auto()
    REPLAY = auto()
    PAPER = auto()
    PROBATION = auto()
    SHADOW = auto()
    STAGING = auto()
    LIVE = auto()
    DR = auto()
    RESEARCH_SANDBOX = auto()
    DESTRUCTIVE_TEST = auto()

class TopologyClass(Enum):
    SINGLE_TENANT = auto()
    SHARED = auto()
    SHADOW = auto()
    DR = auto()
    EPHEMERAL = auto()

class BoundaryClass(Enum):
    CONTROL_PLANE = auto()
    DATA_PLANE = auto()
    TENANT = auto()
    EXECUTION = auto()
    OPERATOR = auto()

class ParityClass(Enum):
    EXACT_PARITY = auto()
    HIGH_PARITY = auto()
    PARTIAL_PARITY = auto()
    LOW_PARITY = auto()
    DIVERGENT = auto()

class DivergenceClass(Enum):
    INTENDED_SAFE = auto()
    INTENDED_REQUIRED = auto()
    INTENDED_BUDGET = auto()
    INTENDED_PRIVACY = auto()
    ACCIDENTAL_DRIFT = auto()
    UNKNOWN = auto()

class PromotionClass(Enum):
    REPLAY_TO_PAPER = auto()
    PAPER_TO_PROBATION = auto()
    PROBATION_TO_LIVE = auto()
    STAGING_TO_LIVE = auto()
    DR_ACTIVATION = auto()

class IsolationClass(Enum):
    COMPUTE = auto()
    NETWORK = auto()
    STATE = auto()
    QUEUE = auto()
    EXECUTION = auto()

class TenancyClass(Enum):
    SINGLE_TENANT = auto()
    SHARED_TENANT = auto()
    SYNTHETIC_TENANT = auto()
    TRAINING_TENANT = auto()

class ContaminationClass(Enum):
    PAPER_LIVE = auto()
    REPLAY_LIVE = auto()
    CROSS_TENANT = auto()
    SECRET = auto()
    SHARED_STATE = auto()

class ReadinessClass(Enum):
    LIVE_LIKE = auto()
    PROMOTION_READY = auto()
    DR_READY = auto()
    DESTRUCTIVE_TEST_READY = auto()
    ISOLATION_READY = auto()

class EquivalenceVerdict(Enum):
    EQUIVALENT = auto()
    PARTIALLY_EQUIVALENT = auto()
    NON_EQUIVALENT = auto()

class TrustVerdict(Enum):
    TRUSTED = auto()
    CAUTION = auto()
    DEGRADED = auto()
    BLOCKED = auto()
    REVIEW_REQUIRED = auto()
