from app.waterfall_plane.models import RankRecord
from app.waterfall_plane.enums import RankClass

def register_rank(rank_id: str, rank_class: RankClass, seniority_level: int) -> RankRecord:
    return RankRecord(rank_id=rank_id, rank_class=rank_class, seniority_level=seniority_level)
