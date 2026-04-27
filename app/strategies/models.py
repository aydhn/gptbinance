from typing import Dict, List, Any, Optional
from pydantic import BaseModel, Field
from datetime import datetime
from app.strategies.enums import (
    StrategyType,
    SignalDirection,
    SignalStatus,
    ConflictType,
    ResolutionType,
    RationaleCategory,
    CooldownScope,
)


class StrategySpec(BaseModel):
    name: str
    strategy_type: StrategyType
    required_features: List[str] = Field(default_factory=list)
    min_history: int = 0
    parameters: Dict[str, Any] = Field(default_factory=dict)


class StrategyContext(BaseModel):
    symbol: str
    interval: str
    timestamp: datetime
    features: Dict[str, Any] = Field(default_factory=dict)
    run_id: Optional[str] = None


class StrategyRationale(BaseModel):
    category: RationaleCategory
    reason: str
    supporting_values: Dict[str, Any] = Field(default_factory=dict)


class StrategyScore(BaseModel):
    value: float = 0.0
    confidence: float = 0.0
    quality: float = 0.0
    components: Dict[str, float] = Field(default_factory=dict)


class SignalCandidate(BaseModel):
    strategy_name: str
    symbol: str
    interval: str
    timestamp: datetime
    direction: SignalDirection
    status: SignalStatus = SignalStatus.ACCEPTED
    score: StrategyScore = Field(default_factory=StrategyScore)
    rationale: List[StrategyRationale] = Field(default_factory=list)


class EntryIntentCandidate(BaseModel):
    strategy_name: str
    symbol: str
    timestamp: datetime
    direction: SignalDirection
    score: float
    confidence: float
    rationale: List[StrategyRationale] = Field(default_factory=list)


class ExitIntentCandidate(BaseModel):
    strategy_name: str
    symbol: str
    timestamp: datetime
    direction: SignalDirection  # Direction of the position to exit
    score: float
    rationale: List[StrategyRationale] = Field(default_factory=list)


class StrategyEvaluationResult(BaseModel):
    strategy_name: str
    symbol: str
    timestamp: datetime
    signal: Optional[SignalCandidate] = None
    entry_intent: Optional[EntryIntentCandidate] = None
    exit_intent: Optional[ExitIntentCandidate] = None
    is_active: bool = False
    error: Optional[str] = None


class StrategyStateSnapshot(BaseModel):
    strategy_name: str
    symbol: str
    last_signal_time: Optional[datetime] = None
    last_direction: Optional[SignalDirection] = None
    internal_state: Dict[str, Any] = Field(default_factory=dict)


class SignalConflict(BaseModel):
    symbol: str
    timestamp: datetime
    conflict_type: ConflictType
    intents: List[EntryIntentCandidate] = Field(default_factory=list)


class SignalResolution(BaseModel):
    symbol: str
    timestamp: datetime
    resolution_type: ResolutionType
    resolved_intent: Optional[EntryIntentCandidate] = None
    reason: str


class CooldownState(BaseModel):
    scope: CooldownScope
    target: str  # symbol or strategy name
    expires_at: datetime
    reason: str


class SignalBatch(BaseModel):
    timestamp: datetime
    symbol: str
    raw_signals: List[SignalCandidate] = Field(default_factory=list)
    raw_entry_intents: List[EntryIntentCandidate] = Field(default_factory=list)
    raw_exit_intents: List[ExitIntentCandidate] = Field(default_factory=list)
    resolved_entry_intent: Optional[EntryIntentCandidate] = None
    resolved_exit_intents: List[ExitIntentCandidate] = Field(default_factory=list)
    conflicts_detected: List[SignalConflict] = Field(default_factory=list)
    resolutions: List[SignalResolution] = Field(default_factory=list)
