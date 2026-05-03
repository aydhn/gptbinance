from typing import List, Optional, Dict, Any
from datetime import datetime, timezone
from pydantic import BaseModel, Field
from app.knowledge.enums import (
    KnowledgeItemType,
    KnowledgeScope,
    LessonStatus,
    DocumentStatus,
    QuizVerdict,
    ReadinessLevel,
    ApplicabilityVerdict,
    FreshnessSeverity,
)


class KnowledgeOwner(BaseModel):
    owner_id: str
    team: str


class KnowledgeConfig(BaseModel):
    review_cadence_days: int = 90
    enforce_strict_applicability: bool = True


class ApplicabilityRule(BaseModel):
    rule_id: str
    description: str
    target_profiles: Optional[List[str]] = None
    target_releases: Optional[List[str]] = None
    target_components: Optional[List[str]] = None
    target_actions: Optional[List[str]] = None
    target_alerts: Optional[List[str]] = None


class KnowledgeItemVersion(BaseModel):
    version: str
    created_at: datetime
    author: str
    changes: str


class KnowledgeItem(BaseModel):
    item_id: str
    item_type: KnowledgeItemType
    title: str
    description: str
    owner: KnowledgeOwner
    status: DocumentStatus
    versions: List[KnowledgeItemVersion] = Field(default_factory=list)
    applicability_rules: List[ApplicabilityRule] = Field(default_factory=list)
    last_reviewed_at: datetime
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class Runbook(KnowledgeItem):
    item_type: KnowledgeItemType = KnowledgeItemType.RUNBOOK
    investigation_steps: List[str] = Field(default_factory=list)
    mitigation_steps: List[str] = Field(default_factory=list)
    prerequisite_items: List[str] = Field(default_factory=list)
    required_evidence_refs: List[str] = Field(default_factory=list)


class SopDocument(KnowledgeItem):
    item_type: KnowledgeItemType = KnowledgeItemType.SOP
    steps: List[str] = Field(default_factory=list)
    expected_outcomes: List[str] = Field(default_factory=list)


class Playbook(KnowledgeItem):
    item_type: KnowledgeItemType = KnowledgeItemType.PLAYBOOK
    trigger_conditions: List[str] = Field(default_factory=list)
    response_actions: List[str] = Field(default_factory=list)


class LessonLearned(KnowledgeItem):
    item_type: KnowledgeItemType = KnowledgeItemType.LESSON_LEARNED
    lesson_status: LessonStatus
    source_incident_ref: Optional[str] = None
    source_replay_ref: Optional[str] = None
    findings: List[str] = Field(default_factory=list)
    recommendations: List[str] = Field(default_factory=list)


class KnowledgeLink(BaseModel):
    source_id: str
    target_id: str
    link_type: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class StalenessWarning(BaseModel):
    reason: str
    detected_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class FreshnessReport(BaseModel):
    item_id: str
    severity: FreshnessSeverity
    warnings: List[StalenessWarning] = Field(default_factory=list)
    last_reviewed_at: datetime
    days_since_review: int


class KnowledgeSearchResult(BaseModel):
    item: KnowledgeItem
    score: float
    match_reasons: List[str]
    freshness: FreshnessSeverity


class TrainingModule(BaseModel):
    module_id: str
    title: str
    description: str
    scope: KnowledgeScope
    content_refs: List[str] = Field(default_factory=list)


class TrainingScenario(BaseModel):
    scenario_id: str
    title: str
    description: str
    setup_steps: List[str] = Field(default_factory=list)
    expected_actions: List[str] = Field(default_factory=list)


class QuizQuestion(BaseModel):
    question_id: str
    text: str
    options: List[str]
    correct_option_index: int


class ReadinessQuiz(BaseModel):
    quiz_id: str
    module_id: str
    title: str
    questions: List[QuizQuestion] = Field(default_factory=list)
    passing_score: float


class QuizResult(BaseModel):
    quiz_id: str
    operator_id: str
    score: float
    verdict: QuizVerdict
    taken_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class OperatorReadinessRecord(BaseModel):
    operator_id: str
    role: str
    readiness_level: ReadinessLevel
    completed_quizzes: List[str] = Field(default_factory=list)
    stale_readiness_reasons: List[str] = Field(default_factory=list)
    last_evaluated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )


class KnowledgeCatalogEntry(BaseModel):
    item_id: str
    item_type: KnowledgeItemType
    status: DocumentStatus
    freshness_severity: FreshnessSeverity
    title: str


class KnowledgeAuditRecord(BaseModel):
    record_id: str
    item_id: str
    action: str
    operator_id: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    details: Dict[str, Any] = Field(default_factory=dict)


class KnowledgeArtifactManifest(BaseModel):
    manifest_id: str
    generated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    item_count: int
    items: List[KnowledgeCatalogEntry] = Field(default_factory=list)
