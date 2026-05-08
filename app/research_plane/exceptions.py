class ResearchPlaneError(Exception):
    pass


class InvalidResearchItemError(ResearchPlaneError):
    pass


class InvalidHypothesisError(ResearchPlaneError):
    pass


class InvalidEvidenceBundleError(ResearchPlaneError):
    pass


class ContradictionHandlingError(ResearchPlaneError):
    pass


class ConfidenceViolationError(ResearchPlaneError):
    pass


class ReadinessViolationError(ResearchPlaneError):
    pass


class InvalidationError(ResearchPlaneError):
    pass


class EquivalenceError(ResearchPlaneError):
    pass


class ResearchStorageError(ResearchPlaneError):
    pass


class OverlapError(ResearchPlaneError):
    pass
