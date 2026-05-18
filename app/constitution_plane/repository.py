from app.constitution_plane.storage import ConstitutionStorage

class ConstitutionRepository:
    def __init__(self, storage: ConstitutionStorage):
        self.storage = storage

    def get_latest_trusted_verdict(self, object_id: str):
        return self.storage.get_final_verdict(object_id)
