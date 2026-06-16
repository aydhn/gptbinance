from app.waterfall_plane.models import DistributionActionRecord
from app.waterfall_plane.enums import DistributionClass

def register_distribution(action_id: str, dist_class: DistributionClass, amount: float) -> DistributionActionRecord:
    return DistributionActionRecord(action_id=action_id, distribution_class=dist_class, amount_distributed=amount)
