import logging
from typing import List, Set
from threading import Lock

from app.data.live_stream_models import SubscriptionSpec

logger = logging.getLogger(__name__)


class SubscriptionRegistry:
    """
    Manages active subscriptions to avoid duplicates and track current state.
    """

    def __init__(self):
        self._lock = Lock()
        # We store the unique stream names
        self._active_streams: Set[str] = set()

    def add_subscriptions(self, specs: List[SubscriptionSpec]) -> List[str]:
        """Adds new subscriptions and returns the list of newly added stream names."""
        new_streams = []
        with self._lock:
            for spec in specs:
                stream_name = spec.stream_name
                if stream_name not in self._active_streams:
                    self._active_streams.add(stream_name)
                    new_streams.append(stream_name)

        if new_streams:
            logger.info(
                f"Added {len(new_streams)} new subscriptions. Total: {len(self._active_streams)}"
            )
        return new_streams

    def remove_subscriptions(self, specs: List[SubscriptionSpec]) -> List[str]:
        """Removes subscriptions and returns the list of actually removed stream names."""
        removed_streams = []
        with self._lock:
            for spec in specs:
                stream_name = spec.stream_name
                if stream_name in self._active_streams:
                    self._active_streams.remove(stream_name)
                    removed_streams.append(stream_name)

        if removed_streams:
            logger.info(
                f"Removed {len(removed_streams)} subscriptions. Total: {len(self._active_streams)}"
            )
        return removed_streams

    def get_active_streams(self) -> List[str]:
        """Returns a list of all active stream names."""
        with self._lock:
            return list(self._active_streams)

    def has_subscriptions(self) -> bool:
        """Returns True if there are active subscriptions."""
        with self._lock:
            return len(self._active_streams) > 0
