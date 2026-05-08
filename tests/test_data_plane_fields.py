from app.data_plane.fields import CanonicalFieldRegistry
from app.data_plane.models import DataFieldDefinition
from app.data_plane.enums import FieldClass


def test_field_registry():
    registry = CanonicalFieldRegistry()
    defn = DataFieldDefinition(
        field_name="close_price",
        field_class=FieldClass.NUMERIC,
        nullable=False,
        unit="USD",
    )
    registry.register(defn)

    retrieved = registry.get("close_price")
    assert retrieved is not None
    assert retrieved.field_name == "close_price"
