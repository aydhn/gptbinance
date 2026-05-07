from app.config_plane.schemas import registry
from app.config_plane.enums import ConfigDomain

def test_schema_registration():
    schema = registry.get_schema(ConfigDomain.STRATEGY)
    assert schema is not None
    assert "feature_flags.enable_ml" in schema.parameters
