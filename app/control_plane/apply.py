import uuid
from typing import Dict
from app.control_plane.models import ActionRequest, ActionApplyRecord, ControlReceipt
from app.control_plane.exceptions import ControlPlaneError


class ApplyEngine:
    def __init__(self):
        self._records: Dict[str, ActionApplyRecord] = {}
        self._receipts: Dict[str, ControlReceipt] = {}

    def apply_action(
        self, request: ActionRequest, is_approved: bool = True
    ) -> ControlReceipt:
        if not is_approved:
            raise ControlPlaneError(f"Action {request.action_id} lacks approval")

        receipt_id = f"RPT-{uuid.uuid4().hex[:8]}"
        record = ActionApplyRecord(
            receipt_id=receipt_id, action_id=request.action_id, outcome="SUCCESS"
        )
        self._records[request.action_id] = record

        receipt = ControlReceipt(
            receipt_id=receipt_id,
            action_id=request.action_id,
            actor=request.actor,
            approvers=[],
            preview_hash="PREV-HASH-OK",
            apply_outcome=record.outcome,
        )
        self._receipts[receipt_id] = receipt
        return receipt

    def get_receipt(self, receipt_id: str) -> ControlReceipt:
        return self._receipts.get(receipt_id)
