from app.waterfall_plane.models import WaterfallRecord
from datetime import datetime

def create_waterfall_record(waterfall_id: str, status: str) -> WaterfallRecord:
    return WaterfallRecord(
        waterfall_id=waterfall_id,
        status=status,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
