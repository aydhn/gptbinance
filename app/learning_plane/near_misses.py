from app.learning_plane.models import NearMissRecord
from app.learning_plane.storage import storage

def create_near_miss(nm: NearMissRecord):
    storage.save_near_miss(nm)
