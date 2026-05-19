from app.learning_plane.models import FindingRecord
from app.learning_plane.storage import storage

def create_finding(finding: FindingRecord):
    storage.save_finding(finding)
