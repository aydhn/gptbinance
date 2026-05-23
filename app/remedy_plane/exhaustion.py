

def verify_remedy_exhaustion_rights(remedy_id: str, challenge_right_ref: str, rights_registry) -> str:
    """Ensures remedy exhaustion does not bury challenge rights."""
    if challenge_right_ref and rights_registry.is_right_active(challenge_right_ref):
        return "explicit caution: remedy exhausted label while beneficiary challenge survives"
    return "exhausted"
