from app.core.logging import redact_secrets


def test_redact_secrets_json():
    raw_json = '{"api_key": "my_secret_key_123", "normal_key": "value"}'
    redacted = redact_secrets(raw_json)
    assert "my_secret_key_123" not in redacted
    assert "REDACTED" in redacted
    assert "normal_key" in redacted


def test_redact_secrets_regex_eq():
    raw_text = "Connecting with API_KEY=my_secret_key_123 and user=admin"
    redacted = redact_secrets(raw_text)
    assert "my_secret_key_123" not in redacted
    assert "REDACTED" in redacted
    assert "user=admin" in redacted


def test_redact_secrets_regex_json_like():
    raw_text = "Error detail: 'api_secret': 'super_secret'"
    redacted = redact_secrets(raw_text)
    assert "super_secret" not in redacted
    assert "REDACTED" in redacted
