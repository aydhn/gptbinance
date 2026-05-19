from app.learning_plane.models import AvoidedFailureRecord
from app.learning_plane.storage import storage

def create_avoided_failure(af: AvoidedFailureRecord):
    storage.save_avoided_failure(af)
