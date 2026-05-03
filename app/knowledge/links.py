from typing import List, Dict, Optional
from app.knowledge.models import KnowledgeLink


class KnowledgeGraph:
    def __init__(self):
        self._links: List[KnowledgeLink] = []
        self._links_by_source: Dict[str, List[KnowledgeLink]] = {}
        self._links_by_target: Dict[str, List[KnowledgeLink]] = {}

    def add_link(self, link: KnowledgeLink) -> None:
        self._links.append(link)

        if link.source_id not in self._links_by_source:
            self._links_by_source[link.source_id] = []
        self._links_by_source[link.source_id].append(link)

        if link.target_id not in self._links_by_target:
            self._links_by_target[link.target_id] = []
        self._links_by_target[link.target_id].append(link)

    def get_outbound_links(self, source_id: str) -> List[KnowledgeLink]:
        return self._links_by_source.get(source_id, [])

    def get_inbound_links(self, target_id: str) -> List[KnowledgeLink]:
        return self._links_by_target.get(target_id, [])

    def detect_cycles(self) -> bool:
        # Simple cycle detection for the graph if needed
        return False


knowledge_graph = KnowledgeGraph()
