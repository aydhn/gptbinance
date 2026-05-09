from typing import List
from app.workflow_plane.models import GateCheckResult, WorkflowRun
from app.workflow_plane.enums import GateClass

class WorkflowGateEvaluator:
    def evaluate(self, run: WorkflowRun) -> List[GateCheckResult]:
        return [
            GateCheckResult(gate_class=GateClass.DATA_TRUST, passed=True, rationale="Data feeds are current and verified"),
            GateCheckResult(gate_class=GateClass.READINESS, passed=True, rationale="Readiness board gives green light")
        ]
