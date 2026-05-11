from app.workflow_plane.models import RunReceipt, WorkflowRun
import uuid


class ReceiptManager:
    def issue_receipt(self, run: WorkflowRun, trigger_provenance: str) -> RunReceipt:
        return RunReceipt(
            receipt_id=f"rec-{uuid.uuid4().hex[:8]}",
            run_id=run.run_id,
            trigger_provenance=trigger_provenance,
            completion_summary=(
                f"Run {run.run_id} completed successfully"
                if run.state == "completed"
                else f"Run stopped at {run.state}"
            ),
            gate_outcomes=run.gate_results,
        )
