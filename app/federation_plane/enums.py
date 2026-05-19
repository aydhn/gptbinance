from enum import Enum


class FederationClass(str, Enum):
    MULTI_TEAM = "multi_team"
    MULTI_TENANT = "multi_tenant"
    MULTI_SYSTEM = "multi_system"
    SHARED_PLATFORM = "shared_platform"
    PARTNER_VENDOR = "partner_vendor"
    REGIONAL = "regional"
    COMPLIANCE_DOMAIN = "compliance_domain"
    SECURITY_DOMAIN = "security_domain"
    EXECUTION_LANE = "execution_lane"
    SHARED_MODEL = "shared_model"
    SHARED_DATA_PLATFORM = "shared_data_platform"
    CROSS_PLANE_META = "cross_plane_meta"


class TaxonomyClass(str, Enum):
    DOMAIN_FEDERATION = "domain_federation"
    TENANT_FEDERATION = "tenant_federation"
    SERVICE_FEDERATION = "service_federation"
    EVIDENCE_FEDERATION = "evidence_federation"
    POLICY_FEDERATION = "policy_federation"


class DomainClass(str, Enum):
    LOCAL = "local"
    SHARED = "shared"
    SOVEREIGN = "sovereign"
    DEPENDENT = "dependent"


class TenantClass(str, Enum):
    ISOLATED = "isolated"
    SHARED = "shared"
    PREMIUM = "premium"
    REGULATED = "regulated"


class TrustBoundaryClass(str, Enum):
    INTERNAL = "internal"
    PARTNER = "partner"
    VENDOR = "vendor"
    TENANT = "tenant"


class AuthorityClass(str, Enum):
    GLOBAL = "global"
    LOCAL = "local"
    DELEGATED = "delegated"
    TENANT_SCOPED = "tenant_scoped"


class PortabilityClass(str, Enum):
    EVIDENCE = "evidence"
    VERDICT = "verdict"
    CONTROL = "control"
    KNOWLEDGE = "knowledge"


class ConflictClass(str, Enum):
    GLOBAL_LOCAL = "global_local"
    TENANT_LOCAL = "tenant_local"
    AUTHORITY = "authority"
    PORTABILITY = "portability"


class VerdictClass(str, Enum):
    LOCAL_PASS = "local_pass"
    FEDERATED_PASS = "federated_pass"
    FEDERATED_BLOCKER = "federated_blocker"
    TENANT_SCOPED_ELIGIBILITY = "tenant_scoped_eligibility"


class IsolationClass(str, Enum):
    TENANT = "tenant"
    DOMAIN = "domain"
    DATA = "data"
    EXECUTION = "execution"


class EquivalenceVerdict(str, Enum):
    EQUIVALENT = "equivalent"
    PARTIALLY_EQUIVALENT = "partially_equivalent"
    DIVERGED = "diverged"
    UNKNOWN = "unknown"


class TrustVerdict(str, Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
