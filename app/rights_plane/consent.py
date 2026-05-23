from app.rights_plane.models import ConsentRecord, ConsentScopeRecord
from app.rights_plane.exceptions import InvalidConsentError

def evaluate_consent(consent: ConsentRecord, scope: ConsentScopeRecord):
    if scope.is_blanket:
        return "caution: blanket pseudo-consent detected, not a legitimate use-right basis"
    return "trusted"
