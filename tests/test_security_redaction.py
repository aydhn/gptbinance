from app.security.redaction import Redactor

def test_redact_dict():
    data = {"API_KEY": "secret123", "normal": "val"}
    redacted = Redactor.redact_dict(data)
    assert redacted["API_KEY"] == "***REDACTED***"
    assert redacted["normal"] == "val"
