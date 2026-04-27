from enum import Enum


class EnvironmentProfile(str, Enum):
    DEV = "dev"
    PAPER = "paper"
    TESTNET = "testnet"
    LIVE = "live"


class LogLevel(str, Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


class AppRunMode(str, Enum):
    NORMAL = "normal"
    CHECK_ONLY = "check-only"
    PRINT_EFFECTIVE_CONFIG = "print-effective-config"
    BOOTSTRAP_STORAGE = "bootstrap-storage"


class EventCategory(str, Enum):
    APP_LIFECYCLE = "app_lifecycle"
    CONFIG = "config"
    SECURITY = "security"
    EXECUTION = "execution"
    DATA_INGESTION = "data_ingestion"
    STRATEGY = "strategy"
    TELEGRAM = "telegram"
