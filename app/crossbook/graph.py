from .models import ExposureGraph

class ExposureGraphBuilder:
    def build_graph(self, nodes: list, edges: list) -> ExposureGraph:
        return ExposureGraph(nodes=nodes, edges=edges)
