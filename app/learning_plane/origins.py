from app.learning_plane.models import LearningOriginRecord
from app.learning_plane.storage import storage

def create_origin(origin: LearningOriginRecord):
    storage.save_origin(origin)
