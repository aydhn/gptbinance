from app.data_plane.revisions import RevisionManager
from app.data_plane.models import DataRevisionRecord
from app.data_plane.enums import RevisionClass
import pytest


def test_revision_manager():
    manager = RevisionManager()
    record = DataRevisionRecord(
        revision_id="rev_1",
        revision_class=RevisionClass.RESTATEMENT,
        original_snapshot_id="snap_1",
        new_snapshot_id="snap_2",
        reason="Test reason",
    )
    manager.record_revision(record)
    assert len(manager.list_revisions()) == 1
    assert manager.list_revisions()[0].revision_id == "rev_1"
