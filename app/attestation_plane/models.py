from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any
from datetime import datetime

@dataclass
class AttestationPlaneConfig:
    enabled: bool = True

@dataclass
class AttestationObject:
    attestation_id: str
    attestation_class: str
    owner: str
    scope: str
    claim_posture: str
    validity_posture: str
    metadata: Dict[str, Any] = field(default_factory=dict)

@dataclass
class AttestationObjectRef:
    attestation_id: str
    timestamp: datetime = field(default_factory=datetime.utcnow)

@dataclass
class AttestationRecord:
    attestation_id: str
    status: str
    timestamp: datetime = field(default_factory=datetime.utcnow)
    notes: List[str] = field(default_factory=list)

@dataclass
class AttestationSubjectRecord:
    subject_id: str
    subject_type: str
    attestation_id: str

@dataclass
class AttestedClaimRecord:
    claim_id: str
    claim_class: str
    attestation_id: str
    is_scoped_clean_state: bool

@dataclass
class AttestationBasisRecord:
    basis_id: str
    basis_class: str
    attestation_id: str

@dataclass
class AttestorRecord:
    attestor_id: str
    attestor_class: str

@dataclass
class AttestorAuthorityRecord:
    authority_id: str
    attestor_id: str
    is_valid: bool

@dataclass
class AttestorIndependenceRecord:
    independence_id: str
    attestor_id: str
    status: str

@dataclass
class CertificationScopeRecord:
    scope_id: str
    attestation_id: str
    boundary: str

@dataclass
class ExcludedScopeRecord:
    exclusion_id: str
    scope_id: str
    details: str

@dataclass
class ValidityWindowRecord:
    validity_id: str
    attestation_id: str
    status: str

@dataclass
class FreshnessDecayRecord:
    freshness_id: str
    attestation_id: str
    decay_status: str

@dataclass
class ProvisionalAttestationRecord:
    provisional_id: str
    attestation_id: str
    status: str

@dataclass
class ConditionalAttestationRecord:
    conditional_id: str
    attestation_id: str
    status: str

@dataclass
class NegativeAttestationRecord:
    negative_id: str
    attestation_id: str
    status: str

@dataclass
class LimitedAttestationRecord:
    limited_id: str
    attestation_id: str
    status: str

@dataclass
class ContradictionRecord:
    contradiction_id: str
    attestation_id: str
    contradiction_class: str

@dataclass
class RevocationRecord:
    revocation_id: str
    attestation_id: str
    revocation_class: str

@dataclass
class AttestationRenewalRecord:
    renewal_id: str
    attestation_id: str
    status: str

@dataclass
class CertificateDriftRecord:
    drift_id: str
    attestation_id: str
    severity: str

@dataclass
class StaleCitationRecord:
    citation_id: str
    attestation_id: str
    risk_level: str

@dataclass
class AttestationDebtRecord:
    debt_id: str
    debt_class: str
    attestation_id: str
    severity: str

@dataclass
class AttestationComparisonRecord:
    comparison_id: str
    attestation_id: str
    target_id: str

@dataclass
class AttestationObservationReport:
    report_id: str
    attestation_id: str
    details: str

@dataclass
class AttestationForecastReport:
    report_id: str
    attestation_id: str
    forecast: str

@dataclass
class AttestationEquivalenceReport:
    report_id: str
    attestation_id: str
    equivalence_status: str

@dataclass
class AttestationDivergenceReport:
    report_id: str
    attestation_id: str
    divergence_details: str

@dataclass
class AttestationTrustVerdict:
    verdict_id: str
    attestation_id: str
    status: str

@dataclass
class AttestationAuditRecord:
    audit_id: str
    attestation_id: str
    action: str

@dataclass
class AttestationArtifactManifest:
    manifest_id: str
    attestation_id: str
    items: List[str]
