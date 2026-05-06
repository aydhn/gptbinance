from app.evidence_graph.artefacts import ArtefactRegistry
from app.evidence_graph.relations import RelationRegistry
from app.evidence_graph.ingest import ArtefactIngestor
from app.evidence_graph.lineage import LineageEngine
from app.evidence_graph.dependencies import DependencyEngine
from app.evidence_graph.cases import CaseFileAssembler
from app.evidence_graph.packs import EvidencePackBuilder
from app.evidence_graph.queries import GraphQueryEngine
from app.evidence_graph.redaction import RedactionEngine
from app.evidence_graph.gaps import GapDetector
from app.evidence_graph.history import HistoryEngine
from app.evidence_graph.storage import EvidenceGraphStorage
from app.evidence_graph.models import EvidenceGraphConfig


class EvidenceGraphRepository:
    def __init__(self, config: EvidenceGraphConfig):
        self.config = config
        self.storage = EvidenceGraphStorage(config)

        self.artefact_registry = ArtefactRegistry()
        self.relation_registry = RelationRegistry()

        self.ingestor = ArtefactIngestor(self.artefact_registry)
        self.lineage_engine = LineageEngine(
            self.artefact_registry, self.relation_registry
        )
        self.dependency_engine = DependencyEngine(
            self.artefact_registry, self.relation_registry
        )

        self.case_assembler = CaseFileAssembler(
            self.artefact_registry, self.lineage_engine
        )
        self.pack_builder = EvidencePackBuilder(self.lineage_engine)

        self.query_engine = GraphQueryEngine(
            self.artefact_registry, self.relation_registry
        )
        self.redaction_engine = RedactionEngine({})  # Configure policies as needed
        self.gap_detector = GapDetector(self.artefact_registry, self.relation_registry)
        self.history_engine = HistoryEngine(
            self.artefact_registry, self.relation_registry
        )

    # Simplified API for outer layers
    def add_artefact(self, data: dict, mapping: dict):
        art = self.ingestor.ingest_from_source(data, mapping)
        self.storage.save_artefact(art)
        return art

    def add_relation(
        self, source_id: str, source_type, target_id: str, target_type, rel_type
    ):
        rel = self.relation_registry.add_relation(
            source_id, source_type, target_id, target_type, rel_type
        )
        self.storage.save_relation(rel)
        return rel
