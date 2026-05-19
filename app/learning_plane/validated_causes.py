from app.learning_plane.models import ValidatedCauseRecord
from app.learning_plane.storage import storage

def create_cause(cause: ValidatedCauseRecord):
    storage.save_cause(cause)
