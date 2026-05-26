class InsolvencyPlaneError(Exception):
    """Base exception for insolvency plane operations."""
    pass

class InvalidInsolvencyObjectError(InsolvencyPlaneError):
    """Raised when an insolvency object is invalid or misconfigured."""
    pass

class InvalidEstateError(InsolvencyPlaneError):
    """Raised when an estate is malformed, leaked, or incorrectly scoped."""
    pass

class InvalidClaimAdmissionError(InsolvencyPlaneError):
    """Raised when claim admission violates rules or priority."""
    pass

class InvalidPriorityTreatmentError(InsolvencyPlaneError):
    """Raised when priority is inverted or illegally inflated."""
    pass

class InvalidPlanError(InsolvencyPlaneError):
    """Raised when a plan violates fairness or class treatment rules."""
    pass

class InvalidConfirmationError(InsolvencyPlaneError):
    """Raised when confirmation is attempted with defective support or illegal overrides."""
    pass

class EstateLeakageViolationError(InsolvencyPlaneError):
    """Raised when assets or value illegally leak from the estate."""
    pass

class InsolvencyStorageError(InsolvencyPlaneError):
    """Raised when there's an error storing or retrieving insolvency artifacts."""
    pass
