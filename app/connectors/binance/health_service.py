import logging
from typing import Optional
from app.config.models import AppConfig
from app.connectors.binance.client_factory import ClientFactory, BinancePublicClient
from app.connectors.binance.time_service import TimeService
from app.connectors.binance.exchange_info_service import ExchangeInfoService
from app.connectors.binance.models import ConnectorHealthResult
from app.core.enums import EnvironmentProfile

logger = logging.getLogger(__name__)


class HealthService:
    """
    Performs aggregated health and connectivity checks against the Binance connector.
    """

    def __init__(self, config: AppConfig, profile: EnvironmentProfile):
        self.config = config
        self.profile = profile
        self.client: Optional[BinancePublicClient] = None

    def check_health(self) -> ConnectorHealthResult:
        """
        Executes a sequence of checks to determine overall connector health.
        """
        result = ConnectorHealthResult(is_healthy=False)

        # 1. Config Check
        if not self.config or not self.profile:
            result.errors.append("Configuration or profile is missing.")
            result.overall_status = "FAILED"
            return result
        result.config_ready = True

        # 2. Client Creation
        try:
            self.client = ClientFactory.create_public_client(self.config, self.profile)
            result.client_created = True
        except Exception as e:
            result.errors.append(f"Failed to create client: {e}")
            result.overall_status = "FAILED"
            return result

        # 3. Server Time Check
        time_service = TimeService(self.client)
        try:
            time_snapshot = time_service.get_server_time()
            result.server_time_ok = True

            # Evaluate Latency
            latency = time_snapshot.latency_ms
            if latency < 500:
                result.latency_status = "GOOD"
            elif latency < 2000:
                result.latency_status = "ACCEPTABLE"
            else:
                result.latency_status = "POOR"
                result.errors.append(f"High latency detected: {latency}ms")

        except Exception as e:
            result.errors.append(f"Server time check failed: {e}")
            result.overall_status = "DEGRADED"

        # 4. Exchange Info Check
        exchange_service = ExchangeInfoService(self.client)
        try:
            exchange_info = exchange_service.get_exchange_info()
            if len(exchange_info.symbols) > 0:
                result.exchange_info_ok = True
            else:
                result.errors.append("Exchange info returned 0 symbols.")
        except Exception as e:
            result.errors.append(f"Exchange info check failed: {e}")
            result.overall_status = "DEGRADED"

        # Overall Status Logic
        if (
            result.config_ready
            and result.client_created
            and result.server_time_ok
            and result.exchange_info_ok
        ):
            if result.latency_status == "POOR":
                result.is_healthy = True  # Technically working, but poor
                result.overall_status = "DEGRADED"
            else:
                result.is_healthy = True
                result.overall_status = "HEALTHY"
        elif result.overall_status == "UNKNOWN":
            result.overall_status = "FAILED"

        return result
