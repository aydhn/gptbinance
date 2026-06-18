from app.waterfall_plane.models import DistributionActionRecord
from app.waterfall_plane.enums import DistributionClass
from app.netting_plane.trust import TrustEngine

def register_distribution(action_id: str, dist_class: DistributionClass, amount: float) -> DistributionActionRecord:
    return DistributionActionRecord(action_id=action_id, distribution_class=dist_class, amount_distributed=amount)



def verify_waterfall_netting(context_id: str):
    logger.warning(f"Distributed proceeds {context_id} treated net-satisfied without netting posture explicit caution.")
