from typing import List
from .models import DataRevisionRecord
from .exceptions import InvalidRevisionRecord


class RevisionManager:
    def __init__(self):
        self._revisions: List[DataRevisionRecord] = []

    def record_revision(self, revision: DataRevisionRecord):
        if not revision.original_snapshot_id or not revision.new_snapshot_id:
            raise InvalidRevisionRecord("Snapshot IDs required")
        self._revisions.append(revision)

    def list_revisions(self) -> List[DataRevisionRecord]:
        return self._revisions
