from app.security.storage import SecurityStorage
from app.security.evidence import EvidenceChain


class SecurityRepository:
    def __init__(self):
        self.storage = SecurityStorage()
        self.evidence = EvidenceChain()

    def log_audit(self, event: str, payload: dict):
        self.evidence.append_event(event, payload)
