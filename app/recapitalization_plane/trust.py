from app.recapitalization_plane.models import RecapitalizationObject, RecapitalizationTrustVerdict
from app.recapitalization_plane.enums import TrustVerdict

def evaluate_trust(recap: RecapitalizationObject) -> RecapitalizationTrustVerdict:
    phantom_capital = any(f.status != "FUNDED" for f in recap.fundings) and recap.is_fully_effective
    hidden_dilution = any(d.status == "HIDDEN" for d in recap.dilutions)
    shadow_control = any(c.is_shadow_control for c in recap.controls)

    verdict = TrustVerdict.TRUSTED
    caveats = []

    if phantom_capital:
        verdict = TrustVerdict.BLOCKED
        caveats.append("Phantom Capital Detected: Effective marked without funding.")
    if hidden_dilution:
        verdict = TrustVerdict.BLOCKED
        caveats.append("Hidden Dilution Detected: Unfair class erosion without protection.")
    if shadow_control:
        verdict = TrustVerdict.CAUTION
        caveats.append("Shadow Control Transfer Detected.")

    return RecapitalizationTrustVerdict(
        recapitalization_id=recap.recapitalization_id,
        verdict=verdict,
        phantom_capital_detected=phantom_capital,
        hidden_dilution_detected=hidden_dilution,
        unauthorized_control_shift=shadow_control,
        caveats=caveats
    )
