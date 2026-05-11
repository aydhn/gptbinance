class WorkflowRun:
    def __init__(self, workflow_principal_id: str):
        if not workflow_principal_id:
            raise ValueError("Shared anonymous workflow actor used")
        self.workflow_principal_id = workflow_principal_id
