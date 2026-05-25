from .exceptions import InvalidComplaintError

class ComplaintManager:
    def process(self, dispute, complaint):
        if not complaint.is_admitted and dispute.disposition_posture:
            raise InvalidComplaintError("no complaint==admitted dispute shortcut")
