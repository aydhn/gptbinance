from app.postmortem_plane.models import RecurrenceRecord
from app.postmortem_plane.enums import RecurrenceClass, RecurrenceEscalationClass

class RecurrenceTracker:
    @staticmethod
    def track(rec_id: str, r_class: RecurrenceClass, family: str, interval: int, escalation: RecurrenceEscalationClass, notes: str) -> RecurrenceRecord:
        return RecurrenceRecord(
            recurrence_id=rec_id,
            recurrence_class=r_class,
            previous_incident_family=family,
            interval_days=interval,
            escalation_class=escalation,
            comparison_notes=notes
        )
