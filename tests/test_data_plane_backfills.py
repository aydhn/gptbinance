from datetime import datetime, timezone
import pytest
from app.data_plane.backfills import BackfillManager
from app.data_plane.models import BackfillRecord
from app.data_plane.exceptions import BackfillViolation


def test_backfill_manager():
    manager = BackfillManager()

    with pytest.raises(BackfillViolation):
        manager.record_backfill(
            BackfillRecord(
                backfill_id="bf_1",
                start_time=datetime(2023, 1, 2, tzinfo=timezone.utc),
                end_time=datetime(2023, 1, 1, tzinfo=timezone.utc),
                source_id="src_1",
            )
        )

    manager.record_backfill(
        BackfillRecord(
            backfill_id="bf_2",
            start_time=datetime(2023, 1, 1, tzinfo=timezone.utc),
            end_time=datetime(2023, 1, 2, tzinfo=timezone.utc),
            source_id="src_1",
        )
    )
    assert len(manager.list_backfills()) == 1
