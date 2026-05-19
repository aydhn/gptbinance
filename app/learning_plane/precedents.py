from app.learning_plane.models import PrecedentLearningRecord
from app.learning_plane.storage import storage

def create_precedent(prec: PrecedentLearningRecord):
    storage.save_precedent(prec)
