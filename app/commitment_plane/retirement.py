from app.commitment_plane.models import RetirementRecord

class RetirementManager:
    @staticmethod
    def create_retirement(retirement_type: str, description: str, caveats: str = None) -> RetirementRecord:
        valid_types = ['retired', 'superseded', 'obsolete']
        if retirement_type not in valid_types:
            raise ValueError(f"Invalid retirement type. Must be one of {valid_types}")

        return RetirementRecord(
            retirement_type=retirement_type,
            description=description,
            caveats=caveats,
            lineage_refs=[]
        )
