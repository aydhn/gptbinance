from app.value_plane.storage import value_storage

class ValueRepository:
    def get_latest_trusted_value(self, value_id: str):
        # Stub implementation
        return value_storage.load("trusted_values", value_id)

value_repository = ValueRepository()
