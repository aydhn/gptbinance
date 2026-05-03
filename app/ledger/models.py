from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime, timezone
from app.ledger.enums import (
    LedgerAccountType,
    LedgerEntryType,
    MovementClass,
    ReconciliationVerdict,
    LotMethod,
    BalanceStatus,
    SourceSystem,
    ScopeType,
    DiscrepancySeverity,
    LedgerVerdict,
)


class LedgerConfig(BaseModel):
    strict_balancing: bool = True
    default_lot_method: LotMethod = LotMethod.FIFO
    default_scope: ScopeType = ScopeType.PAPER


class LedgerAccountRef(BaseModel):
    account_id: str
    workspace_id: str
    profile_id: str
    scope: ScopeType


class LedgerAccount(BaseModel):
    ref: LedgerAccountRef
    name: str
    type: LedgerAccountType
    asset: Optional[str] = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class LedgerPosting(BaseModel):
    account_ref: LedgerAccountRef
    amount: float
    asset: str
    direction: int = Field(..., description="1 for debit, -1 for credit")


class LedgerEventSource(BaseModel):
    system: SourceSystem
    event_id: str
    timestamp: datetime
    metadata: Dict[str, Any] = Field(default_factory=dict)


class LedgerEvent(BaseModel):
    event_id: str
    type: LedgerEntryType
    source: LedgerEventSource
    amount: float
    asset: str
    metadata: Dict[str, Any] = Field(default_factory=dict)


class LedgerEntry(BaseModel):
    entry_id: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    type: LedgerEntryType
    event_ref: str
    postings: List[LedgerPosting]
    scope: ScopeType
    classification: MovementClass
    metadata: Dict[str, Any] = Field(default_factory=dict)


class BalanceSnapshot(BaseModel):
    snapshot_id: str
    timestamp: datetime
    account_ref: LedgerAccountRef
    asset: str
    balance: float
    source: str


class ReconciliationDifference(BaseModel):
    asset: str
    internal_balance: float
    external_balance: float
    delta: float
    severity: DiscrepancySeverity
    recommended_action: str


class ReconciliationResult(BaseModel):
    run_id: str
    timestamp: datetime
    scope: ScopeType
    verdict: ReconciliationVerdict
    differences: List[ReconciliationDifference]


class CostBasisLot(BaseModel):
    lot_id: str
    asset: str
    acquired_amount: float
    remaining_amount: float
    cost_basis_total: float
    cost_basis_per_unit: float
    acquired_at: datetime
    scope: ScopeType
    status: str = "OPEN"
    metadata: Dict[str, Any] = Field(default_factory=dict)


class AssetBalanceSummary(BaseModel):
    asset: str
    total_balance: float
    available_balance: float
    locked_balance: float
    unrealized_pnl: float = 0.0
    realized_pnl: float = 0.0
    status: BalanceStatus


class BalanceExplainResult(BaseModel):
    asset: str
    scope: ScopeType
    current_balance: float
    total_inflows: float
    total_outflows: float
    recent_entries: List[LedgerEntry]
    unexplained_delta: float
    verdict: LedgerVerdict


class LedgerArtifactManifest(BaseModel):
    manifest_id: str
    timestamp: datetime
    entry_count: int
    hash: str
