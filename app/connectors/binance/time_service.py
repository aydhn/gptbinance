import time
import logging
from app.connectors.binance.client_factory import BinancePublicClient
from app.connectors.binance.models import ServerTimeSnapshot
from app.connectors.binance.exceptions import BinanceConnectivityError, BinanceAPIError

logger = logging.getLogger(__name__)


class TimeService:
    """
    Handles synchronization and drift measurement with Binance server time.
    """

    def __init__(self, client: BinancePublicClient):
        self.client = client

    def get_server_time(self) -> ServerTimeSnapshot:
        """
        Fetches the server time and calculates approximate latency and drift.
        Returns a normalized ServerTimeSnapshot.
        """
        try:
            start_time = int(time.time() * 1000)
            response = self.client.get("/api/v3/time")
            end_time = int(time.time() * 1000)

            if "serverTime" not in response:
                raise BinanceAPIError(
                    "Invalid response from /api/v3/time: missing serverTime"
                )

            server_time = int(response["serverTime"])

            # Approximate latency (round trip time)
            rtt = end_time - start_time

            # Approximate local time when the server processed the request
            # Assume symmetric network path (rtt/2)
            approx_local_time_at_server = start_time + (rtt // 2)

            # Drift: positive means local clock is ahead of server clock
            drift_ms = approx_local_time_at_server - server_time

            snapshot = ServerTimeSnapshot(
                server_time=server_time,
                local_time=end_time,
                latency_ms=rtt,
                drift_ms=drift_ms,
            )

            logger.debug(
                f"Time sync: server={server_time}, local={end_time}, rtt={rtt}ms, drift={drift_ms}ms"
            )
            return snapshot

        except (BinanceConnectivityError, BinanceAPIError) as e:
            logger.error(f"Failed to fetch server time: {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error fetching server time: {e}")
            raise BinanceConnectivityError(
                f"Failed to get server time due to unexpected error: {e}"
            )
