class ReadinessBoardError(Exception):
    pass


class InvalidCandidateRecordError(ReadinessBoardError):
    pass


class InvalidEvidenceSubmissionError(ReadinessBoardError):
    pass


class InadmissibleEvidenceError(ReadinessBoardError):
    pass


class ContradictionResolutionError(ReadinessBoardError):
    pass


class FinalDecisionError(ReadinessBoardError):
    pass


class ScopeMismatchError(ReadinessBoardError):
    pass


class StaleDossierError(ReadinessBoardError):
    pass


class ConditionalTermsError(ReadinessBoardError):
    pass


class BoardStorageError(ReadinessBoardError):
    pass


class FreezeError(ReadinessBoardError):
    pass
