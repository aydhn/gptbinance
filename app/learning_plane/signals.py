# Stub to satisfy imports, if any.
from app.learning_plane.models import LearningSignalRecord
from app.learning_plane.storage import storage

def create_signal(signal: LearningSignalRecord):
    storage.save_signal(signal)
