class AccountabilityPlaneError(Exception):
    pass

class InvalidAccountabilityObjectError(AccountabilityPlaneError):
    pass

class AccountabilityTheaterViolation(AccountabilityPlaneError):
    pass

class InvalidAccountableSubjectError(AccountabilityPlaneError):
    pass

class InvalidDutyMappingError(AccountabilityPlaneError):
    pass

class InvalidBreachFindingError(AccountabilityPlaneError):
    pass

class InvalidSanctionError(AccountabilityPlaneError):
    pass

class InvalidAppealError(AccountabilityPlaneError):
    pass

class AccountabilityStorageError(AccountabilityPlaneError):
    pass
