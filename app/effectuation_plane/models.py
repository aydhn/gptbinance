from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from app.effectuation_plane.enums import *

class EffectuationObjectRef(BaseModel):
    effectuation_id: str

class EffectuationObject(BaseModel):
    effectuation_id: str
    owner: str
    scope: str
    execution_posture: str
    completion_posture: str

class EffectuationRecord(BaseModel):
    effectuation_id: str
    state: str

class ExecutableOrderRecord(BaseModel):
    order_id: str
    effectuation_id: str

class ExecutionTargetRecord(BaseModel):
    target_id: str

class ExecutionActorRecord(BaseModel):
    actor_id: str

class ExecutionStepRecord(BaseModel):
    step_id: str

class DependencyGateRecord(BaseModel):
    gate_id: str

class MilestoneRecord(BaseModel):
    milestone_id: str

class DeadlineRecord(BaseModel):
    deadline_id: str

class ExecutionAttemptRecord(BaseModel):
    attempt_id: str

class PartialCompletionRecord(BaseModel):
    completion_id: str

class CompletionProofRecord(BaseModel):
    proof_id: str

class CompletionVerificationRecord(BaseModel):
    verification_id: str

class BeneficiaryOutcomeRecord(BaseModel):
    outcome_id: str

class RollbackRecord(BaseModel):
    rollback_id: str

class NonComplianceRecord(BaseModel):
    noncompliance_id: str

class SlippageRecord(BaseModel):
    slippage_id: str

class ResidualTailRecord(BaseModel):
    tail_id: str

class DelegatedExecutionRecord(BaseModel):
    delegation_id: str

class OrphanExecutionRecord(BaseModel):
    orphan_id: str

class EffectuationDebtRecord(BaseModel):
    debt_id: str

class EffectuationDriftRecord(BaseModel):
    drift_id: str

class EffectuationComparisonRecord(BaseModel):
    comparison_id: str

class EffectuationTrustVerdict(BaseModel):
    effectuation_id: str
    verdict: TrustVerdict

class EffectuationManifest(BaseModel):
    effectuation_id: str
    data: Dict[str, Any]

class EffectuationPlaneConfig(BaseModel):
    strict_mode: bool = True
