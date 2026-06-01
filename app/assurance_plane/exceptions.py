class AssurancePlaneError(Exception):
    pass

class InvalidAssuranceObjectError(AssurancePlaneError):
    pass

class InvalidAssuranceClaimError(AssurancePlaneError):
    pass

class InvalidEvidencePackError(AssurancePlaneError):
    pass

class InvalidSufficiencyEvaluationError(AssurancePlaneError):
    pass

class InvalidCertificationError(AssurancePlaneError):
    pass

class InvalidAttestationError(AssurancePlaneError):
    pass

class AssuranceTheaterViolationError(AssurancePlaneError):
    pass

class AssuranceStorageError(AssurancePlaneError):
    pass
