from .models import JurisdictionTrustVerdict

class TrustedJurisdictionVerdictEngine:
    def evaluate(self) -> JurisdictionTrustVerdict:
        return JurisdictionTrustVerdict(verdict="trusted")
