class WorkflowRun:
    def __init__(self, workflow_principal_id: str, trace_span_id: str = None):
        if not workflow_principal_id:
            raise ValueError("Shared anonymous workflow actor used")
        self.workflow_principal_id = workflow_principal_id
        self.trace_span_id = trace_span_id

    def add_security_lineage(self, security_principal: str, secret_usage_lineage_refs: list, boundary_refs: list):
        self.security_principal = security_principal
        self.secret_usage_lineage_refs = secret_usage_lineage_refs
        self.boundary_refs = boundary_refs
