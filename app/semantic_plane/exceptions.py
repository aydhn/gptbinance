class SemanticPlaneError(Exception):
    pass

class InvalidSemanticObjectError(SemanticPlaneError):
    pass

class InvalidDefinitionError(SemanticPlaneError):
    pass

class InvalidUnitMappingError(SemanticPlaneError):
    pass

class InvalidThresholdSemanticsError(SemanticPlaneError):
    pass

class InvalidAliasError(SemanticPlaneError):
    pass

class SemanticAmbiguityViolationError(SemanticPlaneError):
    pass

class SemanticDriftViolationError(SemanticPlaneError):
    pass

class SemanticStorageError(SemanticPlaneError):
    pass
