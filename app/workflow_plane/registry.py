from typing import Dict, List, Optional
from app.workflow_plane.models import WorkflowDefinition, JobContract, TriggerDefinition
from app.workflow_plane.enums import WorkflowClass, TriggerClass, JobClass

class CanonicalWorkflowRegistry:
    def __init__(self):
        self._workflows: Dict[str, WorkflowDefinition] = {}

    def register(self, workflow: WorkflowDefinition):
        self._workflows[workflow.workflow_id] = workflow

    def get_all(self) -> List[WorkflowDefinition]:
        return list(self._workflows.values())

    def get(self, workflow_id: str) -> Optional[WorkflowDefinition]:
        return self._workflows.get(workflow_id)

registry = CanonicalWorkflowRegistry()
registry.register(WorkflowDefinition(
    workflow_id="session_open_workflow",
    objective="Prepare system for trading session",
    workflow_class=WorkflowClass.PRODUCTION,
    jobs=[JobContract(job_id="verify_ledger", job_class=JobClass.RECONCILIATION, description="Verify balances", is_idempotent=True, mutability_class="read_only", recoverability_class="auto", required_trust_inputs=[])],
    triggers=[TriggerDefinition(trigger_class=TriggerClass.SCHEDULE, description="Daily at market open")],
    critical=True
))
registry.register(WorkflowDefinition(
    workflow_id="market_data_refresh_workflow",
    objective="Sync market truth from venues",
    workflow_class=WorkflowClass.PRODUCTION,
    jobs=[JobContract(job_id="fetch_klines", job_class=JobClass.DATA_REFRESH, description="Fetch Kline data", is_idempotent=True, mutability_class="append_only", recoverability_class="auto", required_trust_inputs=[])],
    triggers=[TriggerDefinition(trigger_class=TriggerClass.SCHEDULE, description="Every 1m")],
    critical=True
))
registry.register(WorkflowDefinition(
    workflow_id="allocation_cycle_workflow",
    objective="Generate allocations based on models",
    workflow_class=WorkflowClass.PRODUCTION,
    jobs=[JobContract(job_id="generate_intents", job_class=JobClass.ALLOCATION, description="Create allocation intents", is_idempotent=True, mutability_class="append_only", recoverability_class="auto", required_trust_inputs=[])],
    triggers=[TriggerDefinition(trigger_class=TriggerClass.DATA_ARRIVAL, description="Upon new model inference")],
    critical=True
))
