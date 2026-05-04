from datetime import datetime, timezone, timedelta
import uuid
from typing import Dict, List, Optional
from app.capital.models import CapitalEvidenceBundle
from app.capital.enums import EvidenceFreshness


def build_evidence_bundle(
    refs: Dict[str, str], timestamps: Dict[str, datetime], stale_timeout_mins: int = 60
) -> CapitalEvidenceBundle:
    """
    Constructs an evidence bundle checking freshness.
    refs: e.g. {"qualification_pass": "qual_123", "ledger_clean": "recon_456"}
    timestamps: dict of evidence type to its creation time
    """
    missing = []
    stale = []
    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(minutes=stale_timeout_mins)

    freshness = EvidenceFreshness.FRESH

    for key, ts in timestamps.items():
        if ts < cutoff:
            stale.append(key)
            freshness = EvidenceFreshness.STALE

    if stale:
        # Just flag it, the escalation policy will decide if it's blocking
        pass

    return CapitalEvidenceBundle(
        bundle_id=f"ev_{uuid.uuid4().hex[:8]}",
        timestamp=now,
        evidence_refs=refs,
        freshness=freshness,
        missing_items=missing,
    )


def check_required_evidence(
    bundle: CapitalEvidenceBundle, required_types: List[str]
) -> List[str]:
    """Returns a list of missing evidence types."""
    missing = []
    for req in required_types:
        if req not in bundle.evidence_refs:
            missing.append(req)
    return missing
