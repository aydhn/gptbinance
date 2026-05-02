import os
from typing import Dict, Optional
from app.security.models import SecretRef, SecretResolutionResult, SecretSource
from app.security.enums import SecretSourceType, SecretStatus


class SecretResolver:
    def resolve(self, ref: SecretRef) -> SecretResolutionResult:
        val = os.getenv(ref.key)
        if val:
            return SecretResolutionResult(
                ref=ref,
                source=SecretSource(type=SecretSourceType.ENV_VAR),
                status=SecretStatus.SAFE,
                value=val,
            )
        return SecretResolutionResult(
            ref=ref,
            source=SecretSource(type=SecretSourceType.MISSING),
            status=SecretStatus.MISSING,
            value=None,
        )
