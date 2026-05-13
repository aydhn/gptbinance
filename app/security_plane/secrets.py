from typing import Dict, List, Optional
from app.security_plane.models import SecretDefinition
from app.security_plane.exceptions import InvalidSecretDefinitionError

class SecretRegistry:
    def __init__(self):
        self._secrets: Dict[str, SecretDefinition] = {}

    def register_secret(self, secret: SecretDefinition) -> None:
        if not secret.secret_id or not secret.owner_id:
             raise InvalidSecretDefinitionError("Unmanaged secrets or ownerless secrets are not allowed")
        self._secrets[secret.secret_id] = secret

    def get_secret(self, secret_id: str) -> Optional[SecretDefinition]:
        return self._secrets.get(secret_id)

    def list_secrets(self) -> List[SecretDefinition]:
        return list(self._secrets.values())
