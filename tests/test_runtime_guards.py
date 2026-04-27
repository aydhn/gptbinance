import pytest
from app.config.models import AppConfig
from app.core.enums import EnvironmentProfile
from app.core.runtime_guards import check_live_guard, LiveModeError


def get_base_live_config():
    cfg = AppConfig()
    cfg.general.profile = EnvironmentProfile.LIVE
    cfg.execution.enabled = True
    cfg.binance.use_testnet = False
    cfg.risk.hard_stops_enabled = True
    cfg.live_guard.live_confirmation = "I_UNDERSTAND_THE_RISKS_AND_ALLOW_LIVE_TRADING"
    # Note: SecretStr requires actual init or monkeypatching, using workaround
    return cfg


def test_live_guard_passes_with_correct_setup(monkeypatch):
    monkeypatch.setenv("PROFILE", "live")
    monkeypatch.setenv("EXECUTION_ENABLED", "true")
    monkeypatch.setenv("BINANCE_USE_TESTNET", "false")
    monkeypatch.setenv("BINANCE_API_KEY", "key")
    monkeypatch.setenv("BINANCE_API_SECRET", "secret")
    monkeypatch.setenv(
        "LIVE_CONFIRMATION", "I_UNDERSTAND_THE_RISKS_AND_ALLOW_LIVE_TRADING"
    )

    from app.config.loader import load_config

    cfg = load_config()
    check_live_guard(cfg)  # Should not raise


def test_live_guard_fails_wrong_confirmation(monkeypatch):
    monkeypatch.setenv("PROFILE", "live")
    monkeypatch.setenv("LIVE_CONFIRMATION", "wrong")
    from app.config.loader import load_config

    cfg = load_config()

    with pytest.raises(LiveModeError, match="confirmation does not match"):
        check_live_guard(cfg)


def test_live_guard_fails_no_secrets(monkeypatch):
    monkeypatch.setenv("PROFILE", "live")
    monkeypatch.setenv(
        "LIVE_CONFIRMATION", "I_UNDERSTAND_THE_RISKS_AND_ALLOW_LIVE_TRADING"
    )
    monkeypatch.setenv("EXECUTION_ENABLED", "true")
    monkeypatch.setenv("BINANCE_USE_TESTNET", "false")
    monkeypatch.delenv("BINANCE_API_KEY", raising=False)

    from app.config.loader import load_config

    cfg = load_config()
    with pytest.raises(LiveModeError, match="Missing Binance API credentials"):
        check_live_guard(cfg)


def test_live_guard_ignores_non_live(monkeypatch):
    monkeypatch.setenv("PROFILE", "dev")
    from app.config.loader import load_config

    cfg = load_config()
    check_live_guard(cfg)  # Should not raise
