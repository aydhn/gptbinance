from typing import List
from app.finality_plane.models import FinalityObject
from app.finality_plane.storage import storage
from app.finality_plane.enums import FinalityClass
import uuid
from datetime import datetime

class FinalityRegistry:
    @staticmethod
    def register_finality(owner: str, scope: str, finality_class: FinalityClass, closure_posture: str, reopen_posture: str) -> FinalityObject:
        fid = f"fin-{uuid.uuid4().hex[:8]}"
        obj = FinalityObject(
            finality_id=fid,
            finality_class=finality_class,
            owner=owner,
            scope=scope,
            closure_posture=closure_posture,
            reopen_posture=reopen_posture
        )
        storage.save_object(obj)
        return obj

    @staticmethod
    def list_objects() -> List[FinalityObject]:
        return list(storage.objects.values())
