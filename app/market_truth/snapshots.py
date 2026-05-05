from typing import Dict, Any


class SnapshotCapture:
    def capture(self, adapter: Any) -> Dict[str, Any]:
        """
        Captures a snapshot using the provided SourceAdapter.
        Records lineage and capture time implicitly via external context wrapper.
        """
        return adapter.fetch_snapshot()
