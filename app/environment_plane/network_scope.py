from app.environment_plane.models import NetworkScopeRecord

def define_network_scope(scope_description: str, mismatch_cautions: str) -> NetworkScopeRecord:
    return NetworkScopeRecord(scope_description=scope_description, mismatch_cautions=mismatch_cautions)
