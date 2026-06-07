from typing import Dict
from app.exception_plane.models import ExceptionObject
from app.exception_plane.base import ExceptionRegistryBase
from app.exception_plane.exceptions import InvalidExceptionObjectError

class CanonicalExceptionRegistry(ExceptionRegistryBase):
    def __init__(self):
        self._registry: Dict[str, ExceptionObject] = {}

    def register(self, obj: ExceptionObject):
        if not obj.exception_id:
            raise InvalidExceptionObjectError("Undocumented exception ids are prohibited.")
        self._registry[obj.exception_id] = obj

    def get(self, exception_id: str) -> ExceptionObject:
        return self._registry.get(exception_id)
