from app.waterfall_plane.models import WaterfallObject

def create_waterfall_object(waterfall_id: str, waterfall_class, owner: str, scope: str, ranking_posture: str, distribution_posture: str) -> WaterfallObject:
    return WaterfallObject(
        waterfall_id=waterfall_id,
        waterfall_class=waterfall_class,
        owner=owner,
        scope=scope,
        ranking_posture=ranking_posture,
        distribution_posture=distribution_posture
    )
