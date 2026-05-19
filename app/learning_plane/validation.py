from app.learning_plane.models import ValidationRecord
from app.learning_plane.storage import storage

def create_validation(val: ValidationRecord):
    storage.save_validation(val)
