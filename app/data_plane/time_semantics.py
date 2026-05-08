from datetime import datetime
from .enums import TimeSemantic
from .exceptions import InvalidTimestampSemantics


class TimeSemanticValidator:
    @staticmethod
    def validate(event_time: datetime, available_at_time: datetime):
        if event_time > available_at_time:
            raise InvalidTimestampSemantics(
                "Event time cannot be after available_at_time"
            )
