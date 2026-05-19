from app.learning_plane.models import RecurrenceRecord
from app.learning_plane.storage import storage

def create_recurrence(rec: RecurrenceRecord):
    storage.save_recurrence(rec)
