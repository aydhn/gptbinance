from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime

class SuccessionPlaneConfig(BaseModel):
    enabled: bool = True
    strict_mode: bool = True

class SuccessionObjectRef(BaseModel):
    succession_id: str
    class_name: str

class SuccessionObject(BaseModel):
    succession_id: str
    owner: str
    scope: str
    transfer_posture: str
    continuity_posture: str

class SuccessionRecord(BaseModel):
    succession_id: str
    status: str
    notes: Optional[str] = None

class PredecessorRecord(BaseModel):
    predecessor_id: str
    status: str

class SuccessorRecord(BaseModel):
    successor_id: str
    status: str

class SuccessorCandidateRecord(BaseModel):
    candidate_id: str
    status: str

class SuccessionTriggerRecord(BaseModel):
    trigger_id: str
    status: str

class EligibilityRecord(BaseModel):
    eligibility_id: str
    status: str

class CapabilityMatchRecord(BaseModel):
    match_id: str
    status: str

class AuthorityTransferRecord(BaseModel):
    transfer_id: str
    status: str

class AcceptanceRecord(BaseModel):
    acceptance_id: str
    status: str

class OverlapWindowRecord(BaseModel):
    window_id: str
    status: str

class DualControlBoundaryRecord(BaseModel):
    boundary_id: str
    status: str

class AssetContinuityRecord(BaseModel):
    asset_id: str
    status: str

class DutyContinuityRecord(BaseModel):
    duty_id: str
    status: str

class RightsContinuityRecord(BaseModel):
    rights_id: str
    status: str

class LiabilityContinuityRecord(BaseModel):
    liability_id: str
    status: str

class KnowledgeTransferRecord(BaseModel):
    transfer_id: str
    status: str

class KnowledgeAbsorptionRecord(BaseModel):
    absorption_id: str
    status: str

class ResidueCleanupRecord(BaseModel):
    cleanup_id: str
    status: str

class VacancyRiskRecord(BaseModel):
    vacancy_id: str
    status: str

class ShadowSuccessorRecord(BaseModel):
    shadow_id: str
    status: str

class SuccessorDriftRecord(BaseModel):
    drift_id: str
    status: str

class SuccessionDowngradeRecord(BaseModel):
    downgrade_id: str
    status: str

class SuccessionRevocationRecord(BaseModel):
    revocation_id: str
    status: str

class SuccessionComparisonRecord(BaseModel):
    comparison_id: str
    status: str

class SuccessionObservationReport(BaseModel):
    report_id: str
    content: str

class SuccessionForecastReport(BaseModel):
    forecast_id: str
    content: str

class SuccessionDebtRecord(BaseModel):
    debt_id: str
    status: str

class SuccessionEquivalenceReport(BaseModel):
    report_id: str
    status: str

class SuccessionDivergenceReport(BaseModel):
    report_id: str
    status: str

class SuccessionTrustVerdict(BaseModel):
    succession_id: str
    verdict: str
    factors: Dict[str, str]

class SuccessionAuditRecord(BaseModel):
    audit_id: str
    timestamp: datetime

class SuccessionArtifactManifest(BaseModel):
    manifest_id: str
    artifacts: List[str]
