

def verify_remedy_exhaustion_rights(remedy_id: str, challenge_right_ref: str, rights_registry) -> str:
    """Ensures remedy exhaustion does not bury challenge rights."""
    if challenge_right_ref and rights_registry.is_right_active(challenge_right_ref):
        return "explicit caution: remedy exhausted label while beneficiary challenge survives"
    return "exhausted"

# OBLIGATION PLANE INTEGRATION
def check_remedy_exhaustion(remedy_exhausted: bool, open_execution_duty: bool) -> str:
    # remedy exhausted label under open execution duty explicit caution
    if remedy_exhausted and open_execution_duty:
        return "CAUTION: Remedy exhausted label applied despite open execution duty."
    return "Remedy exhaustion validated."
