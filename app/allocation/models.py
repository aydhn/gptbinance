from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime, timezone
from app.allocation.enums import *


class SleeveDefinition(BaseModel):
    sleeve_id: str
    sleeve_class: SleeveClass
    allowed_instruments: List[str]
    max_capital_share: float
    conflict_priority: int
    owner_domain: str


class SleeveBudget(BaseModel):
    sleeve_id: str
    budget_class: BudgetClass
    allocated_notional: float
    consumed_notional: float
    headroom: float
    is_frozen: bool


class CapitalRoute(BaseModel):
    route_id: str
    source_sleeve_id: str
    eligible_profiles: List[str]
    max_route_size: float


class AllocationCandidate(BaseModel):
    candidate_id: str
    symbol: str
    signal_source_ref: str
    signal_family: SignalFamily
    sleeve_ref: str
    confidence: float
    requested_notional: float
    allocation_class: AllocationClass
    regime_refs: List[str] = Field(default_factory=list)


class AllocationIntent(BaseModel):
    intent_id: str
    candidate_id: str
    symbol: str
    sleeve_ref: str
    verdict: AllocationVerdict
    base_size: float
    clipped_size: float
    defer_reason: Optional[str] = None
    reject_reason: Optional[str] = None
    clip_reasons: List[str] = Field(default_factory=list)
    budget_ref: str
    route_ref: str


class AllocationManifest(BaseModel):
    manifest_id: str
    timestamp: datetime
    intents: List[AllocationIntent]
    portfolio_gross_exposure: float
    portfolio_net_exposure: float
    constraints_refs: List[str]
    trust_verdict: TrustVerdict
    lineage_hash: str


class AllocationDiffRecord(BaseModel):
    diff_id: str
    baseline_manifest_id: str
    candidate_manifest_id: str
    semantic_deltas: List[str]
    divergence_score: float


class AllocationTrustVerdictReport(BaseModel):
    verdict: TrustVerdict
    signal_trust: float
    model_trust: float
    feature_trust: float
    budget_integrity_score: float
    caveats: List[str]
    blockers: List[str]


class PortfolioExposureSnapshot(BaseModel):
    snapshot_id: str
    timestamp: datetime
    gross_notional: float
    net_notional: float
    sleeve_exposures: Dict[str, float]
    symbol_exposures: Dict[str, float]
