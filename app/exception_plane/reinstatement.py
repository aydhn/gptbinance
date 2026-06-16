
import logging

logger = logging.getLogger(__name__)

def check_escrow_posture(action_name: str, has_explicit_escrow_posture: bool = False):
    if not has_explicit_escrow_posture:
        logger.warning(f"WARNING: Treated exception as escrow-clean without explicit escrow posture caution. Escrow plane integration required.")
        return False
    return True
