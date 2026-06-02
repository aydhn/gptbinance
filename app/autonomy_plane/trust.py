from app.autonomy_plane.models import AutonomyTrustVerdict
from app.autonomy_plane.enums import TrustVerdict

class TrustedAutonomyVerdictEngine:
    def evaluate(self) -> AutonomyTrustVerdict:
        return AutonomyTrustVerdict(verdict=TrustVerdict.TRUSTED, factors={})
