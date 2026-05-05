from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime, timezone
from app.universe.enums import (
    InstrumentType,
    InstrumentStatus,
    LiquiditySeverity,
    SpreadSeverity,
    EligibilityVerdict,
    LifecycleEventType,
    MetadataFreshness,
    TradabilityClass,
)
from app.workspaces.enums import ProfileType


class TickSizeRule(BaseModel):
    tick_size: float
    min_price: float
    max_price: float


class StepSizeRule(BaseModel):
    step_size: float
    min_qty: float
    max_qty: float


class MinNotionalRule(BaseModel):
    min_notional: float
    apply_to_market: bool
    avg_price_mins: int


class ExchangeFilterSet(BaseModel):
    tick_size: Optional[TickSizeRule] = None
    step_size: Optional[StepSizeRule] = None
    min_notional: Optional[MinNotionalRule] = None
    raw_filters: List[Dict[str, Any]] = Field(default_factory=list)


class SymbolAlias(BaseModel):
    symbol: str
    canonical: str


class InstrumentMetadata(BaseModel):
    base_asset: str
    quote_asset: str
    launch_time: Optional[datetime] = None
    delivery_time: Optional[datetime] = None
    contract_size: Optional[float] = None
    margin_asset: Optional[str] = None


class InstrumentRef(BaseModel):
    symbol: str
    product_type: InstrumentType
    canonical_symbol: str


class ProductInstrument(BaseModel):
    ref: InstrumentRef
    status: InstrumentStatus
    filters: ExchangeFilterSet
    metadata: InstrumentMetadata
    freshness: MetadataFreshness
    last_update: datetime
    raw_data: Dict[str, Any] = Field(default_factory=list)


class LiquiditySnapshot(BaseModel):
    ref: InstrumentRef
    rolling_volume: float
    quote_volume: float
    activity_score: float
    severity: LiquiditySeverity
    snapshot_time: datetime


class SpreadSnapshot(BaseModel):
    ref: InstrumentRef
    bid_ask_spread: float
    relative_spread: float
    severity: SpreadSeverity
    snapshot_time: datetime


class TurnoverSnapshot(BaseModel):
    ref: InstrumentRef
    turnover_24h: float
    trade_count_24h: int
    severity: LiquiditySeverity
    snapshot_time: datetime


class TradabilityReport(BaseModel):
    ref: InstrumentRef
    verdict: EligibilityVerdict
    tradability_class: TradabilityClass
    reasons: List[str] = Field(default_factory=list)
    evidence_refs: List[str] = Field(default_factory=list)
    report_time: datetime


class UniverseProfileConfig(BaseModel):
    allowed_products: List[InstrumentType]
    min_liquidity: LiquiditySeverity
    max_spread: SpreadSeverity
    require_fresh_metadata: bool
    allowlist: List[str] = Field(default_factory=list)
    denylist: List[str] = Field(default_factory=list)


class UniverseEligibilityResult(BaseModel):
    ref: InstrumentRef
    profile: ProfileType
    verdict: EligibilityVerdict
    reasons: List[str] = Field(default_factory=list)
    evaluation_time: datetime


class UniverseSnapshot(BaseModel):
    snapshot_id: str
    profile: ProfileType
    created_at: datetime
    eligible_instruments: List[InstrumentRef]
    caution_instruments: List[InstrumentRef]
    blocked_instruments: List[InstrumentRef]
    manifest_ref: str


class LifecycleEvent(BaseModel):
    event_id: str
    ref: InstrumentRef
    event_type: LifecycleEventType
    old_status: Optional[InstrumentStatus] = None
    new_status: Optional[InstrumentStatus] = None
    description: str
    event_time: datetime


class UniverseDiff(BaseModel):
    diff_id: str
    old_snapshot_id: str
    new_snapshot_id: str
    added: List[InstrumentRef]
    removed: List[InstrumentRef]
    status_changed: List[InstrumentRef]
    eligibility_changed: List[InstrumentRef]
    created_at: datetime


class UniverseImpactReport(BaseModel):
    report_id: str
    diff_id: str
    impacted_strategies: List[str]
    impacted_profiles: List[ProfileType]
    severity: str
    recommendations: List[str]
    created_at: datetime
