from enum import Enum


class KnowledgeItemType(Enum):
    RUNBOOK = "runbook"
    SOP = "sop"
    PLAYBOOK = "playbook"
    TRAINING_MODULE = "training_module"
    LESSON_LEARNED = "lesson_learned"


class KnowledgeScope(Enum):
    GLOBAL = "global"
    COMPONENT = "component"
    PROFILE = "profile"
    RELEASE = "release"
    ACTION = "action"
    ALERT = "alert"


class ApplicabilityVerdict(Enum):
    APPLICABLE = "applicable"
    CAUTION = "caution"
    BLOCKED = "blocked"


class FreshnessSeverity(Enum):
    HEALTHY = "healthy"
    WARNING = "warning"
    STALE = "stale"
    CRITICAL = "critical"


class QuizVerdict(Enum):
    PASS = "pass"
    CAUTION = "caution"
    FAIL = "fail"


class ReadinessLevel(Enum):
    READY = "ready"
    CAUTION = "caution"
    NOT_READY = "not_ready"
    EXPIRED = "expired"


class LessonStatus(Enum):
    DRAFT = "draft"
    REVIEWED = "reviewed"
    ADOPTED = "adopted"
    ARCHIVED = "archived"


class DocumentStatus(Enum):
    DRAFT = "draft"
    PUBLISHED = "published"
    DEPRECATED = "deprecated"
    ARCHIVED = "archived"


class KnowledgeVerdict(Enum):
    VERIFIED = "verified"
    UNVERIFIED = "unverified"
    CONTRADICTORY = "contradictory"
