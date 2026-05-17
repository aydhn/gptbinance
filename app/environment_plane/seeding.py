from app.environment_plane.models import EnvironmentSeedRecord

def define_seed(seed_provenance: str, stale_warnings: str) -> EnvironmentSeedRecord:
    return EnvironmentSeedRecord(seed_provenance=seed_provenance, stale_warnings=stale_warnings)
