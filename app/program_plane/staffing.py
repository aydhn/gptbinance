from app.program_plane.models import StaffingRealityRecord

class StaffingManager:
    def evaluate(self, program_id: str) -> StaffingRealityRecord:
        return StaffingRealityRecord(
            staffing_id=f"stf_{program_id}",
            program_id=program_id,
            nominal_staffing=5,
            effective_staffing=4,
            owner_gap=False,
            reviewer_bottleneck=False,
            staffing_drift=True
        )
