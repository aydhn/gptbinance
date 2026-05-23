class TemporalExpiry:
    def __init__(self):
        self.expired_delegation_refs = []
    def __init__(self):
        self.temporary_authority_windows_refs = []
    def __init__(self):
        self.mandate_expiries_refs = []
    def check_stale_precedent(self):
        pass

# Precedent Plane Integration added


def verify_consent_expiry(consent_id: str, rights_registry) -> str:
    if rights_registry.is_consent_expired(consent_id):
        return "explicit caution: expired consent still used as active basis"
    return "trusted"
