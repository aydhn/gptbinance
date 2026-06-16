from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime
from app.collateral_plane.enums import (
    CollateralClass, EligibilityClass, ValuationClass,
    PerfectionClass, LiquidationClass, TrustVerdictType
)

class CollateralPlaneConfig(BaseModel):
    strict_valuation_staleness_hours: int = 24
    allow_rehypothecation: bool = False
    require_independent_custody: bool = True

class CollateralObjectRef(BaseModel):
    collateral_id: str
    version: int

class CollateralObject(BaseModel):
    collateral_id: str
    owner_id: str
    scope: str
    security_posture: str
    liquidation_posture: str
    status: str
    lineage_refs: List[str] = Field(default_factory=list)

class ValuationRecord(BaseModel):
    valuation_id: str
    collateral_id: str
    valuation_class: ValuationClass
    assessed_value: float
    currency: str
    haircut_percentage: float
    timestamp: datetime
    evaluator_id: str
    lineage_refs: List[str] = Field(default_factory=list)

class EncumbranceRecord(BaseModel):
    encumbrance_id: str
    collateral_id: str
    is_hidden: bool
    lien_amount: float
    priority_rank: int
    lien_holder: str
    lineage_refs: List[str] = Field(default_factory=list)

class PerfectionRecord(BaseModel):
    perfection_id: str
    collateral_id: str
    perfection_class: PerfectionClass
    jurisdiction: str
    method: str
    timestamp: datetime
    lineage_refs: List[str] = Field(default_factory=list)

class LiquidationRecord(BaseModel):
    liquidation_id: str
    collateral_id: str
    liquidation_class: LiquidationClass
    realized_value: float
    slippage: float
    deficiency: float
    surplus: float
    timestamp: datetime
    authority_ref: str
    lineage_refs: List[str] = Field(default_factory=list)

class CollateralDebtRecord(BaseModel):
    debt_id: str
    collateral_id: str
    debt_type: str
    severity: str
    description: str
    timestamp: datetime
    lineage_refs: List[str] = Field(default_factory=list)

class CollateralTrustVerdict(BaseModel):
    collateral_id: str
    verdict: TrustVerdictType
    asset_clarity: bool
    eligibility_sufficiency: bool
    valuation_sufficiency: bool
    perfection_integrity: bool
    liquidation_sufficiency: bool
    cautions: List[str]
    timestamp: datetime
