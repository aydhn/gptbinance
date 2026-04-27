import asyncio
import json
import logging
import time
from typing import Callable, Coroutine, Optional, Any

import websockets
from websockets.exceptions import ConnectionClosed

logger = logging.getLogger(__name__)


class BinanceWsClient:
    """
    Manages the raw websocket connection lifecycle, including reconnects.
    Does NOT parse or interpret messages (delegates to callback).
    """

    def __init__(
        self,
        base_url: str,
        on_message_cb: Callable[[str], Coroutine[Any, Any, None]],
        on_connect_cb: Optional[Callable[[], Coroutine[Any, Any, None]]] = None,
        on_disconnect_cb: Optional[Callable[[str], Coroutine[Any, Any, None]]] = None,
        max_reconnect_attempts: int = 50,
        initial_backoff: float = 1.0,
        max_backoff: float = 60.0,
    ):
        self.base_url = base_url
        self.on_message_cb = on_message_cb
        self.on_connect_cb = on_connect_cb
        self.on_disconnect_cb = on_disconnect_cb

        self.max_reconnect_attempts = max_reconnect_attempts
        self.initial_backoff = initial_backoff
        self.max_backoff = max_backoff

        self._ws: Optional[websockets.WebSocketClientProtocol] = None
        self._running = False
        self._task: Optional[asyncio.Task] = None

    async def start(self) -> None:
        if self._running:
            return
        self._running = True
        self._task = asyncio.create_task(self._run_loop())

    async def stop(self) -> None:
        self._running = False
        if self._ws:
            await self._ws.close()
        if self._task:
            await self._task

    async def send(self, payload: dict) -> None:
        if self._ws and self._ws.open:
            await self._ws.send(json.dumps(payload))
        else:
            logger.warning("Cannot send message, websocket is not open.")

    async def _run_loop(self) -> None:
        attempt = 0
        backoff = self.initial_backoff

        while self._running:
            try:
                logger.info(f"Connecting to websocket: {self.base_url}")
                async with websockets.connect(self.base_url) as ws:
                    self._ws = ws
                    attempt = 0  # Reset attempt on successful connect
                    backoff = self.initial_backoff

                    if self.on_connect_cb:
                        await self.on_connect_cb()

                    logger.info("Websocket connected successfully.")

                    # Receive loop
                    while self._running:
                        message = await ws.recv()
                        # Callback should be async
                        await self.on_message_cb(message)

            except ConnectionClosed as e:
                reason = f"Connection closed: code={e.code}, reason={e.reason}"
                logger.warning(reason)
                if self.on_disconnect_cb:
                    await self.on_disconnect_cb(reason)

            except Exception as e:
                reason = f"Websocket error: {e}"
                logger.error(reason, exc_info=True)
                if self.on_disconnect_cb:
                    await self.on_disconnect_cb(reason)

            finally:
                self._ws = None

            if not self._running:
                break

            # Reconnect logic
            attempt += 1
            if attempt > self.max_reconnect_attempts:
                logger.error(
                    f"Max reconnect attempts ({self.max_reconnect_attempts}) reached. Stopping."
                )
                self._running = False
                break

            logger.info(f"Reconnecting in {backoff} seconds (attempt {attempt})...")
            await asyncio.sleep(backoff)

            # Exponential backoff
            backoff = min(backoff * 2, self.max_backoff)
