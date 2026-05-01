from app.security.models import RotationReadinessReport

class RotationReadiness:
    def get_report(self) -> RotationReadinessReport:
        return RotationReadinessReport(
            readiness_score=85,
            impacted_modules=["app.exchange.client"],
            recommendations=["Rotate BINANCE_API_KEY manually and restart via ops/recovery.py"]
        )
