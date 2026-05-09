from app.workflow_plane.models import WorkflowRun, WorkflowTrustVerdict
from app.workflow_plane.enums import RunState, TrustVerdict

class WorkflowTrustEvaluator:
    def evaluate(self, run: WorkflowRun) -> WorkflowTrustVerdict:
        if run.state == RunState.COMPLETED:
            for gate in run.gate_results:
                if gate.bypassed:
                    return WorkflowTrustVerdict(verdict=TrustVerdict.CAUTION, factors={"gate": "bypassed"})
            return WorkflowTrustVerdict(verdict=TrustVerdict.TRUSTED)
        elif run.state == RunState.RERUN_SUPERSEDED:
            return WorkflowTrustVerdict(verdict=TrustVerdict.DEGRADED)
        elif run.state in [RunState.FAILED, RunState.BLOCKED]:
            return WorkflowTrustVerdict(verdict=TrustVerdict.BLOCKED)
        return WorkflowTrustVerdict(verdict=TrustVerdict.REVIEW_REQUIRED)
