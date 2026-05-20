from typing import List
from app.semantic_plane.models import AliasRecord
from app.semantic_plane.enums import AliasClass

class AliasManager:
    def __init__(self, registry):
        self.registry = registry

    def classify_alias(self, alias: AliasRecord) -> AliasClass:
        # Simplified logic for demonstrating classification
        if "legacy" in alias.caveats.lower():
            alias.alias_class = AliasClass.DANGEROUS
        return alias.alias_class

    def get_dangerous_aliases(self) -> List[AliasRecord]:
        dangerous = []
        for term in self.registry.terms.values():
            for alias in term.aliases:
                if alias.alias_class == AliasClass.DANGEROUS:
                    dangerous.append(alias)
        return dangerous
