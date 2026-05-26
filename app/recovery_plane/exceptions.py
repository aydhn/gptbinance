class RecoveryPlaneError(Exception): pass
class InvalidRecoveryObjectError(RecoveryPlaneError): pass
class PhantomRecoveryViolation(RecoveryPlaneError): pass
class InvalidWaterfallError(RecoveryPlaneError): pass
