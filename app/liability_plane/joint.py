import uuid
from typing import List
from app.liability_plane.models import JointLiabilityRecord, ProofNote
from app.liability_plane.enums import JointLiabilityClass
from app.liability_plane.repository import LiabilityRepository

class JointLiabilityManager:
    def __init__(self, repository: LiabilityRepository):
        self.repository = repository

    def add_joint_liability(self, liability_id: str, joint_class: JointLiabilityClass, actors: List[str], notes: List[ProofNote]) -> JointLiabilityRecord:
        record = self.repository.get_liability_record(liability_id)
        if not record:
            raise ValueError(f"Liability {liability_id} not found.")

        joint_record = JointLiabilityRecord(
            record_id=str(uuid.uuid4()),
            liability_id=liability_id,
            joint_class=joint_class,
            actors=actors,
            proof_notes=notes
        )
        record.joint.append(joint_record)
        self.repository.storage.save(record)
        return joint_record
