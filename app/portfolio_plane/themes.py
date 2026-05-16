from typing import Dict, Optional
from app.portfolio_plane.models import PortfolioTheme
from app.portfolio_plane.exceptions import PortfolioStorageError

class ThemeManager:
    def __init__(self):
        self._themes: Dict[str, PortfolioTheme] = {}

    def register(self, theme: PortfolioTheme):
        if theme.theme_id in self._themes:
            raise PortfolioStorageError(f"Theme {theme.theme_id} already exists")
        self._themes[theme.theme_id] = theme

    def get(self, theme_id: str) -> Optional[PortfolioTheme]:
        return self._themes.get(theme_id)

    def get_all(self) -> Dict[str, PortfolioTheme]:
        return self._themes.copy()
