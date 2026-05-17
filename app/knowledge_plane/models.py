from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import datetime

class KnowledgePlaneConfig(BaseModel):
    enabled: bool = True
    require_freshness: bool = True
    enforce_applicability: bool = True

class KnowledgeObjectRef(BaseModel):
    knowledge_id: str
    version: Optional[str] = None
    class_name: str

class KnowledgeObject(BaseModel):
    knowledge_id: str
    owner: str
    knowledge_class: str
    authoritative: bool
    scope: List[str]
    metadata: Dict[str, Any] = Field(default_factory=dict)

class KnowledgeSourceRecord(BaseModel):
    knowledge_id: str
    source_uri: str
    source_class: str

class KnowledgeTaxonomyRecord(BaseModel):
    knowledge_id: str
    taxonomy_class: str

class StandardRecord(BaseModel):
    knowledge_id: str
    is_mandatory: bool
    description: str
    control_linkage: Optional[str] = None

class RunbookRecord(BaseModel):
    knowledge_id: str
    usability_score: float
    runbook_class: str

class PlaybookRecord(BaseModel):
    knowledge_id: str
    playbook_type: str

class SopRecord(BaseModel):
    knowledge_id: str
    actor: str

class ChecklistRecord(BaseModel):
    knowledge_id: str
    enforced: bool
    items: List[str]

class ApplicabilityRecord(BaseModel):
    knowledge_id: str
    applicable_environments: List[str]
    applicable_roles: List[str]
    applicable_workflows: List[str]

class FreshnessRecord(BaseModel):
    knowledge_id: str
    status: str # fresh, review_due, stale, expired
    last_reviewed_at: datetime
    next_review_due: datetime

class ReviewRecord(BaseModel):
    knowledge_id: str
    reviewer: str
    review_date: datetime
    status: str
    notes: Optional[str] = None

class SupersessionRecord(BaseModel):
    knowledge_id: str
    superseded_by: Optional[str]
    supersession_class: str

class ConflictRecord(BaseModel):
    knowledge_id: str
    conflicts_with: List[str]
    conflict_class: str
    resolution_notes: Optional[str] = None

class AdoptionRecord(BaseModel):
    knowledge_id: str
    adoption_level: str
    adopted_by: List[str]

class AttestationRecord(BaseModel):
    knowledge_id: str
    attested_by: str
    attestation_date: datetime
    attestation_class: str

class RetrievalRecord(BaseModel):
    knowledge_id: str
    retrieval_date: datetime
    retriever: str

class UsabilityReport(BaseModel):
    knowledge_id: str
    is_usable: bool
    issues: List[str]

class CoverageReport(BaseModel):
    surface: str
    covered_by: List[str]
    gaps: List[str]

class KnowledgeGapRecord(BaseModel):
    missing_type: str
    severity: str
    description: str

class KnowledgeForecastReport(BaseModel):
    metric: str
    forecast_value: float

class KnowledgeDebtRecord(BaseModel):
    debt_type: str
    severity: str
    description: str
    knowledge_id: Optional[str] = None

class KnowledgeEquivalenceReport(BaseModel):
    surface: str
    is_equivalent: bool
    differences: List[str]

class KnowledgeDivergenceReport(BaseModel):
    surface: str
    divergence_score: float
    description: str

class KnowledgeTrustVerdict(BaseModel):
    verdict: str # trusted, caution, degraded, blocked, review_required
    reasons: List[str]

class KnowledgeAuditRecord(BaseModel):
    knowledge_id: str
    action: str
    timestamp: datetime
    actor: str

class KnowledgeArtifactManifest(BaseModel):
    manifest_id: str
    objects: List[KnowledgeObject]
    generated_at: datetime
