from .models import IncidentScope, IncidentScopeType


class ScopeResolver:
    @staticmethod
    def resolve_blast_radius(scope_type: IncidentScopeType, ref: str) -> IncidentScope:
        return IncidentScope(
            type=scope_type,
            ref=ref,
            blast_radius_summary=f"Affects {scope_type.value} level: {ref}",
        )
