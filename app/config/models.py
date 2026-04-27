from pydantic import BaseModel, Field, SecretStr, validator
from typing import Optional
from app.core.enums import EnvironmentProfile, LogLevel


class GeneralConfig(BaseModel):
    profile: EnvironmentProfile = Field(default=EnvironmentProfile.DEV)
    app_name: str = "binance_trading_bot"


class LoggingConfig(BaseModel):
    level: LogLevel = Field(default=LogLevel.INFO)


class StorageConfig(BaseModel):
    use_sqlite: bool = True


class TelegramConfig(BaseModel):
    enabled: bool = False
    bot_token: Optional[SecretStr] = None
    chat_id: Optional[SecretStr] = None


class BinanceConfig(BaseModel):
    api_key: Optional[SecretStr] = None
    api_secret: Optional[SecretStr] = None
    use_testnet: bool = True


class ExecutionConfig(BaseModel):
    enabled: bool = False


class RiskConfig(BaseModel):
    hard_stops_enabled: bool = True
    max_drawdown_pct: float = Field(default=5.0, ge=0.1, le=20.0)


class LiveGuardConfig(BaseModel):
    # This must match a specific value to allow live trading
    live_confirmation: str = Field(default="")


class AppConfig(BaseModel):
    general: GeneralConfig = Field(default_factory=GeneralConfig)
    logging: LoggingConfig = Field(default_factory=LoggingConfig)
    storage: StorageConfig = Field(default_factory=StorageConfig)
    telegram: TelegramConfig = Field(default_factory=TelegramConfig)
    binance: BinanceConfig = Field(default_factory=BinanceConfig)
    execution: ExecutionConfig = Field(default_factory=ExecutionConfig)
    risk: RiskConfig = Field(default_factory=RiskConfig)
    live_guard: LiveGuardConfig = Field(default_factory=LiveGuardConfig)
