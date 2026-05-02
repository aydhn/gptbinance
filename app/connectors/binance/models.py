from pydantic import BaseModel


class BinanceProfileConfig(BaseModel):
    api_key: str = ""
    api_secret: str = ""
    is_testnet: bool = True
    execution_capability: bool = False
    requires_live_arm: bool = True


class ExchangeInfoSnapshot:
    pass


class ServerTimeSnapshot:
    pass


class SymbolMetadata:
    pass


class SymbolFilter:
    pass


class RateLimit:
    pass


class ConnectorHealthResult:
    pass
