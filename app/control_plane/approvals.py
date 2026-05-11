class ControlApproval:
    def __init__(self, approval_id: str, approver_session_id: str):
        self.approval_id = approval_id
        self.approver_session_id = approver_session_id

    def verify(self, authz_engine, environment: str) -> bool:
        result = authz_engine.evaluate(self.approver_session_id, "control_plane_approve", environment)
        return result.is_allowed
