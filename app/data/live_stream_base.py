import abc
from typing import List, Dict, Any, Callable, Awaitable

from app.data.live_stream_models import SubscriptionSpec, StreamHealthSnapshot

# Type hint for a callback function that handles streaming events
StreamCallback = Callable[[str, float, bool, int], Awaitable[None]]


class BaseLiveStreamManager(abc.ABC):
    """
    Abstract contract for any exchange-specific live stream manager.
    Ensures that the application interacts with a standard interface.
    """

    @abc.abstractmethod
    async def start(self) -> None:
        """Starts the internal connection and loops."""
        pass

    @abc.abstractmethod
    async def stop(self) -> None:
        """Stops the connection and cleans up tasks cleanly."""
        pass

    @abc.abstractmethod
    async def subscribe(self, specs: List[SubscriptionSpec]) -> None:
        """Adds new subscriptions to the active stream."""
        pass

    @abc.abstractmethod
    async def unsubscribe(self, specs: List[SubscriptionSpec]) -> None:
        """Removes subscriptions from the active stream."""
        pass

    @abc.abstractmethod
    def get_health(self) -> StreamHealthSnapshot:
        """Returns the current health and metrics of the stream."""
        pass

    @abc.abstractmethod
    def set_callback(self, callback: StreamCallback) -> None:
        """Registers a callback for processing stream events.
        Callback signature: async def handle_event(symbol: str, price: float, is_closed: bool, event_time_ms: int)
        """
        pass
