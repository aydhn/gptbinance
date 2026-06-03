from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import datetime

class LegitimacyPlaneConfig(BaseModel):
    is_active: bool = True
    enforce_proportionality: bool = True

class LegitimacyObjectRef(BaseModel):
    legitimacy_id: str
    version: str

class LegitimacyObject(BaseModel):
    legitimacy_id: str
    class_name: str
    owner: str
    scope: str
    justification_posture: str
    contestability_posture: str
    status: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class LegitimacyRecord(BaseModel):
    legitimacy_id: str
    state: str
    fragility: str
    revoked: bool
    proof_notes: List[str]

class StakeholderRecord(BaseModel):
    stakeholder_id: str
    legitimacy_id: str
    category: str
    lineage_refs: List[str]

class StakeholderClassRecord(BaseModel):
    class_id: str
    classification: str

class AffectedPartyMapRecord(BaseModel):
    map_id: str
    legitimacy_id: str
    parties: List[str]

class MandateBasisRecord(BaseModel):
    mandate_id: str
    legitimacy_id: str
    basis: str

class JustificationRecord(BaseModel):
    justification_id: str
    legitimacy_id: str
    strength: str

class PublicReasonRecord(BaseModel):
    reason_id: str
    legitimacy_id: str
    accessibility: str

class DisclosureRecord(BaseModel):
    disclosure_id: str
    legitimacy_id: str
    sufficiency: str

class ExplainabilitySufficiencyRecord(BaseModel):
    explainability_id: str
    legitimacy_id: str
    level: str

class ConsultationRecord(BaseModel):
    consultation_id: str
    legitimacy_id: str
    integrity: str

class RepresentationAdequacyRecord(BaseModel):
    representation_id: str
    legitimacy_id: str
    adequacy: str

class ProportionalityRecord(BaseModel):
    proportionality_id: str
    legitimacy_id: str
    finding: str

class BurdenAsymmetryRecord(BaseModel):
    burden_id: str
    legitimacy_id: str
    asymmetry_level: str

class ContestabilityRecord(BaseModel):
    contestability_id: str
    legitimacy_id: str
    posture: str

class AppealAccessibilityRecord(BaseModel):
    appeal_id: str
    legitimacy_id: str
    accessibility: str

class AcceptanceFragilityRecord(BaseModel):
    acceptance_id: str
    legitimacy_id: str
    fragility_state: str

class LegitimacyDowngradeRecord(BaseModel):
    downgrade_id: str
    legitimacy_id: str
    reason: str

class LegitimacyRevocationRecord(BaseModel):
    revocation_id: str
    legitimacy_id: str
    cause: str

class LegitimacyDriftRecord(BaseModel):
    drift_id: str
    legitimacy_id: str
    drift_type: str

class LegitimacyComparisonRecord(BaseModel):
    comparison_id: str
    source_legitimacy_id: str
    target_legitimacy_id: str
    outcome: str

class LegitimacyObservationReport(BaseModel):
    report_id: str
    observations: List[str]

class LegitimacyForecastReport(BaseModel):
    forecast_id: str
    risks: List[str]

class LegitimacyDebtRecord(BaseModel):
    debt_id: str
    legitimacy_id: str
    severity: str

class LegitimacyEquivalenceReport(BaseModel):
    report_id: str
    verdict: str

class LegitimacyDivergenceReport(BaseModel):
    report_id: str
    divergences: List[str]

class LegitimacyTrustVerdict(BaseModel):
    verdict_id: str
    legitimacy_id: str
    verdict: str
    factors: Dict[str, str]

class LegitimacyAuditRecord(BaseModel):
    audit_id: str
    legitimacy_id: str
    findings: List[str]

class LegitimacyArtifactManifest(BaseModel):
    manifest_id: str
    refs: List[str]
    hashes: Dict[str, str]
