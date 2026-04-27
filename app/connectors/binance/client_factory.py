import requests
import logging
from typing import Dict, Any, Optional
from app.config.models import AppConfig
from app.core.enums import EnvironmentProfile
from app.connectors.binance.profile_resolver import ProfileResolver
from app.connectors.binance.exceptions import (
    BinanceConnectivityError,
    BinanceAPIError,
    BinanceRateLimitError,
)

logger = logging.getLogger(__name__)


class BinancePublicClient:
    """
    A strictly public, read-only REST client for Binance.
    Does NOT support authentication, signing, or order execution.
    """

    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update(
            {"Accept": "application/json", "User-Agent": "BinanceTradingPlatform/0.1"}
        )

    def get(
        self, endpoint: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Executes a GET request to a public Binance endpoint."""
        url = f"{self.base_url}{endpoint}"

        try:
            response = self.session.get(url, params=params, timeout=10)

            # Handle rate limiting
            if response.status_code == 429:
                raise BinanceRateLimitError("Rate limit exceeded", status_code=429)
            elif response.status_code == 418:
                raise BinanceRateLimitError(
                    "IP auto-banned for repeated rate limit violations", status_code=418
                )

            # Handle other HTTP errors
            response.raise_for_status()

            data = response.json()

            # Handle Binance specific API errors if present in a 200 OK response (rare but possible)
            if isinstance(data, dict) and "code" in data and data["code"] < 0:
                raise BinanceAPIError(
                    data.get("msg", "Unknown API error"), error_code=data["code"]
                )

            return data

        except requests.exceptions.Timeout as e:
            raise BinanceConnectivityError(f"Request timeout to {url}: {e}")
        except requests.exceptions.ConnectionError as e:
            raise BinanceConnectivityError(f"Connection error to {url}: {e}")
        except requests.exceptions.HTTPError as e:
            # Try to extract Binance error msg
            err_msg = str(e)
            try:
                err_data = e.response.json()
                if "msg" in err_data:
                    err_msg = err_data["msg"]
            except Exception:
                pass
            raise BinanceAPIError(err_msg, status_code=e.response.status_code)
        except requests.exceptions.RequestException as e:
            raise BinanceConnectivityError(f"Request failed: {e}")


class ClientFactory:
    """
    Factory for creating Binance API clients based on configuration and profile.
    Currently only yields read-only public clients.
    """

    @staticmethod
    def create_public_client(
        config: AppConfig, profile: EnvironmentProfile
    ) -> BinancePublicClient:
        """
        Creates a public, read-only client.
        Keys are intentionally ignored here to enforce the read-only constraint.
        """
        capabilities = ProfileResolver.resolve_capabilities(profile)

        if not capabilities.can_read_public_market_data:
            logger.warning(
                f"Profile {profile} does not typically read public market data, but creating client anyway."
            )

        base_url = ProfileResolver.get_base_url(profile, config.binance.use_testnet)
        logger.debug(
            f"Creating BinancePublicClient for profile {profile} with base URL: {base_url}"
        )

        return BinancePublicClient(base_url)
