from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime
from app.warranty_plane.enums import (
    WarrantyClass, ClaimClass, WarrantorClass, CoverageClass,
    ExclusionClass, BreachClass, CureClass, ValidityClass,
    DebtClass, WarrantyEquivalenceVerdictEnum, WarrantyTrustVerdictEnum
)

class WarrantyPlaneConfig(BaseModel):
    strict_mode: bool = True
    enforce_cure_deadlines: bool = True

class WarrantyObjectRef(BaseModel):
    warranty_id: str

class WarrantyObject(BaseModel):
    warranty_id: str
    owner: str
    class_type: WarrantyClass
    scope: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class WarrantyRecord(BaseModel):
    warranty_id: str
    status: str
    proof_notes: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class WarrantedSubjectRecord(BaseModel):
    warranty_id: str
    subject_type: str
    lineage_refs: List[str] = Field(default_factory=list)

class WarrantedClaimRecord(BaseModel):
    warranty_id: str
    claim_class: ClaimClass
    description: str
    lineage_refs: List[str] = Field(default_factory=list)

class WarrantorRecord(BaseModel):
    warranty_id: str
    warrantor_class: WarrantorClass
    description: str
    lineage_refs: List[str] = Field(default_factory=list)

class WarrantyBasisRecord(BaseModel):
    warranty_id: str
    basis_type: str
    lineage_refs: List[str] = Field(default_factory=list)

class CoverageRecord(BaseModel):
    warranty_id: str
    coverage_class: CoverageClass
    lineage_refs: List[str] = Field(default_factory=list)

class ExclusionRecord(BaseModel):
    warranty_id: str
    exclusion_class: ExclusionClass
    lineage_refs: List[str] = Field(default_factory=list)

class DisclaimerRecord(BaseModel):
    warranty_id: str
    disclaimer_type: str
    lineage_refs: List[str] = Field(default_factory=list)

class BeneficiaryCoverageRecord(BaseModel):
    warranty_id: str
    beneficiary_type: str
    lineage_refs: List[str] = Field(default_factory=list)

class WarrantyValidityRecord(BaseModel):
    warranty_id: str
    validity_class: ValidityClass
    lineage_refs: List[str] = Field(default_factory=list)

class WarrantyExpiryRecord(BaseModel):
    warranty_id: str
    expiry_type: str
    lineage_refs: List[str] = Field(default_factory=list)

class TransferabilityRecord(BaseModel):
    warranty_id: str
    transferability_type: str
    lineage_refs: List[str] = Field(default_factory=list)

class AssignabilityRecord(BaseModel):
    warranty_id: str
    assignability_type: str
    lineage_refs: List[str] = Field(default_factory=list)

class WarrantyBreachRecord(BaseModel):
    warranty_id: str
    breach_class: BreachClass
    lineage_refs: List[str] = Field(default_factory=list)

class BreachTriggerRecord(BaseModel):
    warranty_id: str
    trigger_type: str
    lineage_refs: List[str] = Field(default_factory=list)

class PartialBreachRecord(BaseModel):
    warranty_id: str
    partial_type: str
    lineage_refs: List[str] = Field(default_factory=list)

class LatentDefectRecord(BaseModel):
    warranty_id: str
    defect_type: str
    lineage_refs: List[str] = Field(default_factory=list)

class CureRecord(BaseModel):
    warranty_id: str
    cure_class: CureClass
    lineage_refs: List[str] = Field(default_factory=list)

class CureDeadlineRecord(BaseModel):
    warranty_id: str
    deadline_type: str
    lineage_refs: List[str] = Field(default_factory=list)

class CureVerificationRecord(BaseModel):
    warranty_id: str
    verification_type: str
    lineage_refs: List[str] = Field(default_factory=list)

class FailedCureRecord(BaseModel):
    warranty_id: str
    failed_cure_type: str
    lineage_refs: List[str] = Field(default_factory=list)

class ContradictoryWarrantyRecord(BaseModel):
    warranty_id: str
    contradiction_type: str
    lineage_refs: List[str] = Field(default_factory=list)

class IllusoryWarrantyRecord(BaseModel):
    warranty_id: str
    illusory_type: str
    lineage_refs: List[str] = Field(default_factory=list)

class WarrantyDebtRecord(BaseModel):
    warranty_id: str
    debt_class: DebtClass
    amount: float
    lineage_refs: List[str] = Field(default_factory=list)

class WarrantyDriftRecord(BaseModel):
    warranty_id: str
    drift_details: str
    lineage_refs: List[str] = Field(default_factory=list)

class WarrantyComparisonRecord(BaseModel):
    warranty_id: str
    comparison_type: str
    lineage_refs: List[str] = Field(default_factory=list)

class WarrantyObservationReport(BaseModel):
    warranty_id: str
    observation: str

class WarrantyForecastReport(BaseModel):
    warranty_id: str
    forecast: str

class WarrantyEquivalenceReport(BaseModel):
    warranty_id: str
    verdict: WarrantyEquivalenceVerdictEnum
    notes: str

class WarrantyDivergenceReport(BaseModel):
    warranty_id: str
    divergence_details: str

class WarrantyTrustVerdict(BaseModel):
    warranty_id: str
    verdict: WarrantyTrustVerdictEnum
    breakdown: Dict[str, str]

class WarrantyAuditRecord(BaseModel):
    warranty_id: str
    audit_notes: str

class WarrantyArtifactManifest(BaseModel):
    warranty_id: str
    claims_refs: List[str]
    coverage_refs: List[str]
    exclusions_refs: List[str]
    breaches_refs: List[str]
    cures_refs: List[str]
