import json
import re
from typing import Any, Dict


class Redactor:
    SENSITIVE_KEYS = ["API_KEY", "SECRET", "PASSWORD", "TOKEN", "PRIVATE_KEY"]

    @classmethod
    def redact_dict(cls, data: Dict[str, Any]) -> Dict[str, Any]:
        redacted = {}
        for k, v in data.items():
            if any(s in k.upper() for s in cls.SENSITIVE_KEYS):
                redacted[k] = "***REDACTED***"
            elif isinstance(v, dict):
                redacted[k] = cls.redact_dict(v)
            else:
                redacted[k] = v
        return redacted

    @classmethod
    def redact_string(cls, text: str) -> str:
        # Basic regex based redaction for tokens if needed
        return text
