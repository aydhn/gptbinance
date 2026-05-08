from app.data_plane.sources import CanonicalSourceRegistry
from app.data_plane.models import DataSourceDefinition
from app.data_plane.enums import SourceClass


def test_source_registry():
    registry = CanonicalSourceRegistry()
    defn = DataSourceDefinition(
        source_id="test_source",
        source_class=SourceClass.EXCHANGE_KLINES,
        is_mainnet=True,
        expected_cadence_ms=1000,
    )
    registry.register(defn)

    retrieved = registry.get("test_source")
    assert retrieved is not None
    assert retrieved.source_id == "test_source"
