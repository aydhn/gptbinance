from app.learning_plane.models import FailureClassRecord
from app.learning_plane.storage import storage

def create_failure_class(fc: FailureClassRecord):
    storage.save_failure_class(fc)
