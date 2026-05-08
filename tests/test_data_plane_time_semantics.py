import pytest
from datetime import datetime, timezone
from app.data_plane.time_semantics import TimeSemanticValidator
from app.data_plane.exceptions import InvalidTimestampSemantics


def test_time_semantics_validator():
    event_time = datetime(2023, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    available_at_time = datetime(2023, 1, 1, 11, 0, 0, tzinfo=timezone.utc)

    with pytest.raises(InvalidTimestampSemantics):
        TimeSemanticValidator.validate(event_time, available_at_time)
