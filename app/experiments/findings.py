from typing import Dict, List, Any
from app.experiments.hypotheses import FindingToHypothesisCompiler, HypothesisRegistry
from app.experiments.enums import HypothesisClass


class FindingIntake:
    def __init__(self, registry: HypothesisRegistry):
        self.registry = registry
        self.compiler = FindingToHypothesisCompiler()
        self.research_backlog: List[Dict[str, Any]] = []

    def process_finding(self, finding: Dict[str, Any]) -> str:
        # Determine hypothesis class based on finding content (simplified)
        h_class = HypothesisClass.OTHER
        summary = finding.get("summary", "").lower()
        if "friction" in summary:
            h_class = HypothesisClass.POLICY_FRICTION_EXCESSIVE_IN_REGIME
        elif "stale" in summary or "truth" in summary:
            h_class = HypothesisClass.MARKET_TRUTH_THRESHOLDS_TOO_SENSITIVE

        rationale = "Automatically generated from high-severity finding."

        hypothesis = self.compiler.compile(finding, h_class, rationale)
        hypothesis_id = self.registry.register(hypothesis)

        self.research_backlog.append(
            {
                "finding_id": finding.get("finding_id"),
                "hypothesis_id": hypothesis_id,
                "status": "pending_experiment",
            }
        )
        return hypothesis_id

    def get_research_backlog(self) -> List[Dict[str, Any]]:
        return self.research_backlog
