class FederationPlaneError(Exception):
    pass


class InvalidFederationObject(FederationPlaneError):
    pass


class InvalidDomainRecord(FederationPlaneError):
    pass


class InvalidTenantRecord(FederationPlaneError):
    pass


class InvalidBoundaryDefinition(FederationPlaneError):
    pass


class InvalidDelegatedAuthority(FederationPlaneError):
    pass


class InvalidPortabilityClaim(FederationPlaneError):
    pass


class InvalidSharedRiskMapping(FederationPlaneError):
    pass


class FederationConflictViolation(FederationPlaneError):
    pass


class FederationStorageError(FederationPlaneError):
    pass
