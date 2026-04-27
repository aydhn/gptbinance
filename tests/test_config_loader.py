import os
import pytest
from app.config.loader import load_config, get_effective_config_dict
from app.core.enums import EnvironmentProfile

def test_load_default_config(monkeypatch):
    monkeypatch.delenv("PROFILE", raising=False)
    config = load_config()
    assert config.general.profile == EnvironmentProfile.DEV

def test_load_custom_config(monkeypatch):
    monkeypatch.setenv("PROFILE", "paper")
    monkeypatch.setenv("BINANCE_USE_TESTNET", "true")
    config = load_config()
    assert config.general.profile == EnvironmentProfile.PAPER
    assert config.binance.use_testnet is True

def test_effective_config_masks_secrets(monkeypatch):
    monkeypatch.setenv("BINANCE_API_KEY", "super_secret_key")
    config = load_config()
    eff_cfg = get_effective_config_dict(config, mask_secrets=True)

    # Due to our redact_secrets function, the serialized output will be replaced by ***REDACTED***
    assert eff_cfg["binance"]["api_key"] in ["**********", "***REDACTED***"]

def test_effective_config_masks_secrets_custom(monkeypatch):
    monkeypatch.setenv("BINANCE_API_KEY", "super_secret_key")
    config = load_config()

    # Force the dump json redaction logic to run over a normal string if it wasn't a SecretStr
    dump_json = config.model_dump_json()
    import app.core.logging as app_logging
    redacted = app_logging.redact_secrets('{"api_key": "super_secret_key"}')
    assert "super_secret_key" not in redacted
    assert "***REDACTED***" in redacted
