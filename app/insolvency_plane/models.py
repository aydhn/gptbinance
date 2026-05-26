from datetime import timezone
from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import datetime
from app.insolvency_plane.enums import (
    InsolvencyClass, DistressTriggerClass, EstateClass, ClaimClass,
    AdmissionClass, PriorityClass, StayClass, PlanClass, ConfirmationClass,
    LiquidationClass, EquivalenceVerdict, InsolvencyTrustVerdict
)

class InsolvencyObjectRef(BaseModel):
    insolvency_id: str
    class_type: InsolvencyClass
    owner: str

class InsolvencyObject(BaseModel):
    id: str
    class_type: InsolvencyClass
    owner: str
    scope: str
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class DistressTriggerRecord(BaseModel):
    trigger_id: str
    trigger_class: DistressTriggerClass
    description: str
    lineage_refs: List[str]

class EstateScopeRecord(BaseModel):
    scope_id: str
    description: str
    status: str
    lineage_refs: List[str]

class EstateAssetRecord(BaseModel):
    asset_id: str
    description: str
    status: str
    lineage_refs: List[str]

class EstateRecord(BaseModel):
    estate_id: str
    insolvency_ref: InsolvencyObjectRef
    estate_class: EstateClass
    scope: EstateScopeRecord
    assets: List[EstateAssetRecord]
    lineage_refs: List[str]

class ClaimRecord(BaseModel):
    claim_id: str
    estate_id: str
    claim_class: ClaimClass
    amount: float
    description: str
    lineage_refs: List[str]

class ClaimAdmissionRecord(BaseModel):
    admission_id: str
    claim_id: str
    admission_class: AdmissionClass
    admitted_amount: float
    lineage_refs: List[str]

class SecuredClaimRecord(BaseModel):
    claim_id: str
    security_description: str
    collateral_value: float
    is_false_comfort: bool = False
    lineage_refs: List[str]

class PriorityClaimRecord(BaseModel):
    claim_id: str
    priority_class: PriorityClass
    rank: int
    lineage_refs: List[str]

class StayScopeRecord(BaseModel):
    scope_id: str
    coverage_description: str
    carve_outs: List[str]
    lineage_refs: List[str]

class StayRecord(BaseModel):
    stay_id: str
    insolvency_ref: InsolvencyObjectRef
    stay_class: StayClass
    scope: StayScopeRecord
    lineage_refs: List[str]

class PlanClassRecord(BaseModel):
    class_id: str
    description: str
    is_impaired: bool
    lineage_refs: List[str]

class PlanSupportRecord(BaseModel):
    support_id: str
    plan_id: str
    class_id: str
    support_posture: str
    lineage_refs: List[str]

class PlanRecord(BaseModel):
    plan_id: str
    insolvency_ref: InsolvencyObjectRef
    plan_class: PlanClass
    classes: List[PlanClassRecord]
    support: List[PlanSupportRecord]
    lineage_refs: List[str]

class ConfirmationRecord(BaseModel):
    confirmation_id: str
    plan_id: str
    confirmation_class: ConfirmationClass
    conditions: List[str]
    lineage_refs: List[str]

class HaircutRecord(BaseModel):
    haircut_id: str
    claim_id: str
    haircut_percentage: float
    description: str
    lineage_refs: List[str]

class CureRecord(BaseModel):
    cure_id: str
    commitment_id: str
    cure_amount: float
    status: str
    lineage_refs: List[str]

class LiquidationRecord(BaseModel):
    liquidation_id: str
    insolvency_ref: InsolvencyObjectRef
    liquidation_class: LiquidationClass
    description: str
    lineage_refs: List[str]

class ResidualDeficitRecord(BaseModel):
    deficit_id: str
    description: str
    deficit_amount: float
    is_hidden: bool = False
    lineage_refs: List[str]

class DistributionLossRecord(BaseModel):
    loss_id: str
    class_id: str
    loss_amount: float
    description: str
    lineage_refs: List[str]

class InsolvencyDebtRecord(BaseModel):
    debt_id: str
    insolvency_ref: InsolvencyObjectRef
    debt_type: str
    description: str
    severity: str

class InsolvencyEquivalenceReport(BaseModel):
    report_id: str
    insolvency_ref: InsolvencyObjectRef
    verdict: EquivalenceVerdict
    divergences: List[str]

class InsolvencyTrustVerdict(BaseModel):
    verdict: str  # trusted, caution, degraded, blocked, review_required
    reasons: List[str]
    estate_clarity: str
    claim_rigor: str
    priority_discipline: str
    stay_integrity: str
    plan_integrity: str
    residual_deficit_visibility: str

class InsolvencyArtifactManifest(BaseModel):
    manifest_id: str
    insolvency_ref: InsolvencyObjectRef
    estate_refs: List[str]
    claim_refs: List[str]
    stay_refs: List[str]
    plan_refs: List[str]
    distribution_refs: List[str]
    deficit_refs: List[str]
    hash: str
