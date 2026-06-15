class AttestationPlaneError(Exception):
    pass

class InvalidAttestationObjectError(AttestationPlaneError):
    pass

class InvalidAttestedClaimError(AttestationPlaneError):
    pass

class InvalidAttestationBasisError(AttestationPlaneError):
    pass

class InvalidAttestorAuthorityError(AttestationPlaneError):
    pass

class InvalidValidityWindowError(AttestationPlaneError):
    pass

class InvalidRevocationError(AttestationPlaneError):
    pass

class AttestationTheaterViolation(AttestationPlaneError):
    pass

class AttestationStorageError(AttestationPlaneError):
    pass
