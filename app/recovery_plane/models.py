from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import datetime
from app.recovery_plane.enums import *

class RecoveryPlaneConfig(BaseModel):
    strict_waterfall: bool = True
    no_hidden_shortfall: bool = True
    require_receipt_for_finalization: bool = True

class RecoveryObjectRef(BaseModel):
    recovery_id: str
    class_type: str

class RecoveryObject(BaseModel):
    recovery_id: str
    owner: str
    scope: str
    recovery_class: RecoveryClass
    source_posture: str
    distribution_posture: str

class RecoveryRecord(BaseModel):
    recovery_id: str
    state: str
    proof_notes: str
    lineage_refs: List[str]

class RecoveryClaimRecord(BaseModel):
    claim_id: str
    recovery_id: str
    claim_class: ClaimClass
    basis_notes: str

class RecoverySourceRecord(BaseModel):
    source_id: str
    recovery_id: str
    source_class: SourceClass
    lineage_refs: List[str]

class SecuredRecoveryRecord(BaseModel):
    recovery_id: str
    secured_class: SecuredClass
    cautions: List[str]

class UnsecuredRecoveryRecord(BaseModel):
    recovery_id: str
    posture: str

class WaterfallRecord(BaseModel):
    waterfall_id: str
    recovery_id: str
    waterfall_class: WaterfallClass
    opacity_cautions: List[str]

class PriorityTierRecord(BaseModel):
    tier_id: str
    waterfall_id: str
    priority_class: PriorityClass

class AllocationRecord(BaseModel):
    allocation_id: str
    waterfall_id: str
    posture: str

class DistributionRecord(BaseModel):
    distribution_id: str
    allocation_id: str
    distribution_class: DistributionClass
    caveats: List[str]

class ReceiptRecord(BaseModel):
    receipt_id: str
    distribution_id: str
    posture: str
    notes: str

class GrossRecoveryRecord(BaseModel):
    recovery_id: str
    amount: float
    overstated_cautions: List[str]

class NetRecoveryRecord(BaseModel):
    recovery_id: str
    net_amount: float
    distributable_amount: float
    realized_amount: float

class CostOfRecoveryRecord(BaseModel):
    recovery_id: str
    direct_cost: float
    legal_cost: float
    warnings: List[str]

class OffsetRecord(BaseModel):
    recovery_id: str
    posture: str
    cash_equivalence_caution: str

class ProvisionalRecoveryRecord(BaseModel):
    recovery_id: str
    provisional_posture: str

class ClawbackRiskRecord(BaseModel):
    recovery_id: str
    clawback_class: ClawbackClass
    notes: str

class HoldbackDistributionRecord(BaseModel):
    recovery_id: str
    posture: str
    visibility_cautions: List[str]

class ShortfallRecord(BaseModel):
    recovery_id: str
    shortfall_class: ShortfallClass

class DeficiencyRecord(BaseModel):
    recovery_id: str
    deficiency_class: DeficiencyClass

class FinalizedRecoveryRecord(BaseModel):
    recovery_id: str
    finalization_posture: str

class ResidualExposureRecord(BaseModel):
    recovery_id: str
    exposure_posture: str
    notes: str

class RecoveryComparisonRecord(BaseModel):
    recovery_id: str
    gross_vs_net: str
    allocation_vs_distribution: str

class RecoveryForecastReport(BaseModel):
    recovery_id: str
    collection_delay_forecast: str
    shortfall_growth_forecast: str

class RecoveryDebtRecord(BaseModel):
    recovery_id: str
    phantom_recovery_debt: float
    hidden_shortfall_debt: float

class RecoveryEquivalenceReport(BaseModel):
    recovery_id: str
    verdict: EquivalenceVerdict
    blockers: List[str]

class RecoveryTrustVerdict(BaseModel):
    recovery_id: str
    verdict: TrustVerdict
    blockers: List[str]
    caveats: List[str]
