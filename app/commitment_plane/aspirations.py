from app.commitment_plane.models import AspirationRecord

class AspirationManager:
    @staticmethod
    def create_aspiration(aspiration_type: str, description: str, caveats: str = "ASPIRATION IS NOT BINDING") -> AspirationRecord:
        if not description:
            raise ValueError("Aspiration description cannot be empty")
        return AspirationRecord(
            aspiration_type=aspiration_type,
            description=description,
            caveats=caveats,
            lineage_refs=[]
        )
