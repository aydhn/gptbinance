class PostmortemError(Exception):
    pass


class InvalidPostmortemSeed(PostmortemError):
    pass


class InvalidChronology(PostmortemError):
    pass


class CausalGraphError(PostmortemError):
    pass


class InadmissibleEvidenceError(PostmortemError):
    pass


class RootCauseAmbiguityError(PostmortemError):
    pass


class CounterfactualMisuseError(PostmortemError):
    pass


class ActionTrackingError(PostmortemError):
    pass


class RecurrenceScoringError(PostmortemError):
    pass


class PostmortemStorageError(PostmortemError):
    pass
