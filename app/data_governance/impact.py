from typing import List, Dict
from app.data_governance.models import DatasetRef, DownstreamImpactReport, LineageNode
from app.data_governance.enums import ImpactSeverity
from app.data_governance.lineage import LineageGraph

class ImpactAnalyzer:
    def __init__(self, lineage_graph: LineageGraph):
        self.lineage_graph = lineage_graph

    def analyze(self, dataset_ref: DatasetRef) -> DownstreamImpactReport:
        # Simplistic analysis based on downstream node count and types
        node_id = f"{dataset_ref.dataset_id}:{dataset_ref.version}"

        try:
             downstream_nodes = self.lineage_graph.get_downstream(node_id)
        except Exception:
             downstream_nodes = []

        impacted = [n.producing_module for n in downstream_nodes]

        severity = ImpactSeverity.LOW
        if len(impacted) > 5:
            severity = ImpactSeverity.CRITICAL
        elif len(impacted) > 2:
            severity = ImpactSeverity.HIGH
        elif len(impacted) > 0:
             severity = ImpactSeverity.MEDIUM

        recommended = ["Review downstream ML datasets", "Check analytics summaries"] if severity != ImpactSeverity.LOW else []
        blockers = ["ML Model Training", "Live Strategy Execution"] if severity in [ImpactSeverity.CRITICAL, ImpactSeverity.HIGH] else []

        return DownstreamImpactReport(
            dataset_ref=dataset_ref,
            impacted_components=impacted,
            severity=severity,
            recommended_checks=recommended,
            likely_blockers=blockers
        )
