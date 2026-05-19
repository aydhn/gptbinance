from app.learning_plane.models import CausalHypothesisRecord
from app.learning_plane.storage import storage

def create_hypothesis(hyp: CausalHypothesisRecord):
    storage.save_hypothesis(hyp)
