class LearningPlaneError(Exception):
    pass

class InvalidLearningObject(LearningPlaneError):
    pass

class InvalidSignalRecord(LearningPlaneError):
    pass

class InvalidFinding(LearningPlaneError):
    pass

class InvalidCausalHypothesis(LearningPlaneError):
    pass

class InvalidLessonScope(LearningPlaneError):
    pass

class InvalidHardeningAction(LearningPlaneError):
    pass

class InvalidValidation(LearningPlaneError):
    pass

class RecurrenceViolation(LearningPlaneError):
    pass

class LearningStorageError(LearningPlaneError):
    pass
