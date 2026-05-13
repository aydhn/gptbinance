from enum import Enum

class AssetClass(Enum):
    RUNTIME_SERVICE = "runtime_service"
    WORKFLOW = "workflow"
    RELEASE_BUNDLE = "release_bundle"
    DATA_STORE = "data_store"
    MODEL = "model"
    SECRETS_VAULT = "secrets_vault"
    ACCOUNT_WORKSPACE_PROFILE = "account_workspace_profile"
    UNKNOWN = "unknown"

class BoundaryClass(Enum):
    ENVIRONMENT_BOUNDARY = "environment_boundary"
    SERVICE_TO_SERVICE = "service_to_service"
    OPERATOR_TO_SYSTEM = "operator_to_system"
    WORKFLOW_EXECUTION = "workflow_execution"
    EXTERNAL_INTEGRATION = "external_integration"

class SecretClass(Enum):
    PASSWORD = "password"
    API_KEY = "api_key"
    SYMMETRIC_KEY = "symmetric_key"
    ASYMMETRIC_PRIVATE_KEY = "asymmetric_private_key"
    OAUTH_TOKEN = "oauth_token"
    SESSION_COOKIE = "session_cookie"
    OTHER = "other"

class CredentialState(Enum):
    ISSUED = "issued"
    ACTIVE = "active"
    ROTATED = "rotated"
    REVOKED = "revoked"
    EXPIRED = "expired"
    SUSPENDED = "suspended"
    EXPOSED = "exposed"

class VulnerabilityClass(Enum):
    SOFTWARE_DEFECT = "software_defect"
    MISCONFIGURATION = "misconfiguration"
    WEAK_CRYPTOGRAPHY = "weak_cryptography"
    INSECURE_DEPENDENCY = "insecure_dependency"
    EXPOSED_SECRET = "exposed_secret"
    OTHER = "other"

class ExploitabilityClass(Enum):
    PROVEN = "proven"
    HIGH_PROBABILITY = "high_probability"
    THEORETICAL = "theoretical"
    UNREACHABLE = "unreachable"
    MITIGATED = "mitigated"
    UNKNOWN = "unknown"

class ExposureClass(Enum):
    PUBLIC = "public"
    INTERNAL_LATERAL = "internal_lateral"
    CREDENTIAL_EXPOSURE = "credential_exposure"
    BOUNDARY_EXPOSURE = "boundary_exposure"

class HardeningClass(Enum):
    LEAST_PRIVILEGE = "least_privilege"
    BOUNDARY_ISOLATION = "boundary_isolation"
    RUNTIME_CONFIGURATION = "runtime_configuration"
    RELEASE_HARDENING = "release_hardening"
    OBSERVABILITY_REDACTION = "observability_redaction"

class DetectionClass(Enum):
    SECRET_MISUSE = "secret_misuse"
    REVOCATION_BYPASS = "revocation_bypass"
    SUSPICIOUS_BOUNDARY_CROSSING = "suspicious_boundary_crossing"
    ANOMALOUS_PRIVILEGED_ACTION = "anomalous_privileged_action"
    REPEATED_FAILED_AUTHZ = "repeated_failed_authz"

class ExceptionClass(Enum):
    BUSINESS_JUSTIFIED = "business_justified"
    TECHNICAL_LIMITATION = "technical_limitation"
    COMPENSATING_CONTROL_APPLIED = "compensating_control_applied"
    LEGACY_DEBT = "legacy_debt"

class EquivalenceVerdict(Enum):
    EQUIVALENT = "equivalent"
    DIVERGENT = "divergent"
    UNKNOWN = "unknown"

class SecurityTrustVerdictEnum(Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
