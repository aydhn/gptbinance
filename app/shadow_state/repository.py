from app.shadow_state.storage import shadow_storage
from app.shadow_state.models import ShadowTwinSnapshot, ConvergenceRun


class ShadowRepository:
    def save_twin(self, twin: ShadowTwinSnapshot):
        shadow_storage.save_twin(twin)

    def save_run(self, run: ConvergenceRun):
        shadow_storage.save_run(run)


shadow_repository = ShadowRepository()
