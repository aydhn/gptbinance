from typing import List, Optional, Dict
from pydantic import BaseModel
from app.federation_plane.enums import (
    FederationClass,
    TaxonomyClass,
    DomainClass,
    TenantClass,
    TrustBoundaryClass,
    AuthorityClass,
    PortabilityClass,
    ConflictClass,
    VerdictClass,
    IsolationClass,
    EquivalenceVerdict,
    TrustVerdict,
)


class FederationObjectRef(BaseModel):
    ref_id: str
    ref_type: str


class FederationObject(BaseModel):
    federation_id: str
    domain_id: Optional[str] = None
    tenant_id: Optional[str] = None
    object_class: str
    owner: str
    authority_scope: str
    trust_boundary: str
    portability_posture: str


class FederationRecord(BaseModel):
    federation_id: str
    federation_class: FederationClass
    purpose: str
    participating_domains: List[str]
    participating_tenants: List[str]
    trust_translation_notes: str
    lineage_refs: List[str] = []


class FederationTaxonomyRecord(BaseModel):
    taxonomy_id: str
    taxonomy_class: TaxonomyClass
    description: str


class DomainRecord(BaseModel):
    domain_id: str
    domain_class: DomainClass
    owner: str
    orphan_warnings: List[str] = []
    lineage_refs: List[str] = []


class TenantRecord(BaseModel):
    tenant_id: str
    tenant_class: TenantClass
    criticality_notes: str
    lineage_refs: List[str] = []


class TrustBoundaryRecord(BaseModel):
    boundary_id: str
    boundary_class: TrustBoundaryClass
    crossing_notes: str
    lineage_refs: List[str] = []


class AuthorityBoundaryRecord(BaseModel):
    authority_id: str
    authority_class: AuthorityClass
    conflict_notes: str
    lineage_refs: List[str] = []


class SharedServiceRecord(BaseModel):
    service_id: str
    blast_notes: str
    lineage_refs: List[str] = []


class DependencyFederationRecord(BaseModel):
    dependency_id: str
    dependency_type: str
    hidden_dependency_warnings: List[str] = []
    lineage_refs: List[str] = []


class DelegatedAuthorityRecord(BaseModel):
    delegation_id: str
    bounds: str
    expiry: str
    stale_delegation_warnings: List[str] = []
    proof_notes: str
    lineage_refs: List[str] = []


class PortabilityRecord(BaseModel):
    portability_id: str
    portability_class: PortabilityClass
    caveats: str
    proof_notes: str
    lineage_refs: List[str] = []


class EvidenceTranslationRecord(BaseModel):
    translation_id: str
    translation_type: str
    trust_downgrade_notes: str
    proof_notes: str
    lineage_refs: List[str] = []


class GlobalLocalRuleRecord(BaseModel):
    rule_id: str
    rule_type: str
    cross_domain_conflict_notes: str
    lineage_refs: List[str] = []


class FederatedConflictRecord(BaseModel):
    conflict_id: str
    conflict_class: ConflictClass
    unresolved_notes: str
    proof_notes: str


class BlastRadiusRecord(BaseModel):
    blast_id: str
    blast_type: str
    unknown_warnings: List[str] = []
    lineage_refs: List[str] = []


class TenantIsolationRecord(BaseModel):
    isolation_id: str
    isolation_class: IsolationClass
    weak_isolation_notes: str
    proof_notes: str
    lineage_refs: List[str] = []


class SharedRiskRecord(BaseModel):
    risk_id: str
    risk_type: str
    burden_notes: str
    lineage_refs: List[str] = []


class PartnerFederationRecord(BaseModel):
    partner_id: str
    evidence_sufficiency: str
    stale_trust_warnings: List[str] = []
    proof_notes: str
    lineage_refs: List[str] = []


class FederatedVerdictRecord(BaseModel):
    verdict_id: str
    local_intake: str
    verdict_class: VerdictClass
    tenant_scoped_eligibility: bool
    proof_notes: str
    lineage_refs: List[str] = []


class FederationObservationRecord(BaseModel):
    observation_id: str
    observation_type: str
    sufficiency_notes: str
    lineage_refs: List[str] = []


class FederationForecastReport(BaseModel):
    forecast_id: str
    forecast_type: str
    uncertainty_classes: List[str]


class FederationDebtRecord(BaseModel):
    debt_id: str
    debt_type: str
    severity: str


class FederationEquivalenceReport(BaseModel):
    report_id: str
    verdict: EquivalenceVerdict
    proof_notes: str
    divergence_sources: List[str]


class FederationDivergenceReport(BaseModel):
    report_id: str
    divergence_type: str
    severity: str
    blast_radius: str


class FederationTrustVerdict(BaseModel):
    verdict_id: str
    verdict: TrustVerdict
    breakdown: Dict[str, str]


class FederationAuditRecord(BaseModel):
    audit_id: str
    action: str
    metadata: Dict[str, str]


class FederationArtifactManifest(BaseModel):
    manifest_id: str
    refs: List[FederationObjectRef]
    hashes: Dict[str, str]
