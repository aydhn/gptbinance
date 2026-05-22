from app.commitment_plane.models import CommitmentObject
from app.commitment_plane.enums import CommitmentClass

def is_authoritative(commitment: CommitmentObject) -> bool:
    # Logic to determine if authoritative based on class and binding
    return commitment.commitment_class in [CommitmentClass.PROMISE, CommitmentClass.OBLIGATION, CommitmentClass.GUARANTEE]

def is_decision_critical(commitment: CommitmentObject) -> bool:
    # Logic for decision critical
    return is_authoritative(commitment) and len(commitment.deadlines) > 0
