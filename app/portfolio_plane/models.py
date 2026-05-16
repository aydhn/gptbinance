from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime

from app.portfolio_plane.enums import (
    PortfolioObjectClass,
    PortfolioThemeClass,
    InvestmentBucketClass,
    CommitmentClass,
    FundingClass,
    WIPClass,
    PortfolioStateClass,
    PortfolioTrustVerdict,
    PortfolioEquivalenceVerdict,
    DependencyConstraintClass,
    RoadmapHorizon,
    ReadinessClass
)

class PortfolioObjectRef(BaseModel):
    portfolio_id: str
    object_class: PortfolioObjectClass

class PortfolioTheme(BaseModel):
    theme_id: str
    theme_class: PortfolioThemeClass
    name: str
    description: str
    horizon_notes: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class InvestmentBucket(BaseModel):
    bucket_id: str
    bucket_class: InvestmentBucketClass
    name: str
    budget_envelope: float
    capacity_envelope: float
    description: str

class PortfolioObject(BaseModel):
    portfolio_id: str
    object_class: PortfolioObjectClass
    owner: str
    scope: str
    commitment_class: CommitmentClass
    value_thesis: str
    theme_id: str
    bucket_id: str
    state: PortfolioStateClass

class InitiativeRecord(BaseModel):
    initiative_id: str
    portfolio_id: str
    name: str
    thesis_type: str
    lifecycle_phase: str
    proof_notes: str

class WorkstreamRecord(BaseModel):
    workstream_id: str
    initiative_id: str
    name: str
    ownership_scope: str
    is_sequence_critical: bool
    lineage_refs: List[str] = Field(default_factory=list)

class RoadmapItem(BaseModel):
    roadmap_item_id: str
    portfolio_id: str
    horizon: RoadmapHorizon
    is_committed: bool
    integrity_notes: str

class PrioritizationRecord(BaseModel):
    prioritization_id: str
    portfolio_id: str
    value_weight: float
    risk_weight: float
    urgency_cost_of_delay: float
    strategic_fit_score: float
    proof_notes: str

class DependencyConstraint(BaseModel):
    dependency_id: str
    source_portfolio_id: str
    target_portfolio_id: str
    constraint_class: DependencyConstraintClass
    proof_notes: str

class SequencingRecord(BaseModel):
    sequencing_id: str
    portfolio_id: str
    sequence_order: int
    dependencies: List[DependencyConstraint]
    rationale_notes: str

class CommitmentRecord(BaseModel):
    commitment_id: str
    portfolio_id: str
    commitment_class: CommitmentClass
    downgrade_upgrade_history: List[str] = Field(default_factory=list)

class FundingRecord(BaseModel):
    funding_id: str
    portfolio_id: str
    funding_class: FundingClass
    envelope_allocated: float
    lineage_refs: List[str] = Field(default_factory=list)

class StaffingRecord(BaseModel):
    staffing_id: str
    portfolio_id: str
    assigned_team: str
    is_partial: bool
    drift_warnings: List[str] = Field(default_factory=list)

class CapacityReservationRef(BaseModel):
    reservation_id: str
    portfolio_id: str
    capacity_allocated: float
    crowding_warnings: List[str] = Field(default_factory=list)

class WipLimitRecord(BaseModel):
    wip_record_id: str
    bucket_id: str
    wip_class: WIPClass
    current_wip: int
    wip_limit: int

class CrowdOutRecord(BaseModel):
    crowd_out_id: str
    displacing_portfolio_id: str
    displaced_portfolio_id: str
    rationale: str

class PortfolioBalanceReport(BaseModel):
    report_id: str
    timestamp: datetime
    bucket_balances: Dict[str, float]
    domination_cautions: List[str] = Field(default_factory=list)

class FreezeRecord(BaseModel):
    freeze_id: str
    portfolio_id: str
    freeze_type: str
    rationale: str
    expiry: Optional[datetime]

class KillRecord(BaseModel):
    kill_id: str
    portfolio_id: str
    kill_reason: str
    evidence_notes: str

class DeferralRecord(BaseModel):
    deferral_id: str
    portfolio_id: str
    deferral_reason: str
    expiry: datetime

class StageFundingRecord(BaseModel):
    stage_funding_id: str
    portfolio_id: str
    current_stage: FundingClass
    gate_evidence: str

class StrategicFitRecord(BaseModel):
    fit_id: str
    portfolio_id: str
    fit_type: str
    proof_notes: str

class PortfolioVarianceRecord(BaseModel):
    variance_id: str
    portfolio_id: str
    variance_type: str
    proof_notes: str

class PortfolioForecastReport(BaseModel):
    forecast_id: str
    timestamp: datetime
    completion_forecasts: Dict[str, str]
    funding_runway_forecasts: Dict[str, str]

class PortfolioDebtRecord(BaseModel):
    debt_id: str
    portfolio_id: str
    debt_type: str
    severity: str

class PortfolioEquivalenceReport(BaseModel):
    report_id: str
    portfolio_id: str
    verdict: PortfolioEquivalenceVerdict
    blockers: List[str] = Field(default_factory=list)

class PortfolioDivergenceReport(BaseModel):
    report_id: str
    portfolio_id: str
    divergence_type: str
    severity: str

class PortfolioTrustVerdictReport(BaseModel):
    verdict_id: str
    portfolio_id: str
    verdict: PortfolioTrustVerdict
    factors: Dict[str, str]

class PortfolioArtifactManifest(BaseModel):
    manifest_id: str
    timestamp: datetime
    objects: List[PortfolioObjectRef]
    hash_val: str
