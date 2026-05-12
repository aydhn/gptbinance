class ControlReceipt:
    def __init__(self, action_id: str, session_id: str, trace_lineage: str = None):
        self.action_id = action_id
        self.session_id = session_id
        self.trace_lineage = trace_lineage
