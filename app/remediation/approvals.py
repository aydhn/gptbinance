import uuid
from app.remediation.models import RemediationPack


class ApprovalManager:
    def generate_request(self, pack: RemediationPack) -> str:
        request_id = f"APRV-{uuid.uuid4().hex[:8].upper()}"
        # In a real system, this would write to a control/governance database
        # For now, it just generates an ID
        return request_id

    def check_approval_status(self, request_id: str) -> str:
        # Mock status checker
        return "PENDING"
