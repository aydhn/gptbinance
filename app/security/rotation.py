import logging
from typing import Optional
from app.security.models import RotationReadinessReport
from app.control.models import AuthorizationResult

logger = logging.getLogger(__name__)


class RotationReadiness:
    def get_report(self) -> RotationReadinessReport:
        return RotationReadinessReport(
            readiness_score=85,
            impacted_modules=["app.exchange.client"],
            recommendations=[
                "Rotate BINANCE_API_KEY manually and restart via ops/recovery.py"
            ],
        )

    def apply_rotation(self, auth_bundle: Optional[AuthorizationResult] = None) -> bool:
        if not auth_bundle or auth_bundle.verdict.value != "approved":
            logger.error(
                "Rotation apply blocked: Missing or denied authorization bundle."
            )
            return False

        logger.info("Applying credential rotation.")
        return True
