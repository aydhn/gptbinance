from .models import IncidentRecord, IncidentTimelineEvent


class TimelineManager:
    @staticmethod
    def add_event(incident: IncidentRecord, event_type: str, description: str):
        incident.timeline.append(
            IncidentTimelineEvent(event_type=event_type, description=description)
        )
