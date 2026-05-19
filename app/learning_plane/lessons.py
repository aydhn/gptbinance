from app.learning_plane.models import LessonRecord
from app.learning_plane.storage import storage

def create_lesson(lesson: LessonRecord):
    storage.save_lesson(lesson)
