import pytest
from app.postmortem_plane.lessons import LessonsLearned

def test_lessons_learned():
    lesson = LessonsLearned.capture("L-1", "Process", "Always verify DB locks in staging", "GLOBAL")
    assert lesson.note_id == "L-1"
