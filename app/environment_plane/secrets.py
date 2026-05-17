from app.environment_plane.models import SecretScopeRecord

def define_secret_scope(scope_description: str, proof_notes: str) -> SecretScopeRecord:
    return SecretScopeRecord(scope_description=scope_description, proof_notes=proof_notes)
