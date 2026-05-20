from typing import Dict, List, Optional
from app.semantic_plane.models import (
    TermRecord, EntityRecord, MetricRecord, LabelRecord,
    SemanticPlaneConfig, SemanticConflictRecord
)
from app.semantic_plane.enums import SemanticClass, ConflictClass
from app.semantic_plane.exceptions import InvalidSemanticObjectError

class CanonicalSemanticRegistry:
    def __init__(self, config: SemanticPlaneConfig = SemanticPlaneConfig()):
        self.config = config
        self.terms: Dict[str, TermRecord] = {}
        self.entities: Dict[str, EntityRecord] = {}
        self.metrics: Dict[str, MetricRecord] = {}
        self.labels: Dict[str, LabelRecord] = {}
        self.conflicts: Dict[str, SemanticConflictRecord] = {}

    def register_term(self, term: TermRecord):
        if not term.term_id or not term.name:
            raise InvalidSemanticObjectError("Term must have ID and name")

        # Check for same-name, different meaning (simple check)
        for existing_term in self.terms.values():
            if existing_term.name == term.name and existing_term.term_id != term.term_id:
                conflict = SemanticConflictRecord(
                    conflict_id=f"conf_{term.term_id}",
                    semantic_id=term.term_id,  # Link the conflict to the new term causing it
                    conflict_class=ConflictClass.SAME_NAME_DIFFERENT_MEANING,
                    unresolved_notes=f"Term '{term.name}' is overloaded."
                )
                self.conflicts[term.term_id] = conflict # Store by semantic_id for easy lookup in evaluator

        self.terms[term.term_id] = term

    def get_term(self, term_id: str) -> Optional[TermRecord]:
        return self.terms.get(term_id)

    def register_metric(self, metric: MetricRecord):
        if not metric.metric_id or not metric.name:
             raise InvalidSemanticObjectError("Metric must have ID and name")
        self.metrics[metric.metric_id] = metric

    def get_metric(self, metric_id: str) -> Optional[MetricRecord]:
        return self.metrics.get(metric_id)

    def register_entity(self, entity: EntityRecord):
        if not entity.entity_id or not entity.name:
             raise InvalidSemanticObjectError("Entity must have ID and name")
        self.entities[entity.entity_id] = entity

    def register_label(self, label: LabelRecord):
        self.labels[label.label_id] = label
