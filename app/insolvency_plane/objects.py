# objects.py
from typing import Dict, Any
from app.insolvency_plane.models import InsolvencyObject
from app.insolvency_plane.enums import InsolvencyClass

def create_insolvency_object(id: str, class_type: InsolvencyClass, owner: str, scope: str, metadata: Dict[str, Any] = None) -> InsolvencyObject:
    if metadata is None:
        metadata = {}
    return InsolvencyObject(
        id=id,
        class_type=class_type,
        owner=owner,
        scope=scope,
        metadata=metadata
    )
