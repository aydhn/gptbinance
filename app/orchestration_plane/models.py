from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from .enums import OrchestrationClass, IntentClass, PlanClass, TrustVerdict

class OrchestrationObjectRef(BaseModel):
    orchestration_id: str
    version: str

class OrchestrationPlaneConfig(BaseModel):
    strict_dependency_enforcement: bool = True
    require_rollback_plan: bool = True

class InterventionIntentRecord(BaseModel):
    intent_id: str
    intent_class: IntentClass
    description: str

class ExecutablePlanRecord(BaseModel):
    plan_id: str
    plan_class: PlanClass
    steps: List[str]

class RollbackRecord(BaseModel):
    rollback_id: str
    is_tested: bool
    compensating_actions: List[str]

class OrchestrationTrustVerdict(BaseModel):
    orchestration_id: str
    verdict: TrustVerdict
    factors: Dict[str, str]
