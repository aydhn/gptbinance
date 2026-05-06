from typing import Any
from app.postmortems.models import RootCauseCandidate
from app.postmortems.enums import RootCauseConfidence
from typing import List


class RootCauseEvaluator:
    def evaluate(self, causal_graph: Any) -> List[RootCauseCandidate]:
        candidates = []
        if causal_graph and hasattr(causal_graph, "nodes"):
            for node in causal_graph.nodes:
                if node.node_type == "trigger":
                    candidates.append(
                        RootCauseCandidate(
                            candidate_id=f"rc_{node.node_id}",
                            description=f"Potential root cause from {node.description}",
                            confidence=RootCauseConfidence.LIKELY.value,
                        )
                    )
        if not candidates:
            candidates.append(
                RootCauseCandidate(
                    candidate_id="rc_unknown",
                    description="Unresolved root cause due to insufficient evidence",
                    confidence=RootCauseConfidence.UNRESOLVED.value,
                )
            )
        return candidates
