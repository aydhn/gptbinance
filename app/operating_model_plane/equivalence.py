from app.operating_model_plane.models import OperatingModelObject
from app.operating_model_plane.enums import EquivalenceVerdict

def compare_equivalence(paper_obj: OperatingModelObject, live_obj: OperatingModelObject) -> EquivalenceVerdict:
    if paper_obj.primary_owner and live_obj.primary_owner:
        if paper_obj.primary_owner.owner_role.role_id != live_obj.primary_owner.owner_role.role_id:
            return EquivalenceVerdict.DIVERGED_ACCOUNTABILITY

    if paper_obj.backup_coverage != live_obj.backup_coverage:
        return EquivalenceVerdict.DIVERGED_COVERAGE

    return EquivalenceVerdict.EQUIVALENT
