from pydantic import BaseModel
from typing import List, Dict, Optional, Any
from app.viability_plane.enums import *

class ViabilityPlaneConfig(BaseModel):
    strict_subsidy_checks: bool = True
    forbid_hidden_burdens: bool = True

class ViabilityObject(BaseModel):
    viability_id: str
    v_class: str
    owner: str
    scope: str
    economics_posture: Dict[str, Any]
    sustainability_posture: Dict[str, Any]

class RunwayRecord(BaseModel):
    runway_id: str
    runway_class: RunwayClass
    months_remaining: float
    basis_notes: str

class CostBurdenRecord(BaseModel):
    burden_id: str
    burden_class: BurdenClass
    description: str

class SubsidyRecord(BaseModel):
    subsidy_id: str
    subsidy_class: SubsidyClass
    provider: str

class AffordabilityRecord(BaseModel):
    affordability_id: str
    affordability_class: AffordabilityClass

class SustainabilityMarginRecord(BaseModel):
    margin_id: str
    sustainability_class: SustainabilityClass

class ViabilityTrustVerdict(BaseModel):
    verdict: TrustVerdict
    breakdown: Dict[str, Any]
    notes: str
