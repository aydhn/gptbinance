from app.qualification.models import QualificationRun
from app.qualification.storage import QualificationStorage


class QualificationRepository:
    def __init__(self):
        self.storage = QualificationStorage()

    def save_run(self, run: QualificationRun):
        self.storage.save_run(run)

    def get_run(self, run_id: str) -> QualificationRun:
        return self.storage.get_run(run_id)
