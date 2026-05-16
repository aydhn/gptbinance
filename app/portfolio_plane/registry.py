from typing import Dict, Optional
from app.portfolio_plane.models import PortfolioObject
from app.portfolio_plane.exceptions import InvalidPortfolioObjectError

class CanonicalPortfolioRegistry:
    def __init__(self):
        self._objects: Dict[str, PortfolioObject] = {}

    def register(self, obj: PortfolioObject):
        if obj.portfolio_id in self._objects:
            raise InvalidPortfolioObjectError(f"Object {obj.portfolio_id} already registered.")
        if not obj.portfolio_id or not obj.theme_id or not obj.bucket_id:
            raise InvalidPortfolioObjectError("Portfolio object must have ID, theme ID, and bucket ID.")
        self._objects[obj.portfolio_id] = obj

    def get(self, portfolio_id: str) -> Optional[PortfolioObject]:
        return self._objects.get(portfolio_id)

    def get_all(self) -> Dict[str, PortfolioObject]:
        return self._objects.copy()

registry = CanonicalPortfolioRegistry()
