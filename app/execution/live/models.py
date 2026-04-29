from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List
from decimal import Decimal
from datetime import datetime
from app.execution.live.enums import (
    ExecutionEnvironment,
    OrderLifecycleStatus,
    ReconciliationStatus,
    ExecutionHealthStatus,
    UserStreamEventType,
)
from app.core.models import OrderSide, OrderType


class ExecutionConfig(BaseModel):
    environment: ExecutionEnvironment = Field(default=ExecutionEnvironment.TESTNET)
    mainnet_armed: bool = Field(default=False)
    allow_market_orders: bool = Field(default=False)
    dry_run_gates: bool = Field(default=False)


class SafeExecutionGateResult(BaseModel):
    passed: bool
    reason: Optional[str] = None
    severity: Optional[str] = None


class ExecutionIntent(BaseModel):
    symbol: str
    side: OrderSide
    order_type: OrderType
    quantity: Decimal
    price: Optional[Decimal] = None
    intent_id: str
    ttl_seconds: int = 60
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class ExecutionRequest(BaseModel):
    intent: ExecutionIntent
    client_order_id: str
    environment: ExecutionEnvironment


class SubmittedOrder(BaseModel):
    client_order_id: str
    exchange_order_id: Optional[str] = None
    symbol: str
    side: OrderSide
    order_type: OrderType
    quantity: Decimal
    price: Optional[Decimal] = None
    status: OrderLifecycleStatus
    submitted_at: datetime = Field(default_factory=datetime.utcnow)


class ExchangeAck(BaseModel):
    client_order_id: str
    exchange_order_id: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    raw_response: Dict[str, Any]


class ExchangeReject(BaseModel):
    client_order_id: str
    reason: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class OrderLifecycleEvent(BaseModel):
    client_order_id: str
    status: OrderLifecycleStatus
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    details: Optional[Dict[str, Any]] = None


class OrderStateSnapshot(BaseModel):
    client_order_id: str
    exchange_order_id: Optional[str] = None
    symbol: str
    status: OrderLifecycleStatus
    filled_quantity: Decimal = Field(default=Decimal("0"))
    average_price: Optional[Decimal] = None
    last_update: datetime
    is_open: bool


class ExecutionResult(BaseModel):
    success: bool
    client_order_id: str
    status: OrderLifecycleStatus
    message: Optional[str] = None


class CancelRequest(BaseModel):
    client_order_id: str
    symbol: str
    reason: str


class CancelResult(BaseModel):
    success: bool
    client_order_id: str
    status: OrderLifecycleStatus
    message: Optional[str] = None


class ReplaceRequest(BaseModel):
    original_client_order_id: str
    new_intent: ExecutionIntent


class ReconciliationReport(BaseModel):
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    status: ReconciliationStatus
    drift_items: List[str] = Field(default_factory=list)
    repaired_items: List[str] = Field(default_factory=list)
    unresolved_anomalies: List[str] = Field(default_factory=list)


class UserStreamEvent(BaseModel):
    event_type: UserStreamEventType
    timestamp: datetime
    raw_data: Dict[str, Any]


class ExecutionRun(BaseModel):
    run_id: str
    environment: ExecutionEnvironment
    start_time: datetime = Field(default_factory=datetime.utcnow)


class ExecutionAuditRecord(BaseModel):
    run_id: str
    event_type: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    data: Dict[str, Any]


class OrderSubmissionEnvelope(BaseModel):
    request: ExecutionRequest
    raw_payload: Dict[str, Any]


class ExecutionHealthSnapshot(BaseModel):
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    status: ExecutionHealthStatus
    rest_latency_ms: Optional[float] = None
    stream_freshness_seconds: Optional[float] = None
    reject_count: int = 0
    drift_count: int = 0
    open_orders_count: int = 0
    safety_gate_status: Dict[str, bool] = Field(default_factory=dict)


class OpenOrderSnapshot(BaseModel):
    orders: List[OrderStateSnapshot] = Field(default_factory=list)


class AccountExecutionSnapshot(BaseModel):
    balances: Dict[str, Decimal] = Field(default_factory=dict)
    open_orders: OpenOrderSnapshot
