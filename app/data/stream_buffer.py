import logging
from collections import deque
from typing import Dict, List, Any, Type
from threading import Lock

logger = logging.getLogger(__name__)


class StreamBuffer:
    """
    Keeps a sliding window of recent events for inspection and debugging.
    """

    def __init__(self, max_len_per_type: int = 100):
        self._max_len = max_len_per_type
        self._lock = Lock()
        # Mapping type -> deque of events
        self._buffers: Dict[Type[Any], deque] = {}

    def add_event(self, event: Any) -> None:
        event_type = type(event)
        with self._lock:
            if event_type not in self._buffers:
                self._buffers[event_type] = deque(maxlen=self._max_len)
            self._buffers[event_type].append(event)

    def get_recent_events(self, event_type: Type[Any], limit: int = 10) -> List[Any]:
        with self._lock:
            if event_type not in self._buffers:
                return []
            q = self._buffers[event_type]
            # convert to list and return last `limit` items
            lst = list(q)
            return lst[-limit:]

    def get_snapshot(self) -> Dict[str, int]:
        """Returns a count of events currently buffered by type name."""
        with self._lock:
            return {t.__name__: len(q) for t, q in self._buffers.items()}
