from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from datetime import datetime, timezone
from app.operating_model_plane.enums import (
    OperatingObjectClass, RoleClass, OwnershipClass, CoverageClass, IndependenceClass, TrustVerdict
)

class RoleRef(BaseModel):
    role_id: str
    role_name: str
    role_class: RoleClass

class OwnershipAssignment(BaseModel):
    assignment_id: str
    target_id: str
    owner_role: RoleRef
    ownership_class: OwnershipClass
    last_attested_at: datetime
    is_stale: bool = False

class EscalationChain(BaseModel):
    chain_id: str
    first_line_role: RoleRef
    management_role: RoleRef
    is_broken: bool = False

class SegregationOfDutiesRecord(BaseModel):
    record_id: str
    proposer_role: RoleRef
    approver_role: RoleRef
    is_violated: bool

class OperatingModelObject(BaseModel):
    operating_id: str
    object_class: OperatingObjectClass
    is_critical: bool
    primary_owner: Optional[OwnershipAssignment]
    backup_coverage: CoverageClass
    escalation_chain: Optional[EscalationChain]

class OperatingModelTrustVerdictReport(BaseModel):
    verdict: TrustVerdict
    breakdown: Dict[str, str]
    stale_owner_debt: bool
    missing_backup_debt: bool
    broken_escalation_debt: bool
    reviewer_conflict_debt: bool
    ownerless_critical_surface: bool
    proof_notes: List[str]
