from app.learning_plane.models import AdoptionRecord
from app.learning_plane.storage import storage

def create_adoption(adoption: AdoptionRecord):
    storage.save_adoption(adoption)
