class WorkflowRun:
    def __init__(self, workflow_principal_id: str, trace_span_id: str = None):
        if not workflow_principal_id:
            raise ValueError("Shared anonymous workflow actor used")
        self.workflow_principal_id = workflow_principal_id
        self.trace_span_id = trace_span_id
