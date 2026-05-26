from pydantic import BaseModel, Field
from typing import List, Optional, Dict
from app.recapitalization_plane.enums import RecapitalizationClass, FundingClass, DilutionClass, TrustVerdict

class CapitalStackRecord(BaseModel):
    stack_id: str
    pre_recap_value: float
    post_recap_value: float
    is_provisional: bool = False

class InstrumentRecord(BaseModel):
    instrument_id: str
    instrument_type: str
    amount: float
    is_active: bool

class CommitmentRecord(BaseModel):
    commitment_id: str
    investor: str
    amount_committed: float
    is_binding: bool

class FundingRecord(BaseModel):
    funding_id: str
    commitment_id: str
    amount_funded: float
    status: FundingClass

class DilutionRecord(BaseModel):
    dilution_id: str
    affected_class: str
    dilution_percentage: float
    status: DilutionClass

class ControlRightRecord(BaseModel):
    control_id: str
    owner: str
    voting_power: float
    is_shadow_control: bool = False

class RecapitalizationTrustVerdict(BaseModel):
    recapitalization_id: str
    verdict: TrustVerdict
    phantom_capital_detected: bool
    hidden_dilution_detected: bool
    unauthorized_control_shift: bool
    caveats: List[str]

class RecapitalizationObject(BaseModel):
    recapitalization_id: str
    recap_class: RecapitalizationClass
    owner: str
    scope: str
    commitments: List[CommitmentRecord] = []
    fundings: List[FundingRecord] = []
    dilutions: List[DilutionRecord] = []
    controls: List[ControlRightRecord] = []
    capital_stack: Optional[CapitalStackRecord] = None
    is_fully_effective: bool = False
