"""Exceptions for paper trading runtime."""


class PaperRuntimeError(Exception):
    """Base exception for paper runtime errors."""


class InvalidPaperSessionConfig(PaperRuntimeError):
    """Invalid session configuration."""


class PaperOrderLifecycleError(PaperRuntimeError):
    """Invalid order state transition."""


class PaperFillError(PaperRuntimeError):
    """Error during fill simulation."""


class SessionStateError(PaperRuntimeError):
    """Invalid session state for requested action."""


class RuntimeHaltError(PaperRuntimeError):
    """Runtime halted due to critical error."""


class NotifierError(PaperRuntimeError):
    """Error sending notifications."""


class PaperPersistenceError(PaperRuntimeError):
    """Error persisting paper runtime data."""
