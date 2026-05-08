from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime, timezone
from app.ledger_plane.enums import *

class LedgerEntryRef(BaseModel):
    entry_id: str

class LedgerEntry(BaseModel):
    id: str
    ledger_class: LedgerClass
    asset: str
    amount: float
    account_scope: str
    source_ref: str
    timestamp: datetime
    metadata: Dict[str, Any] = Field(default_factory=dict)

class CashflowRef(BaseModel):
    cashflow_id: str

class CashflowRecord(BaseModel):
    id: str
    cashflow_class: CashflowClass
    asset: str
    amount: float
    account_scope: str
    direction: str # in, out
    timestamp: datetime
    metadata: Dict[str, Any] = Field(default_factory=dict)

class BalanceBucket(BaseModel):
    bucket_class: BalanceClass
    amount: float
    asset: str
    metadata: Dict[str, Any] = Field(default_factory=dict)

class BalanceStateRef(BaseModel):
    state_id: str

class BalanceState(BaseModel):
    id: str
    account_scope: str
    asset: str
    buckets: List[BalanceBucket]
    timestamp: datetime
    authoritative: bool = False
    metadata: Dict[str, Any] = Field(default_factory=dict)

class CollateralStateRef(BaseModel):
    state_id: str

class CollateralState(BaseModel):
    id: str
    account_scope: str
    asset: str
    collateral_class: CollateralClass
    amount: float
    timestamp: datetime
    metadata: Dict[str, Any] = Field(default_factory=dict)

class TransferRecord(BaseModel):
    id: str
    transfer_class: TransferClass
    asset: str
    amount: float
    source_scope: str
    target_scope: str
    status: str # pending, settled
    timestamp: datetime
    metadata: Dict[str, Any] = Field(default_factory=dict)

class TransferChain(BaseModel):
    chain_id: str
    records: List[TransferRecord]

class EquityView(BaseModel):
    id: str
    account_scope: str
    equity_class: EquityClass
    total_value: float
    currency: str
    timestamp: datetime
    metadata: Dict[str, Any] = Field(default_factory=dict)

class AccountScope(BaseModel):
    scope_id: str
    scope_class: AccountScopeClass
    metadata: Dict[str, Any] = Field(default_factory=dict)

class LedgerManifestEntry(BaseModel):
    ref_id: str
    ref_type: str # entry, balance, collateral, etc.

class LedgerManifest(BaseModel):
    manifest_id: str
    entries: List[LedgerManifestEntry]
    timestamp: datetime
    hash_value: str

class LedgerDivergenceReport(BaseModel):
    id: str
    severity: DivergenceSeverity
    description: str
    timestamp: datetime
    metadata: Dict[str, Any] = Field(default_factory=dict)

class LedgerEquivalenceReport(BaseModel):
    id: str
    verdict: EquivalenceVerdict
    description: str
    timestamp: datetime
    metadata: Dict[str, Any] = Field(default_factory=dict)

class LedgerTrustVerdict(BaseModel):
    id: str
    verdict: TrustVerdict
    reasons: List[str]
    timestamp: datetime
    metadata: Dict[str, Any] = Field(default_factory=dict)

class LedgerAuditRecord(BaseModel):
    id: str
    action: str
    timestamp: datetime
    metadata: Dict[str, Any] = Field(default_factory=dict)

class LedgerArtifactManifest(BaseModel):
    id: str
    artifacts: List[str]
    timestamp: datetime
