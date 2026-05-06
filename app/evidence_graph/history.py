from typing import List, Dict
from datetime import datetime

from app.evidence_graph.artefacts import ArtefactRegistry
from app.evidence_graph.relations import RelationRegistry


class HistoryEngine:
    def __init__(
        self, artefact_registry: ArtefactRegistry, relation_registry: RelationRegistry
    ):
        self.artefact_registry = artefact_registry
        self.relation_registry = relation_registry

    def get_snapshot(self, as_of: datetime) -> Dict[str, List]:
        # Filter artefacts and relations created before as_of
        artefacts = [
            a for a in self.artefact_registry.list_artefacts() if a.created_at <= as_of
        ]
        relations = [
            r
            for r in self.relation_registry.get_all_relations()
            if r.created_at <= as_of
        ]
        return {"artefacts": artefacts, "relations": relations}
