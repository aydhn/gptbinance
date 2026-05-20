from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from app.semantic_plane.enums import (
    SemanticClass, TermClass, EntityClass, MetricClass,
    UnitClass, ThresholdClass, LabelClass, AliasClass,
    ConflictClass, InterpretationClass, EquivalenceVerdict, TrustVerdict
)

class SemanticObjectRef(BaseModel):
    semantic_id: str
    class_name: SemanticClass
    name: str

class CanonicalDefinitionRecord(BaseModel):
    definition_id: str
    semantic_id: str
    authoritative_text: str
    clarity_notes: str = ""
    is_superseded: bool = False

class AliasRecord(BaseModel):
    alias_id: str
    semantic_id: str
    alias_term: str
    alias_class: AliasClass
    caveats: str = ""

class InterpretationRecord(BaseModel):
    interpretation_id: str
    semantic_id: str
    interpretation_class: InterpretationClass
    sufficiency_notes: str = ""

class TermRecord(BaseModel):
    term_id: str
    name: str
    term_class: TermClass
    proof_notes: str = ""
    lineage_refs: List[str] = Field(default_factory=list)
    canonical_definition: Optional[CanonicalDefinitionRecord] = None
    aliases: List[AliasRecord] = Field(default_factory=list)
    interpretations: List[InterpretationRecord] = Field(default_factory=list)

class EntityRecord(BaseModel):
    entity_id: str
    name: str
    entity_class: EntityClass
    boundary_notes: str = ""
    lineage_refs: List[str] = Field(default_factory=list)

class MeasureDefinitionRecord(BaseModel):
    measure_id: str
    numerator_basis: str
    denominator_basis: str
    aggregation_semantics: str
    sampling_semantics: str
    window_semantics: str
    proof_notes: str = ""

class MetricRecord(BaseModel):
    metric_id: str
    name: str
    metric_class: MetricClass
    formula_notes: str = ""
    measure_definition: Optional[MeasureDefinitionRecord] = None
    lineage_refs: List[str] = Field(default_factory=list)

class UnitRecord(BaseModel):
    unit_id: str
    semantic_id: str
    unit_class: UnitClass
    conversion_caveats: str = ""

class ThresholdRecord(BaseModel):
    threshold_id: str
    semantic_id: str
    threshold_class: ThresholdClass
    implication_notes: str = ""

class LabelRecord(BaseModel):
    label_id: str
    name: str
    label_class: LabelClass
    burden_notes: str = ""

class EnumSemanticRecord(BaseModel):
    enum_id: str
    value_meaning: str
    is_deprecated: bool = False
    drift_notes: str = ""

class ContextRecord(BaseModel):
    context_id: str
    semantic_id: str
    context_type: str
    specific_meaning_notes: str = ""

class DisambiguationRecord(BaseModel):
    disambiguation_id: str
    semantic_id: str
    ambiguity_source: str
    resolution_notes: str = ""

class ObligationSemanticsRecord(BaseModel):
    obligation_id: str
    semantic_id: str
    action_mapping: str
    proof_notes: str = ""

class SemanticConflictRecord(BaseModel):
    conflict_id: str
    semantic_id: str
    conflict_class: ConflictClass
    unresolved_notes: str = ""

class SemanticDriftRecord(BaseModel):
    drift_id: str
    semantic_id: str
    drift_type: str
    severity: str
    proof_notes: str = ""

class TranslationLossRecord(BaseModel):
    translation_id: str
    semantic_id: str
    loss_type: str
    portability_warnings: str = ""

class SemanticComparisonRecord(BaseModel):
    comparison_id: str
    base_semantic_id: str
    target_semantic_id: str
    comparison_type: str
    findings: str = ""

class SemanticForecastReport(BaseModel):
    forecast_id: str
    alias_confusion_growth: str
    drift_likelihood: str
    threshold_misuse_forecast: str
    translation_loss_forecast: str
    ambiguity_recurrence: str

class SemanticDebtRecord(BaseModel):
    debt_id: str
    debt_type: str
    severity: str
    unresolved_conflict_debt: str = ""

class SemanticEquivalenceReport(BaseModel):
    equivalence_id: str
    semantic_id: str
    verdict: EquivalenceVerdict
    blockers: List[str] = Field(default_factory=list)

class SemanticDivergenceReport(BaseModel):
    divergence_id: str
    semantic_id: str
    divergence_type: str
    severity: str
    blast_radius: str

class SemanticTrustVerdict(BaseModel):
    verdict_id: str
    semantic_id: str
    verdict: TrustVerdict
    blockers: List[str] = Field(default_factory=list)
    caveats: str = ""

class SemanticArtifactManifest(BaseModel):
    manifest_id: str
    semantic_id: str
    term_refs: List[str] = Field(default_factory=list)
    metric_refs: List[str] = Field(default_factory=list)
    hash: str

class SemanticPlaneConfig(BaseModel):
    strict_mode: bool = True
