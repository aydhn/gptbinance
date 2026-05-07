from app.config_plane.storage import save_manifest, load_manifest

class ConfigRepository:
    def get_manifest(self, manifest_id: str):
        return load_manifest(manifest_id)

    def store_manifest(self, manifest):
        save_manifest(manifest)

repository = ConfigRepository()
