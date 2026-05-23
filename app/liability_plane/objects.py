from app.liability_plane.models import LiabilityObject

# This will just serve as a helper module or extension point for object builders.
def build_liability_object(liability_id: str, liability_class, owner: str, scope: str, causation_posture: str, exposure_posture: str) -> LiabilityObject:
    return LiabilityObject(
        liability_id=liability_id,
        liability_class=liability_class,
        owner=owner,
        scope=scope,
        causation_posture=causation_posture,
        exposure_posture=exposure_posture
    )
