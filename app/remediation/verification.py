from app.remediation.models import RemediationPack, VerificationResult
from app.remediation.enums import VerificationVerdict


class VerificationEngine:
    def verify(self, pack: RemediationPack) -> VerificationResult:
        # Mock verify: assumes finding resolved
        return VerificationResult(
            verdict=VerificationVerdict.FIXED,
            details="Drift finding successfully closed. Shadow state matches venue.",
        )
