from pydantic import BaseModel
from typing import List, Dict, Any, Optional
from app.clearing_plane.enums import ClearingClass, AccountClass, TradeStatus, SegregationClass, MarginClass, DefaultClass, AuctionClass, RecoveryClass, DebtClass, EquivalenceVerdict, TrustVerdict

class ClearingPlaneConfig(BaseModel):
    strict_novation: bool = True
    enforce_segregation: bool = True
    forbid_fake_portability: bool = True

class ClearingObject(BaseModel):
    clearing_id: str
    object_class: str
    owner: str
    scope: str
    novation_posture: str
    default_management_posture: str
