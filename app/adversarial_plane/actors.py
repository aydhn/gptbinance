from typing import List, Optional
from app.adversarial_plane.models import ActorRecord
from app.adversarial_plane.enums import ActorClass

def register_actor(actor_id: str, actor_class: ActorClass, posture_notes: str, lineage_refs: Optional[List[str]] = None) -> ActorRecord:
    if not actor_id:
        raise ValueError("Actor must have an ID")
    return ActorRecord(
        actor_id=actor_id,
        actor_class=actor_class,
        actor_posture_notes=posture_notes,
        lineage_refs=lineage_refs or []
    )

class ActorManager:
    def __init__(self):
        self._actors = {}

    def add_actor(self, actor: ActorRecord):
        self._actors[actor.actor_id] = actor

    def get_actor(self, actor_id: str) -> Optional[ActorRecord]:
        return self._actors.get(actor_id)

    def list_actors(self) -> List[ActorRecord]:
        return list(self._actors.values())
