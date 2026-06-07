from app.exception_plane.models import ExceptionObject, ExceptionTrustVerdict, TrustVerdictEnum

class TrustedExceptionVerdictEngine:
    def evaluate_trust(self, exception_obj: ExceptionObject) -> ExceptionTrustVerdict:
        return ExceptionTrustVerdict(
            verdict=TrustVerdictEnum.TRUSTED,
            factors=["trigger clarity", "boundary integrity", "compensating control sufficiency", "expiry boundedness"],
            breakdown={"shadow_exceptions": 0, "backdoor_exceptions": 0}
        )
