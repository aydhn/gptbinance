import logging
import json
from app.config.models import AppConfig
from app.core.enums import EnvironmentProfile
from app.connectors.binance.health_service import HealthService
from app.connectors.binance.time_service import TimeService
from app.connectors.binance.exchange_info_service import ExchangeInfoService
from app.connectors.binance.client_factory import ClientFactory
from app.connectors.binance.universe_service import UniverseService

logger = logging.getLogger(__name__)


def check_binance_connectivity(config: AppConfig, profile: EnvironmentProfile):
    """
    Runs the health check sequence and prints the result.
    """
    logger.info(f"Running Binance connectivity check for profile: {profile.value}")
    health_service = HealthService(config, profile)
    result = health_service.check_health()

    print("\n--- Binance Connectivity Report ---")
    print(f"Overall Status: {result.overall_status}")
    print(f"Healthy: {result.is_healthy}")
    print(f"Config Ready: {result.config_ready}")
    print(f"Client Created: {result.client_created}")
    print(f"Server Time OK: {result.server_time_ok}")
    print(f"Exchange Info OK: {result.exchange_info_ok}")
    print(f"Latency Status: {result.latency_status}")

    if result.errors:
        print("\nErrors:")
        for err in result.errors:
            print(f" - {err}")
    print("-----------------------------------\n")


def check_time_sync(config: AppConfig, profile: EnvironmentProfile):
    """
    Fetches server time and prints drift information.
    """
    logger.info(f"Running Binance time sync check for profile: {profile.value}")
    try:
        client = ClientFactory.create_public_client(config, profile)
        time_service = TimeService(client)
        snapshot = time_service.get_server_time()

        print("\n--- Binance Time Sync Report ---")
        print(f"Local Time:  {snapshot.local_time}")
        print(f"Server Time: {snapshot.server_time}")
        print(f"Latency:     {snapshot.latency_ms} ms")
        print(f"Drift:       {snapshot.drift_ms} ms")
        print("--------------------------------\n")

    except Exception as e:
        logger.error(f"Time sync check failed: {e}")
        print(f"\n[ERROR] Time sync check failed: {e}\n")


def fetch_exchange_info(config: AppConfig, profile: EnvironmentProfile):
    """
    Fetches exchange info and prints a summary.
    """
    logger.info(f"Fetching Binance exchange info for profile: {profile.value}")
    try:
        client = ClientFactory.create_public_client(config, profile)
        exchange_service = ExchangeInfoService(client)
        info = exchange_service.get_exchange_info()

        print("\n--- Binance Exchange Info Summary ---")
        print(f"Server Time: {info.server_time}")
        print(f"Total Symbols: {len(info.symbols)}")
        print(f"Total Rate Limits: {len(info.rate_limits)}")

        # Print a few example symbols
        example_count = min(3, len(info.symbols))
        if example_count > 0:
            print("\nExamples:")
            for i in range(example_count):
                sym = info.symbols[i]
                print(
                    f" - {sym.symbol} (Status: {sym.status.value}, Tradable: {sym.is_tradable})"
                )
        print("-------------------------------------\n")

    except Exception as e:
        logger.error(f"Exchange info fetch failed: {e}")
        print(f"\n[ERROR] Exchange info fetch failed: {e}\n")


def print_symbol_universe(config: AppConfig, profile: EnvironmentProfile):
    """
    Fetches exchange info and prints the active USDT symbol universe.
    """
    logger.info(f"Printing symbol universe for profile: {profile.value}")
    try:
        client = ClientFactory.create_public_client(config, profile)
        exchange_service = ExchangeInfoService(client)
        info = exchange_service.get_exchange_info()

        active_usdt = UniverseService.get_active_usdt_pairs(info)

        print("\n--- Active USDT Symbol Universe ---")
        print(f"Total Active USDT Pairs: {len(active_usdt)}")

        # Only print up to 10 to avoid console spam
        display_limit = 10
        print(f"\nTop {display_limit} pairs:")
        for sym in active_usdt[:display_limit]:
            print(
                f" - {sym.symbol} (Base: {sym.base_asset}, Base Prec: {sym.base_asset_precision}, Quote Prec: {sym.quote_asset_precision})"
            )

        if len(active_usdt) > display_limit:
            print(f" ... and {len(active_usdt) - display_limit} more.")

        print("-----------------------------------\n")

    except Exception as e:
        logger.error(f"Symbol universe fetch failed: {e}")
        print(f"\n[ERROR] Symbol universe fetch failed: {e}\n")
