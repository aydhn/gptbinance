from enum import Enum, auto


class ComponentClass(Enum):
    SOURCE_COMPONENT = auto()
    THIRD_PARTY_DEPENDENCY = auto()
    GENERATED_CODE_COMPONENT = auto()
    MODEL_ARTIFACT_COMPONENT = auto()
    DATASET_SNAPSHOT_COMPONENT = auto()
    BUILD_TOOL_COMPONENT = auto()
    WORKFLOW_IMAGE_COMPONENT = auto()
    RUNTIME_CONTAINER_COMPONENT = auto()
    RELEASE_BUNDLE_COMPONENT = auto()
    CONFIG_BUNDLE_COMPONENT = auto()
    OBSERVABILITY_AGENT_COMPONENT = auto()
    CONTROL_AUTOMATION_COMPONENT = auto()


class OriginClass(Enum):
    INTERNAL_SOURCE = auto()
    VENDORED_SOURCE = auto()
    THIRD_PARTY_PACKAGE = auto()
    GENERATED_SOURCE = auto()
    DOWNLOADED_BINARY = auto()
    EXTERNAL_DATA_MODEL = auto()


class DependencyClass(Enum):
    DIRECT = auto()
    TRANSITIVE = auto()
    OPTIONAL = auto()
    BUILD_TIME = auto()
    RUNTIME = auto()


class BuildClass(Enum):
    DETERMINISTIC = auto()
    NON_DETERMINISTIC = auto()


class ArtifactClass(Enum):
    PACKAGE = auto()
    CONTAINER_IMAGE = auto()
    GENERATED_FILE = auto()
    COMPILED_BINARY = auto()


class SbomClass(Enum):
    SOURCE_SBOM = auto()
    BUILD_SBOM = auto()
    RELEASE_SBOM = auto()
    RUNTIME_SBOM = auto()


class VerificationClass(Enum):
    DIGEST_MATCH = auto()
    SIGNATURE_VERIFIED = auto()
    PROVENANCE_VERIFIED = auto()
    RUNTIME_MATCH = auto()
    REBUILD_MATCH = auto()


class LicenseClass(Enum):
    ACCEPTABLE = auto()
    PROHIBITED = auto()
    REVIEW_REQUIRED = auto()
    UNKNOWN = auto()


class DriftClass(Enum):
    DEPENDENCY_DRIFT = auto()
    BUILD_RECIPE_DRIFT = auto()
    RUNTIME_ARTIFACT_DRIFT = auto()
    SBOM_DRIFT = auto()
    LICENSE_DRIFT = auto()
    BASE_IMAGE_DRIFT = auto()


class ExceptionClass(Enum):
    SCOPED_EXCEPTION = auto()
    TTL_BOUND = auto()
    UNVERIFIABLE_COMPONENT = auto()
    LICENSE_EXCEPTION = auto()
    STALE_DEPENDENCY = auto()


class EquivalenceVerdict(Enum):
    FULLY_EQUIVALENT = auto()
    PARTIALLY_EQUIVALENT = auto()
    DIVERGED = auto()


class TrustVerdict(Enum):
    TRUSTED = auto()
    CAUTION = auto()
    DEGRADED = auto()
    BLOCKED = auto()
    REVIEW_REQUIRED = auto()


class ReadinessClass(Enum):
    READY = auto()
    CAUTION = auto()
    NOT_READY = auto()
