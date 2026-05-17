from app.environment_plane.models import DataScopeRecord

def define_data_scope(scope_description: str, bleed_warnings: str) -> DataScopeRecord:
    return DataScopeRecord(scope_description=scope_description, bleed_warnings=bleed_warnings)
