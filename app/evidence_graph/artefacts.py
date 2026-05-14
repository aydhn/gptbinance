from enum import Enum
class IdentityArtefact:
    pass


class ComplianceArtefact:
    pass


class TelemetrySchemaArtefact:
    pass


class TelemetryDiagnosticArtefact:
    pass


class TelemetryTrustReportArtefact:
    pass

class SecurityAssetArtefact:
    pass

class SecurityBoundaryArtefact:
    pass

class SecuritySecretArtefact:
    pass

class SecurityVulnerabilityArtefact:
    pass

class SecurityPatchArtefact:
    pass

class ArtefactFamily(str, Enum):
    DECISION_DEFINITION = 'decision_definition'
    DECISION_MANIFEST = 'decision_manifest'