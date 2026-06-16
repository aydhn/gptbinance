
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime
from app.waterfall_plane.enums import (
    WaterfallClass, ClaimClass, RankClass, PoolClass, ReserveClass,
    DistributionClass, ClawbackClass, DebtClass, EquivalenceVerdict, TrustVerdict
)

class WaterfallObjectRef(BaseModel):
    waterfall_id: str
    version: str

class WaterfallPlaneConfig(BaseModel):
    strict_enforcement: bool = True
    allow_advisory_waterfalls: bool = False

class WaterfallObject(BaseModel):
    waterfall_id: str
    waterfall_class: WaterfallClass
    owner: str
    scope: str
    ranking_posture: str
    distribution_posture: str
    metadata: Dict[str, Any] = Field(default_factory=dict)

class WaterfallRecord(BaseModel):
    waterfall_id: str
    status: str
    created_at: datetime
    updated_at: datetime

class WaterfallSubjectRecord(BaseModel):
    subject_id: str
    subject_type: str

class ClaimRecord(BaseModel):
    claim_id: str
    waterfall_id: str
    claim_class: ClaimClass
    amount: float

class ClaimantRecord(BaseModel):
    claimant_id: str
    claimant_type: str

class ClaimLaneRecord(BaseModel):
    lane_id: str
    lane_type: str

class RankRecord(BaseModel):
    rank_id: str
    rank_class: RankClass
    seniority_level: int

class SeniorityRecord(BaseModel):
    seniority_id: str
    description: str

class SubordinationRecord(BaseModel):
    subordination_id: str
    subordinated_to: str

class IntercreditorRecord(BaseModel):
    rule_id: str
    description: str

class PariPassuRecord(BaseModel):
    rule_id: str
    members: List[str]

class ProceedsPoolRecord(BaseModel):
    pool_id: str
    pool_class: PoolClass
    total_amount: float

class PoolSourceRecord(BaseModel):
    source_id: str
    source_type: str

class PoolAvailabilityRecord(BaseModel):
    availability_id: str
    status: str

class NonDistributableComponentRecord(BaseModel):
    component_id: str
    amount: float

class ReserveRecord(BaseModel):
    reserve_id: str
    reserve_class: ReserveClass
    amount: float

class HoldbackRecord(BaseModel):
    holdback_id: str
    amount: float

class DisputedClaimReserveRecord(BaseModel):
    reserve_id: str
    claim_id: str
    amount: float

class ContingentClaimReserveRecord(BaseModel):
    reserve_id: str
    claim_id: str
    amount: float

class DistributionRuleRecord(BaseModel):
    rule_id: str
    description: str

class DistributionActionRecord(BaseModel):
    action_id: str
    distribution_class: DistributionClass
    amount_distributed: float

class PartialSatisfactionRecord(BaseModel):
    satisfaction_id: str
    claim_id: str
    amount_satisfied: float
    deficiency: float

class DeficiencyCarryRecord(BaseModel):
    deficiency_id: str
    claim_id: str
    carried_amount: float

class AntiDuplicationRecord(BaseModel):
    record_id: str
    claim_id: str
    description: str

class OverdistributionRecord(BaseModel):
    record_id: str
    claim_id: str
    excess_amount: float

class ClawbackTriggerRecord(BaseModel):
    trigger_id: str
    condition: str

class ClawbackRecord(BaseModel):
    clawback_id: str
    clawback_class: ClawbackClass
    recovered_amount: float

class ReallocationRecord(BaseModel):
    reallocation_id: str
    from_pool: str
    to_pool: str
    amount: float

class WaterfallDebtRecord(BaseModel):
    debt_id: str
    debt_class: DebtClass
    severity: str

class WaterfallDriftRecord(BaseModel):
    drift_id: str
    description: str

class WaterfallComparisonRecord(BaseModel):
    comparison_id: str
    details: str

class WaterfallObservationReport(BaseModel):
    report_id: str
    metrics: Dict[str, Any]

class WaterfallForecastReport(BaseModel):
    forecast_id: str
    predictions: Dict[str, Any]

class WaterfallEquivalenceReport(BaseModel):
    report_id: str
    verdict: EquivalenceVerdict

class WaterfallDivergenceReport(BaseModel):
    report_id: str
    divergence_sources: List[str]

class WaterfallTrustVerdict(BaseModel):
    waterfall_id: str
    verdict: TrustVerdict
    claim_clarity: bool
    rank_sufficiency: bool
    pool_sufficiency: bool
    reserve_adequacy: bool
    distribution_sufficiency: bool
    clawback_sufficiency: bool
    contradiction_cleanliness: bool

class WaterfallAuditRecord(BaseModel):
    audit_id: str
    waterfall_id: str
    action: str

class WaterfallArtifactManifest(BaseModel):
    manifest_id: str
    items: List[str]
