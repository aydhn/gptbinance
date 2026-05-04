from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime

from app.order_intent.enums import (
    IntentType,
    PlanType,
    OrderLegType,
    VenueProduct,
    AccountMode,
    PositionMode,
    CompileVerdict,
    BorrowMode,
    SafetyMode,
    OrderSide,
    PositionSide,
)


class OrderIntentConfig(BaseModel):
    strict_mode: bool = True
    default_safety_mode: SafetyMode = SafetyMode.STRICT
    allow_implicit_borrow: bool = False


class HighLevelIntent(BaseModel):
    intent_id: str
    intent_type: IntentType
    symbol: str
    product: VenueProduct
    side: OrderSide
    size: float
    position_side: Optional[PositionSide] = None
    workspace_id: str
    profile_id: str
    created_at: datetime
    metadata: Dict[str, Any] = Field(default_factory=dict)


class AccountModeSnapshot(BaseModel):
    timestamp: datetime
    active_modes: List[AccountMode]
    futures_position_mode: Optional[PositionMode] = None


class IntentContext(BaseModel):
    account_snapshot: AccountModeSnapshot
    existing_exposure: float = 0.0
    borrowed_amount: float = 0.0
    available_balance: float = 0.0
    event_risk_active: bool = False
    cross_book_conflict: bool = False
    capital_tier_allows_new: bool = True
    authorized: bool = True


class IntentScope(BaseModel):
    allowed_products: List[VenueProduct]
    requires_existing_position: bool = False


class IntentLeg(BaseModel):
    leg_id: str
    leg_type: OrderLegType
    symbol: str
    side: Optional[OrderSide] = None
    size: float
    position_side: Optional[PositionSide] = None
    reduce_only: bool = False
    close_position: bool = False
    metadata: Dict[str, Any] = Field(default_factory=dict)


class CompiledOrderLeg(BaseModel):
    leg_id: str
    leg_type: OrderLegType
    symbol: str
    product: VenueProduct
    side: Optional[OrderSide] = None
    size: float
    position_side: Optional[PositionSide] = None
    reduce_only: bool = False
    close_position: bool = False
    borrow_mode: Optional[BorrowMode] = None
    dependency_leg_ids: List[str] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)


class CompiledOrderPlan(BaseModel):
    plan_id: str
    intent_id: str
    plan_type: PlanType
    legs: List[CompiledOrderLeg]
    created_at: datetime
    compiled_at: datetime


class VenueSemanticsProfile(BaseModel):
    product: VenueProduct
    requires_position_side: bool = False
    supports_reduce_only: bool = False
    supports_close_position: bool = False
    supports_borrow: bool = False


class MarginBorrowPlan(BaseModel):
    asset: str
    amount: float


class MarginRepayPlan(BaseModel):
    asset: str
    amount: float


class ReduceOnlyPlan(BaseModel):
    symbol: str
    side: OrderSide
    size: float


class CloseOnlyPlan(BaseModel):
    symbol: str
    position_side: PositionSide


class ClosePositionPlan(BaseModel):
    symbol: str
    position_side: PositionSide


class PlanExplanation(BaseModel):
    reason: str
    field_changes: Dict[str, Any] = Field(default_factory=dict)


class PlanValidationResult(BaseModel):
    is_valid: bool
    errors: List[str] = Field(default_factory=list)
    warnings: List[str] = Field(default_factory=list)


class PlanDiff(BaseModel):
    requested_size: float
    compiled_size: float
    is_multi_leg: bool
    diff_reasons: List[str] = Field(default_factory=list)


class CompileAuditRecord(BaseModel):
    run_id: str
    intent_id: str
    verdict: CompileVerdict
    reasons: List[str] = Field(default_factory=list)
    timestamp: datetime


class IntentCompilationResult(BaseModel):
    intent: HighLevelIntent
    plan: Optional[CompiledOrderPlan] = None
    verdict: CompileVerdict
    audit_record: CompileAuditRecord
    explanation: Optional[PlanExplanation] = None
    diff: Optional[PlanDiff] = None
    validation_result: Optional[PlanValidationResult] = None


class CompileArtifactManifest(BaseModel):
    run_id: str
    intent_id: str
    plan_id: Optional[str] = None
    timestamp: datetime
