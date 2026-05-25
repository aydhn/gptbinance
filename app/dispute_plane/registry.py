from .models import DisputeRecord
from .exceptions import InvalidDisputeObjectError

class CanonicalDisputeRegistry:
    def __init__(self):
        self._disputes = {}

    def register(self, dispute: DisputeRecord):
        if not dispute.dispute_id:
            raise InvalidDisputeObjectError("Dispute must have an ID")
        self._disputes[dispute.dispute_id] = dispute

    def get(self, dispute_id: str) -> DisputeRecord:
        return self._disputes.get(dispute_id)

    def all(self):
        return list(self._disputes.values())

dispute_registry = CanonicalDisputeRegistry()
