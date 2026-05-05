class WorkspaceError(Exception):
    pass


class InvalidWorkspaceConfigError(WorkspaceError):
    pass


class InvalidProfileDefinitionError(WorkspaceError):
    pass


class BoundaryViolationError(WorkspaceError):
    pass


class WrongWorkspaceContextError(WorkspaceError):
    pass


class CrossProfileContaminationError(WorkspaceError):
    pass


class ScopedPathError(WorkspaceError):
    pass


class WorkspaceSwitchError(WorkspaceError):
    pass


class ManifestIntegrityError(WorkspaceError):
    pass


class IsolationPolicyError(WorkspaceError):
    pass
