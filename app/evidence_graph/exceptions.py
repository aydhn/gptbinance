class EvidenceGraphError(Exception):
    pass


class InvalidArtefactRecordError(EvidenceGraphError):
    pass


class InvalidRelationEdgeError(EvidenceGraphError):
    pass


class ScopeViolationError(EvidenceGraphError):
    pass


class LineageTraversalError(EvidenceGraphError):
    pass


class DependencyTraversalError(EvidenceGraphError):
    pass


class CaseFileAssemblyError(EvidenceGraphError):
    pass


class RedactionError(EvidenceGraphError):
    pass


class GraphGapError(EvidenceGraphError):
    pass


class EvidenceGraphStorageError(EvidenceGraphError):
    pass
