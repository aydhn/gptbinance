from typing import List
from app.security.models import RetentionPolicy
from app.security.enums import RetentionClass


class RetentionManager:
    def get_policies(self) -> List[RetentionPolicy]:
        return [
            RetentionPolicy(
                retention_class=RetentionClass.HOT, max_age_days=7, action="Keep"
            ),
            RetentionPolicy(
                retention_class=RetentionClass.WARM, max_age_days=30, action="Archive"
            ),
            RetentionPolicy(
                retention_class=RetentionClass.ARCHIVE, max_age_days=365, action="Prune"
            ),
            RetentionPolicy(
                retention_class=RetentionClass.DISPOSABLE,
                max_age_days=1,
                action="Delete",
            ),
        ]

    def get_summary(self) -> dict:
        return {"action_recommended": "Prune old logs"}
