from app.constitution_plane.models import WaiverRecord

class WaiverManager:
    def check_waiver_freshness(self, waiver: WaiverRecord) -> bool:
        return not waiver.is_stale
