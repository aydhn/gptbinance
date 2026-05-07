class ConfigPlaneError(Exception):
    pass

class InvalidConfigSchema(ConfigPlaneError):
    pass

class InvalidParameterDefinition(ConfigPlaneError):
    pass

class InvalidOverride(ConfigPlaneError):
    pass

class ScopeMismatchError(ConfigPlaneError):
    pass

class MutabilityViolation(ConfigPlaneError):
    pass

class ConfigResolutionError(ConfigPlaneError):
    pass

class EquivalenceError(ConfigPlaneError):
    pass

class DriftDetectionError(ConfigPlaneError):
    pass

class ConfigStorageError(ConfigPlaneError):
    pass
