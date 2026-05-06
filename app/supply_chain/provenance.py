from app.supply_chain.models import ProvenanceChain, ProvenanceNode


class ProvenanceBuilder:
    def build_chain(
        self, build_manifest_id: str, src_id: str, dep_id: str, timestamp
    ) -> ProvenanceChain:
        nodes = [
            ProvenanceNode(node_id=src_id, node_type="source", timestamp=timestamp),
            ProvenanceNode(node_id=dep_id, node_type="dependency", timestamp=timestamp),
            ProvenanceNode(
                node_id=build_manifest_id, node_type="build", timestamp=timestamp
            ),
        ]
        edges = [
            {"from": src_id, "to": build_manifest_id, "type": "built_from_source"},
            {"from": dep_id, "to": build_manifest_id, "type": "built_with_deps"},
        ]

        return ProvenanceChain(
            id=f"prov_{build_manifest_id}",
            nodes=nodes,
            edges=edges,
            completeness_score=1.0 if src_id and dep_id else 0.5,
        )
