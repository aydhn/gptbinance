class ChangePlaneError(Exception):
    pass

class InvalidChangeObjectError(ChangePlaneError):
    pass

class InvalidRequestDefinitionError(ChangePlaneError):
    pass

class InvalidImpactAssessmentError(ChangePlaneError):
    pass

class InvalidApprovalChainError(ChangePlaneError):
    pass

class InvalidChangeWindowError(ChangePlaneError):
    pass

class InvalidRollbackPlanError(ChangePlaneError):
    pass

class InvalidVerificationRecordError(ChangePlaneError):
    pass

class FreezeViolationError(ChangePlaneError):
    pass

class ChangeStorageError(ChangePlaneError):
    pass
