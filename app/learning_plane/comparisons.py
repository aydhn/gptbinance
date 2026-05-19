from app.learning_plane.models import LearningComparisonRecord
from app.learning_plane.storage import storage

def create_comparison(comp: LearningComparisonRecord):
    storage.save_comparison(comp)
