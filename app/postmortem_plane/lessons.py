from typing import List
from app.postmortem_plane.models import LearningNote

class LessonsLearned:
    @staticmethod
    def capture(note_id: str, category: str, desc: str, transferability: str, lineages: List[str] = None) -> LearningNote:
        return LearningNote(
            note_id=note_id,
            category=category,
            description=desc,
            scope_transferability=transferability,
            lineage_refs=lineages or []
        )
