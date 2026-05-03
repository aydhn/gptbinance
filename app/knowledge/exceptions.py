class KnowledgeError(Exception):
    """Base exception for knowledge domain."""

    pass


class InvalidKnowledgeItem(KnowledgeError):
    """Raised when a knowledge item is invalid or malformed."""

    pass


class InvalidApplicabilityRule(KnowledgeError):
    """Raised when an applicability rule cannot be processed."""

    pass


class StaleKnowledgeError(KnowledgeError):
    """Raised when attempting to use explicitly stale knowledge for a critical path."""

    pass


class UnsupportedRunbookScope(KnowledgeError):
    """Raised when a runbook does not apply to the requested scope."""

    pass


class InvalidQuizDefinition(KnowledgeError):
    """Raised when a quiz definition is invalid."""

    pass


class ReadinessEvaluationError(KnowledgeError):
    """Raised when operator readiness cannot be evaluated."""

    pass


class LessonLinkageError(KnowledgeError):
    """Raised when linking a lesson to other knowledge items fails."""

    pass


class CatalogIntegrityError(KnowledgeError):
    """Raised when catalog integrity constraints are violated."""

    pass
