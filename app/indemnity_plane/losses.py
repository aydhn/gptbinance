from app.indemnity_plane.models import CoveredLossRecord
def record_loss(indemnity_id: str, loss_class: str) -> CoveredLossRecord:
    return CoveredLossRecord(indemnity_id=indemnity_id, loss_class=loss_class)
