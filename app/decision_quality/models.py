from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import datetime
from .enums import (
    FunnelStage,
    DecisionClass,
    BlockReasonClass,
    FrictionClass,
    OutcomeWindow,
    EvidenceConfidence,
    DecisionQualityVerdict,
)


class DecisionQualityConfig(BaseModel):
    enabled: bool = True
    storage_path: str = "data/decision_quality.db"
    enable_hindsight_safe_checks: bool = True


class OpportunityRef(BaseModel):
    id: str
    symbol: str
    timestamp: datetime


class OpportunityCandidate(BaseModel):
    id: str
    symbol: str
    timestamp: datetime
    timeframe: str
    regime: str
    strategy_family: str
    profile: str
    signal_strength: float
    market_truth_posture: str
    event_risk_context: str
    universe_eligibility_context: str
    metadata: Dict[str, Any] = Field(default_factory=dict)


class BlockReasonRecord(BaseModel):
    id: str
    opportunity_id: str
    reason_class: BlockReasonClass
    description: str
    is_primary: bool
    evidence_refs: List[str] = Field(default_factory=list)


class FunnelStageRecord(BaseModel):
    id: str
    opportunity_id: str
    stage: FunnelStage
    entered_at: datetime
    exited_at: Optional[datetime] = None
    passed: bool
    latency_ms: Optional[float] = None
    reason_refs: List[str] = Field(default_factory=list)


class DecisionFunnelRecord(BaseModel):
    opportunity_id: str
    stages: List[FunnelStageRecord] = Field(default_factory=list)
    final_class: DecisionClass
    created_at: datetime


class DecisionOutcomeWindow(BaseModel):
    window_type: OutcomeWindow
    start_time: datetime
    end_time: datetime


class OpportunityOutcome(BaseModel):
    opportunity_id: str
    window: DecisionOutcomeWindow
    realized_pnl: Optional[float] = None
    max_favorable_excursion: Optional[float] = None
    max_adverse_excursion: Optional[float] = None
    confidence: EvidenceConfidence
    verdict: DecisionQualityVerdict
    evidence_refs: List[str] = Field(default_factory=list)


class ExecutedDecisionRecord(BaseModel):
    opportunity_id: str
    fill_id: str
    execution_friction_score: float


class BlockedDecisionRecord(BaseModel):
    opportunity_id: str
    primary_block_reason: BlockReasonClass
    supporting_reasons: List[BlockReasonClass]


class SkippedDecisionRecord(BaseModel):
    opportunity_id: str
    reason: str


class DecisionFrictionRecord(BaseModel):
    opportunity_id: str
    friction_class: FrictionClass
    severity: float
    description: str


class OpportunityClass(BaseModel):
    opportunity_id: str
    verdict: DecisionQualityVerdict
    confidence: EvidenceConfidence


class DecisionComparison(BaseModel):
    id: str
    base_opportunity_id: str
    target_opportunity_id: str
    verdict: str
    reason: str


class DecisionQualityFinding(BaseModel):
    id: str
    description: str
    friction_class: FrictionClass
    severity: str
    related_opportunities: List[str]


class DecisionQualitySummary(BaseModel):
    timestamp: datetime
    total_opportunities: int
    executed_count: int
    blocked_count: int
    skipped_count: int
    suppressed_count: int
    top_block_reasons: Dict[str, int]
    top_frictions: Dict[str, int]
    findings: List[DecisionQualityFinding]


class OpportunityQualityReport(BaseModel):
    report_id: str
    timestamp: datetime
    opportunities: List[OpportunityOutcome]
    summary: DecisionQualitySummary


class DecisionQualityAuditRecord(BaseModel):
    id: str
    action: str
    timestamp: datetime
    details: Dict[str, Any]


class DecisionQualityArtifactManifest(BaseModel):
    manifest_id: str
    created_at: datetime
    reports_included: List[str]
    storage_refs: List[str]
