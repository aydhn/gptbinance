import logging
from typing import Any, Callable, Dict, Set, Type
import asyncio
import inspect

logger = logging.getLogger(__name__)


# A simple EventBus for routing typed events to subscribers
class EventBus:
    def __init__(self):
        # Maps event type (class) to a set of handler functions
        self._subscribers: Dict[Type[Any], Set[Callable]] = {}

    def subscribe(self, event_type: Type[Any], handler: Callable) -> None:
        if event_type not in self._subscribers:
            self._subscribers[event_type] = set()
        self._subscribers[event_type].add(handler)
        logger.debug(f"Subscribed {handler.__name__} to {event_type.__name__}")

    def unsubscribe(self, event_type: Type[Any], handler: Callable) -> None:
        if event_type in self._subscribers:
            self._subscribers[event_type].discard(handler)
            logger.debug(f"Unsubscribed {handler.__name__} from {event_type.__name__}")

    async def publish(self, event: Any) -> None:
        event_type = type(event)
        if event_type in self._subscribers:
            for handler in list(self._subscribers[event_type]):
                try:
                    if inspect.iscoroutinefunction(handler):
                        await handler(event)
                    else:
                        handler(event)
                except Exception as e:
                    logger.error(
                        f"Error in handler {handler.__name__} for event {event_type.__name__}: {e}",
                        exc_info=True,
                    )
