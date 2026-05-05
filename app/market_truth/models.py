from pydantic import BaseModel
from typing import List, Dict
from datetime import datetime
from app.market_truth.enums import (
    SourceType,
    StreamType,
    TruthDomain,
    FreshnessClass,
    GapType,
    DedupVerdict,
    OrderingSeverity,
    ConvergenceVerdict,
    TruthfulnessClass,
    MarketTruthVerdict,
)


class SourceAdapterConfig(BaseModel):
    source_type: SourceType
    description: str


class MarketTruthConfig(BaseModel):
    enabled: bool = True


class MarketClockSnapshot(BaseModel):
    exchange_time: datetime
    local_wall_time: datetime
    local_monotonic_time: float
    processing_lag_ms: float
    drift_ms: float


class ExchangeTimeSnapshot(BaseModel):
    server_time: datetime
    latency_ms: float


class SymbolFeedHealth(BaseModel):
    symbol: str
    stream_type: StreamType
    is_healthy: bool
    last_update_local: datetime
    last_update_exchange: datetime


class FeedHealthSnapshot(BaseModel):
    timestamp: datetime
    symbols: Dict[str, List[SymbolFeedHealth]]


class StreamEventRef(BaseModel):
    event_id: str
    timestamp: datetime


class SequenceWindow(BaseModel):
    start_id: int
    end_id: int
    count: int


class GapFinding(BaseModel):
    gap_type: GapType
    start_id: int
    end_id: int
    missing_count: int
    severity: str


class GapCluster(BaseModel):
    findings: List[GapFinding]


class SequenceIntegrityReport(BaseModel):
    stream_type: StreamType
    symbol: str
    is_monotonic: bool
    gaps: GapCluster


class DedupRecord(BaseModel):
    event_id: str
    verdict: DedupVerdict


class OrderingViolation(BaseModel):
    event_id: str
    expected_order: int
    actual_order: int
    severity: OrderingSeverity


class FreshnessBudget(BaseModel):
    profile_name: str
    max_lag_ms: float
    max_silence_ms: float


class FreshnessReport(BaseModel):
    symbol: str
    domain: TruthDomain
    freshness_class: FreshnessClass
    lag_ms: float
    silence_ms: float


class StreamConvergenceReport(BaseModel):
    symbol: str
    stream_type: StreamType
    verdict: ConvergenceVerdict
    divergence_magnitude: float


class KlineTruthReport(BaseModel):
    symbol: str
    interval: str
    is_aligned: bool
    missing_bars: int


class TradeTruthReport(BaseModel):
    symbol: str
    trade_continuity: bool
    stale_silence: bool


class QuoteTruthReport(BaseModel):
    symbol: str
    freshness: FreshnessClass
    crossed_suspicion: bool


class MarkPriceTruthReport(BaseModel):
    symbol: str
    freshness: FreshnessClass
    stale_caution: bool


class TruthfulnessVerdictDetail(BaseModel):
    domain: TruthDomain
    truth_class: TruthfulnessClass
    reasons: List[str]


class MarketTruthEvidenceBundle(BaseModel):
    timestamp: datetime
    symbol: str
    verdicts: List[TruthfulnessVerdictDetail]
    overall_verdict: MarketTruthVerdict


class MarketTruthAuditRecord(BaseModel):
    run_id: str
    timestamp: datetime
    evidence_bundle: MarketTruthEvidenceBundle


class MarketTruthArtifactManifest(BaseModel):
    run_id: str
    artifact_paths: List[str]


class MarketTruthContext(BaseModel):
    evidence: MarketTruthEvidenceBundle
    clock: MarketClockSnapshot
