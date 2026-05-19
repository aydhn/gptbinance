from app.learning_plane.models import UpdateTargetRecord
from app.learning_plane.storage import storage

def create_update_target(target: UpdateTargetRecord):
    storage.save_target(target)
