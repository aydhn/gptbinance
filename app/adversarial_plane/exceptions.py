class AdversarialPlaneError(Exception):
    pass

class InvalidAdversarialObjectError(AdversarialPlaneError):
    pass

class InvalidActorRecordError(AdversarialPlaneError):
    pass

class InvalidExploitDefinitionError(AdversarialPlaneError):
    pass

class InvalidSuspicionError(AdversarialPlaneError):
    pass

class InvalidConfirmationError(AdversarialPlaneError):
    pass

class EvasionIntegrityViolationError(AdversarialPlaneError):
    pass

class GamingEvidenceViolationError(AdversarialPlaneError):
    pass

class AdversarialStorageError(AdversarialPlaneError):
    pass
