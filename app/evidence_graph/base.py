from abc import ABC, abstractmethod
from typing import Dict, Any

from app.evidence_graph.models import (
    ArtefactRecord,
    RelationEdge,
    QueryResult,
    QueryRequest,
    EvidenceCaseFile,
)


class ArtefactIngestorBase(ABC):
    @abstractmethod
    def ingest(self, raw_data: Dict[str, Any]) -> ArtefactRecord:
        pass


class RelationBuilderBase(ABC):
    @abstractmethod
    def build_relation(
        self,
        source_id: str,
        target_id: str,
        relation_type: str,
        metadata: Dict[str, Any],
    ) -> RelationEdge:
        pass


class GraphQueryEngineBase(ABC):
    @abstractmethod
    def execute_query(self, request: QueryRequest) -> QueryResult:
        pass


class CaseFileAssemblerBase(ABC):
    @abstractmethod
    def assemble_case_file(self, case_type: str, context_id: str) -> EvidenceCaseFile:
        pass
