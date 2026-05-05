from datetime import datetime, timezone
from typing import Dict, Any

from app.remediation.models import RemediationFindingRef


class FindingIntake:
    def normalize_finding(
        self,
        finding_id: str,
        source_domain: str,
        severity: str,
        context: Dict[str, Any],
        is_stale: bool = False,
    ) -> RemediationFindingRef:
        return RemediationFindingRef(
            finding_id=finding_id,
            source_domain=source_domain,
            severity=severity,
            detected_at=datetime.now(timezone.utc),
            is_stale=is_stale,
            context=context,
        )
