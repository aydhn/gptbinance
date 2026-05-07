import json
import os
from app.config_plane.models import EffectiveConfigManifest

# Simplified file-based storage for testing/CLI
STORAGE_DIR = "/tmp/config_plane_storage"

def _ensure_dir():
    if not os.path.exists(STORAGE_DIR):
        os.makedirs(STORAGE_DIR)

def save_manifest(manifest: EffectiveConfigManifest):
    _ensure_dir()
    path = os.path.join(STORAGE_DIR, f"{manifest.manifest_id}.json")
    with open(path, "w") as f:
        f.write(manifest.model_dump_json(indent=2))

def load_manifest(manifest_id: str) -> EffectiveConfigManifest:
    path = os.path.join(STORAGE_DIR, f"{manifest_id}.json")
    if not os.path.exists(path):
        return None
    with open(path, "r") as f:
        return EffectiveConfigManifest.model_validate_json(f.read())
