from typing import List, Optional
from datetime import datetime, timezone
from app.knowledge.models import LessonLearned
from app.knowledge.catalog import catalog_registry
from app.knowledge.enums import KnowledgeItemType, LessonStatus


class LessonRegistry:
    def register(self, lesson: LessonLearned) -> None:
        catalog_registry.register(lesson)

    def get_lesson(self, item_id: str) -> Optional[LessonLearned]:
        item = catalog_registry.get(item_id)
        if item and item.item_type == KnowledgeItemType.LESSON_LEARNED:
            return item  # type: ignore
        return None

    def list_lessons(self) -> List[LessonLearned]:
        return [item for item in catalog_registry.list_by_type(KnowledgeItemType.LESSON_LEARNED)]  # type: ignore

    def transition_lesson(self, item_id: str, new_status: LessonStatus) -> bool:
        lesson = self.get_lesson(item_id)
        if lesson:
            if new_status == LessonStatus.ADOPTED and not (
                lesson.source_incident_ref or lesson.source_replay_ref
            ):
                # Must have evidence to adopt
                return False
            lesson.lesson_status = new_status
            lesson.last_reviewed_at = datetime.now(timezone.utc)
            return True
        return False


lesson_registry = LessonRegistry()
