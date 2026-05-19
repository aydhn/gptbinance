from app.learning_plane.models import OutcomeRecord
from app.learning_plane.storage import storage

def create_outcome(outcome: OutcomeRecord):
    storage.save_outcome(outcome)
