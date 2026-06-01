from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import datetime
from app.adaptation_plane.enums import (
    AdaptationClass, TriggerClass, HypothesisClass, CorrectiveClass, HardeningClass,
    RecalibrationClass, VerificationClass, SideEffectClass, FitnessClass, RenormalizationClass,
    TrustVerdict, EquivalenceVerdict
)

class AdaptationObjectRef(BaseModel):
    id: str

class AdaptationTriggerRecord(BaseModel):
    trigger_id: str
    adaptation_id: str
    type: TriggerClass
    description: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    lineage_refs: List[str] = []

class RootCauseHypothesisRecord(BaseModel):
    hypothesis_id: str
    adaptation_id: str
    rigor: HypothesisClass
    description: str
    owner: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    lineage_refs: List[str] = []

class CountermeasureRecord(BaseModel):
    countermeasure_id: str
    adaptation_id: str
    scope: str
    description: str
    lineage_refs: List[str] = []

class CorrectivePackageRecord(BaseModel):
    package_id: str
    adaptation_id: str
    sufficiency: CorrectiveClass
    countermeasures: List[CountermeasureRecord] = []
    lineage_refs: List[str] = []

class VerificationWindowRecord(BaseModel):
    window_id: str
    adaptation_id: str
    maturity: VerificationClass
    start_time: datetime
    end_time: Optional[datetime] = None
    lineage_refs: List[str] = []

class SideEffectRecord(BaseModel):
    side_effect_id: str
    adaptation_id: str
    visibility: SideEffectClass
    description: str
    beneficiary_impact: str
    lineage_refs: List[str] = []

class FitnessRestorationRecord(BaseModel):
    fitness_id: str
    adaptation_id: str
    level: FitnessClass
    description: str
    lineage_refs: List[str] = []

class AdaptationRecord(BaseModel):
    adaptation_id: str
    class_type: AdaptationClass
    owner: str
    scope: str
    status: str
    trigger: Optional[AdaptationTriggerRecord] = None
    hypothesis: Optional[RootCauseHypothesisRecord] = None
    corrective_package: Optional[CorrectivePackageRecord] = None
    verification: Optional[VerificationWindowRecord] = None
    side_effects: List[SideEffectRecord] = []
    fitness: Optional[FitnessRestorationRecord] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    lineage_refs: List[str] = []

class AdaptationTrustVerdict(BaseModel):
    verdict_id: str
    adaptation_id: str
    status: TrustVerdict
    breakdown: Dict[str, str]
    timestamp: datetime = Field(default_factory=datetime.utcnow)
