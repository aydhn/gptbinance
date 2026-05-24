class EnforcementPlaneError(Exception):
    """Base exception for Enforcement Plane."""
    pass

class InvalidEnforcementObjectError(EnforcementPlaneError): pass
class InvalidTriggerBasisError(EnforcementPlaneError): pass
class IndefiniteHoldError(EnforcementPlaneError): pass
class DueProcessBypassError(EnforcementPlaneError): pass
class CoerciveOverreachViolation(EnforcementPlaneError): pass
class InvalidLiftCriteriaError(EnforcementPlaneError): pass
class ShadowEnforcementError(EnforcementPlaneError): pass
class InvalidSanctionError(EnforcementPlaneError): pass
class InvalidReversalError(EnforcementPlaneError): pass
class InvalidAppealHandlingError(EnforcementPlaneError): pass
class EnforcementStorageError(EnforcementPlaneError): pass
