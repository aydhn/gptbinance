from typing import Dict, Optional
from app.portfolio_plane.models import WorkstreamRecord
from app.portfolio_plane.exceptions import PortfolioStorageError

class WorkstreamManager:
    def __init__(self):
        self._workstreams: Dict[str, WorkstreamRecord] = {}

    def register(self, workstream: WorkstreamRecord):
        if workstream.workstream_id in self._workstreams:
            raise PortfolioStorageError(f"Workstream {workstream.workstream_id} already exists")
        self._workstreams[workstream.workstream_id] = workstream

    def get(self, workstream_id: str) -> Optional[WorkstreamRecord]:
        return self._workstreams.get(workstream_id)

    def get_all(self) -> Dict[str, WorkstreamRecord]:
        return self._workstreams.copy()
