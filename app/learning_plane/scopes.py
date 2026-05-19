from app.learning_plane.models import ScopeOfLessonRecord
from app.learning_plane.storage import storage

def create_scope(scope: ScopeOfLessonRecord):
    storage.save_scope(scope)
