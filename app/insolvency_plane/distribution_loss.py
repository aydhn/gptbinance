# distribution_loss.py
from typing import Dict, List, Optional
from app.insolvency_plane.models import DistributionLossRecord

class DistributionLossManager:
    def __init__(self):
        self.losses: Dict[str, DistributionLossRecord] = {}

    def register_loss(self, loss: DistributionLossRecord):
        self.losses[loss.loss_id] = loss

    def get_loss(self, loss_id: str) -> Optional[DistributionLossRecord]:
        return self.losses.get(loss_id)

    def list_losses(self) -> List[DistributionLossRecord]:
        return list(self.losses.values())
