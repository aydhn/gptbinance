from dataclasses import dataclass, field
from typing import Dict, Any
from datetime import datetime

@dataclass
class JurisdictionPlaneConfig:
    enabled: bool = True

@dataclass
class JurisdictionObjectRef:
    id: str

@dataclass
class JurisdictionScopeRecord:
    scope_id: str
    scope_type: str

@dataclass
class SubjectRecord:
    subject_id: str

@dataclass
class ActorSubjectRecord(SubjectRecord):
    actor_type: str

@dataclass
class ActionScopeRecord:
    action_id: str

@dataclass
class ArtefactScopeRecord:
    artefact_id: str

@dataclass
class DomainJurisdictionRecord:
    domain_id: str

@dataclass
class TenantJurisdictionRecord:
    tenant_id: str

@dataclass
class EnvironmentJurisdictionRecord:
    environment_id: str

@dataclass
class DataJurisdictionRecord:
    data_id: str

@dataclass
class RegimeRecord:
    regime_id: str

@dataclass
class GoverningSourceRecord:
    source_id: str

@dataclass
class ApplicabilityRecord:
    applicability_id: str

@dataclass
class ExclusionRecord:
    exclusion_id: str

@dataclass
class ExemptionRecord:
    exemption_id: str

@dataclass
class WaiverRecord:
    waiver_id: str

@dataclass
class JurisdictionConflictRecord:
    conflict_id: str

@dataclass
class PrecedenceRecord:
    precedence_id: str

@dataclass
class ReachRecord:
    reach_id: str

@dataclass
class PortabilityRecord:
    portability_id: str

@dataclass
class PermissionUnderJurisdictionRecord:
    permission_id: str

@dataclass
class ProhibitionUnderJurisdictionRecord:
    prohibition_id: str

@dataclass
class ObligationUnderJurisdictionRecord:
    obligation_id: str

@dataclass
class EnforcementRecord:
    enforcement_id: str

@dataclass
class JurisdictionComparisonRecord:
    comparison_id: str

@dataclass
class JurisdictionObservationReport:
    report_id: str

@dataclass
class JurisdictionForecastReport:
    forecast_id: str

@dataclass
class JurisdictionDebtRecord:
    debt_id: str

@dataclass
class JurisdictionEquivalenceReport:
    report_id: str

@dataclass
class JurisdictionDivergenceReport:
    report_id: str

@dataclass
class JurisdictionTrustVerdict:
    verdict: str
    factors: Dict[str, Any] = field(default_factory=dict)

@dataclass
class JurisdictionAuditRecord:
    audit_id: str

@dataclass
class JurisdictionArtifactManifest:
    manifest_id: str

@dataclass
class JurisdictionObject:
    jurisdiction_id: str
    jurisdiction_class: str
    owner: str
    scope: JurisdictionScopeRecord
    governing_source_posture: str
    applicability_posture: str
    created_at: datetime = field(default_factory=datetime.utcnow)
