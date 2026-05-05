class ShadowStateError(Exception):
    """Base exception for shadow state operations."""


class VenueSnapshotError(ShadowStateError):
    """Error during venue snapshot retrieval or mapping."""


class LocalSnapshotError(ShadowStateError):
    """Error during local derived snapshot gathering."""


class DriftDetectionError(ShadowStateError):
    """Error during drift detection."""


class ConvergenceError(ShadowStateError):
    """Error during convergence logic."""


class RemediationPlanningError(ShadowStateError):
    """Error during remediation planning."""


class StaleSnapshotError(ShadowStateError):
    """Error due to stale or unusable snapshot."""


class ScopeMismatchError(ShadowStateError):
    """Error due to mixed scopes across profiles/accounts."""


class TruthfulnessEvaluationError(ShadowStateError):
    """Error evaluating truthfulness."""


class ShadowStorageError(ShadowStateError):
    """Error storing or retrieving shadow artifacts."""
