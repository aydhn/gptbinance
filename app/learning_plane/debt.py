from app.learning_plane.models import LearningDebtRecord
from app.learning_plane.storage import storage

def create_debt(debt: LearningDebtRecord):
    storage.save_debt(debt)
