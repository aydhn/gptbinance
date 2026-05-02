from app.release.storage import ReleaseStorage
from app.release.models import ReleaseBundle

class ReleaseRepository:
    def __init__(self, storage: ReleaseStorage):
        self.storage = storage

    def save_release(self, bundle: ReleaseBundle):
        self.storage.save_bundle(bundle)

    def get_release(self, version: str) -> ReleaseBundle:
        return self.storage.load_bundle(version)
