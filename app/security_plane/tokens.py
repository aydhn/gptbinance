from typing import Dict, List, Optional
from app.security_plane.models import TokenDefinition

class TokenManager:
    def __init__(self):
        self._tokens: Dict[str, TokenDefinition] = {}

    def register_token(self, token: TokenDefinition) -> None:
        self._tokens[token.token_id] = token

    def list_tokens(self) -> List[TokenDefinition]:
        return list(self._tokens.values())
