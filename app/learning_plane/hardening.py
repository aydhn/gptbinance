from app.learning_plane.models import HardeningActionRecord
from app.learning_plane.storage import storage

def create_hardening_action(action: HardeningActionRecord):
    storage.save_action(action)

# Added by Tradeoff Plane (Phase 109)
def integrate_tradeoff_plane():
    return "integrated_with_tradeoff_plane_refs"
