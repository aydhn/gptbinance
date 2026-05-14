class SupplyChainPlaneError(Exception):
    pass


class InvalidComponentDefinition(SupplyChainPlaneError):
    pass


class InvalidDependencyGraph(SupplyChainPlaneError):
    pass


class InvalidBuildRecipe(SupplyChainPlaneError):
    pass


class InvalidProvenanceRecord(SupplyChainPlaneError):
    pass


class InvalidSbomRecord(SupplyChainPlaneError):
    pass


class InvalidSignatureOrVerificationState(SupplyChainPlaneError):
    pass


class LicenseViolation(SupplyChainPlaneError):
    pass


class DriftViolation(SupplyChainPlaneError):
    pass


class SupplyChainStorageError(SupplyChainPlaneError):
    pass
