import uuid
from typing import Dict, List, Any
from app.experiments.models import HypothesisRecord, HypothesisVersion
from app.experiments.enums import HypothesisClass
from app.experiments.exceptions import InvalidHypothesisError


class HypothesisRegistry:
    def __init__(self):
        self._hypotheses: Dict[str, HypothesisRecord] = {}

    def register(self, hypothesis: HypothesisRecord) -> str:
        if not hypothesis.hypothesis_id:
            hypothesis.hypothesis_id = str(uuid.uuid4())
        self._hypotheses[hypothesis.hypothesis_id] = hypothesis
        return hypothesis.hypothesis_id

    def get(self, hypothesis_id: str) -> HypothesisRecord:
        if hypothesis_id not in self._hypotheses:
            raise InvalidHypothesisError(f"Hypothesis {hypothesis_id} not found")
        return self._hypotheses[hypothesis_id]

    def list_all(self) -> List[HypothesisRecord]:
        return list(self._hypotheses.values())


class FindingToHypothesisCompiler:
    def compile(
        self, finding: Dict[str, Any], h_class: HypothesisClass, rationale: str
    ) -> HypothesisRecord:
        v = HypothesisVersion(
            version_id=1, rationale=rationale, author="system_compiler"
        )
        hr = HypothesisRecord(
            hypothesis_id=str(uuid.uuid4()),
            h_class=h_class,
            title=f"Compiled Hypothesis from Finding {finding.get('finding_id', 'unknown')}",
            description=finding.get("summary", "No summary provided"),
            affected_domains=[finding.get("domain", "unknown")],
            expected_measurable_signals=["friction_reduction", "pnl_improvement"],
            disallowed_interpretations=["overfitting_expected"],
            required_evidence=["offline_backtest", "regime_split"],
            risk_notes="Compiled automatically from finding. Needs review.",
            versions=[v],
        )
        return hr
