from app.order_lifecycle.enums import DedupVerdict


class DedupEngine:
    def check_event(self, event_id: str) -> DedupVerdict:
        return DedupVerdict.NEW_EVENT
