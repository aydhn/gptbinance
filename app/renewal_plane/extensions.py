
from app.renewal_plane.models import ExtensionRecord

class ExtensionManager:
    def grant_extension(self, renewal_id: str, duration: int) -> ExtensionRecord:
        return ExtensionRecord(extension_id=f"ext_{renewal_id}", type="bounded")
