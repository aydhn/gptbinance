from pydantic import BaseModel, Field
from typing import Dict, List, Optional, Any
from datetime import datetime, timezone
from decimal import Decimal

from app.position_plane.enums import (
    ProductClass,
    Side,
    LifecycleState,
    PnlComponent,
    DivergenceSeverity,
    EquivalenceVerdict,
    TrustVerdict,
    CostBasisClass,
)


class PositionPlaneConfig(BaseModel):
    allow_cross_book_aggregation: bool = False
    strict_lot_matching: bool = True
    mark_staleness_threshold_seconds: int = 60
    cost_basis_method: CostBasisClass = CostBasisClass.FIFO_LOT


class PositionLotRef(BaseModel):
    lot_id: str
    fill_id: str
    quantity: Decimal
    price: Decimal


class PositionLot(BaseModel):
    id: str
    symbol: str
    product_class: ProductClass
    side: Side
    quantity: Decimal
    remaining_quantity: Decimal
    entry_price: Decimal
    created_at: datetime
    source_fill_id: str
    sleeve_id: str
    is_closed: bool = False
    metadata: Dict[str, Any] = Field(default_factory=dict)


class PositionStateRef(BaseModel):
    state_id: str
    hash: str


class PositionState(BaseModel):
    id: str
    symbol: str
    product_class: ProductClass
    sleeve_id: str
    side: Side
    quantity: Decimal
    average_entry_price: Decimal
    lifecycle_state: LifecycleState
    open_lots: List[PositionLot] = Field(default_factory=list)
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    is_authoritative: bool = False
    metadata: Dict[str, Any] = Field(default_factory=dict)


class PositionLifecycleEvent(BaseModel):
    event_id: str
    state_id: str
    previous_lifecycle: LifecycleState
    new_lifecycle: LifecycleState
    reason: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    source_ref_id: Optional[str] = None


class PositionExposureView(BaseModel):
    symbol: str
    gross_exposure: Decimal
    net_directional_exposure: Decimal
    hedge_adjusted_exposure: Decimal
    residual_directional_exposure: Decimal
    base_currency: str
    quote_currency: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    caveats: List[str] = Field(default_factory=list)


class RealizedPnLRecord(BaseModel):
    record_id: str
    symbol: str
    sleeve_id: str
    amount: Decimal
    currency: str
    source_lot_id: str
    close_fill_id: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    proof_notes: List[str] = Field(default_factory=list)


class UnrealizedPnLRecord(BaseModel):
    record_id: str
    symbol: str
    sleeve_id: str
    amount: Decimal
    currency: str
    mark_price: Decimal
    mark_source: str
    mark_timestamp: datetime
    confidence: float
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    caveats: List[str] = Field(default_factory=list)


class FeeAttributionRecord(BaseModel):
    record_id: str
    symbol: str
    amount: Decimal
    currency: str
    fee_type: PnlComponent
    source_fill_id: Optional[str] = None
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class FundingAttributionRecord(BaseModel):
    record_id: str
    symbol: str
    amount: Decimal
    currency: str
    funding_rate: Decimal
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class CarryAttributionRecord(BaseModel):
    record_id: str
    symbol: str
    amount: Decimal
    currency: str
    description: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class PositionPnLBreakdown(BaseModel):
    symbol: str
    realized_pnl: Decimal
    unrealized_pnl: Decimal
    total_fees: Decimal
    total_funding: Decimal
    total_carry: Decimal
    currency: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class PositionDivergenceReport(BaseModel):
    report_id: str
    symbol: str
    severity: DivergenceSeverity
    runtime_qty: Decimal
    ledger_qty: Optional[Decimal]
    shadow_qty: Optional[Decimal]
    description: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    downstream_impact_hints: List[str] = Field(default_factory=list)


class PositionEquivalenceReport(BaseModel):
    report_id: str
    symbol: str
    verdict: EquivalenceVerdict
    environment_a: str
    environment_b: str
    discrepancies: List[str] = Field(default_factory=list)
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class PositionTrustVerdict(BaseModel):
    verdict: TrustVerdict
    symbol: str
    reasons: List[str] = Field(default_factory=list)
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    breakdown: Dict[str, Any] = Field(default_factory=dict)


class PositionManifestEntry(BaseModel):
    state_id: str
    symbol: str
    quantity: Decimal
    hash: str


class PositionManifest(BaseModel):
    manifest_id: str
    entries: List[PositionManifestEntry] = Field(default_factory=list)
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    trust_verdict: Optional[PositionTrustVerdict] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)


class PositionAuditRecord(BaseModel):
    record_id: str
    action: str
    target_id: str
    details: Dict[str, Any] = Field(default_factory=dict)
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class PositionArtifactManifest(BaseModel):
    artifact_id: str
    manifest_id: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
