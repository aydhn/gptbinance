from typing import Dict, List
from app.adversarial_plane.models import AdversarialObject
from app.adversarial_plane.enums import AdversarialClass

def create_authoritative_adversarial_object(
    adv_id: str,
    adv_class: AdversarialClass,
    name: str,
    owner: str,
    scope: str,
    actor_posture: str,
    exploit_posture: str
) -> AdversarialObject:
    if not name:
        raise ValueError("Adversarial object name cannot be vague or empty")
    return AdversarialObject(
        adversarial_id=adv_id,
        adversarial_class=adv_class,
        name=name,
        owner=owner,
        scope=scope,
        actor_posture=actor_posture,
        exploit_posture=exploit_posture
    )
