import json
import os

from app.evidence_graph.models import EvidenceGraphConfig, ArtefactRecord, RelationEdge
from app.evidence_graph.exceptions import EvidenceGraphStorageError


class EvidenceGraphStorage:
    def __init__(self, config: EvidenceGraphConfig):
        self.config = config
        self.base_path = config.storage_path
        os.makedirs(self.base_path, exist_ok=True)
        self.artefacts_path = os.path.join(self.base_path, "artefacts.jsonl")
        self.relations_path = os.path.join(self.base_path, "relations.jsonl")

    def save_artefact(self, artefact: ArtefactRecord):
        try:
            with open(self.artefacts_path, "a") as f:
                f.write(json.dumps(artefact.__dict__, default=str) + "\n")
        except Exception as e:
            raise EvidenceGraphStorageError(f"Failed to save artefact: {str(e)}")

    def save_relation(self, relation: RelationEdge):
        try:
            with open(self.relations_path, "a") as f:
                f.write(json.dumps(relation.__dict__, default=str) + "\n")
        except Exception as e:
            raise EvidenceGraphStorageError(f"Failed to save relation: {str(e)}")

    # Mock load for testing
    def load_all(self):
        pass
