from app.learning_plane.models import HardeningActionRecord
from app.learning_plane.storage import storage

def create_hardening_action(action: HardeningActionRecord):
    storage.save_action(action)
