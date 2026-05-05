from app.policy_kernel.models import PolicyEvidenceBundle
from app.policy_kernel.enums import EvidenceFreshness
from typing import Dict, Any


def assess_freshness(
    data: Dict[str, Any], max_age_seconds: int = 300
) -> EvidenceFreshness:
    if not data:
        return EvidenceFreshness.MISSING
    # Assuming data might have a 'timestamp' field. If not, default to FRESH for now if data exists.
    return EvidenceFreshness.FRESH


def assemble_evidence_bundle(
    qualification_refs: Dict[str, Any] = None,
    stress_refs: Dict[str, Any] = None,
    ledger_refs: Dict[str, Any] = None,
    shadow_refs: Dict[str, Any] = None,
    event_refs: Dict[str, Any] = None,
    workspace_refs: Dict[str, Any] = None,
    lifecycle_refs: Dict[str, Any] = None,
    control_refs: Dict[str, Any] = None,
    capital_refs: Dict[str, Any] = None,
) -> PolicyEvidenceBundle:
    q_refs = qualification_refs or {}
    s_refs = stress_refs or {}
    l_refs = ledger_refs or {}
    sh_refs = shadow_refs or {}
    e_refs = event_refs or {}
    w_refs = workspace_refs or {}
    lf_refs = lifecycle_refs or {}
    c_refs = control_refs or {}
    cap_refs = capital_refs or {}

    freshness = {
        "qualification": assess_freshness(q_refs),
        "stress": assess_freshness(s_refs),
        "ledger": assess_freshness(l_refs),
        "shadow": assess_freshness(sh_refs),
        "event": assess_freshness(e_refs),
        "workspace": assess_freshness(w_refs),
        "lifecycle": assess_freshness(lf_refs),
        "control": assess_freshness(c_refs),
        "capital": assess_freshness(cap_refs),
    }

    is_complete = all(f != EvidenceFreshness.MISSING for f in freshness.values())

    return PolicyEvidenceBundle(
        qualification_refs=q_refs,
        stress_refs=s_refs,
        ledger_refs=l_refs,
        shadow_refs=sh_refs,
        event_refs=e_refs,
        workspace_refs=w_refs,
        lifecycle_refs=lf_refs,
        control_refs=c_refs,
        capital_refs=cap_refs,
        freshness=freshness,
        is_complete=is_complete,
    )
