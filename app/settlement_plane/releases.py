from app.settlement_plane.models import ReleaseRecord, ReleaseClass
from app.settlement_plane.exceptions import InvalidReleaseError, OverreleaseViolationError

def evaluate_release(release: ReleaseRecord, expected_scope_refs: list[str]):
    if not release.scope:
        raise InvalidReleaseError("Release must define a scope")

    # Check for overrelease - releasing more than the settlement scope
    if release.release_class == ReleaseClass.FULL and release.inflation_caution:
        raise OverreleaseViolationError(f"Release {release.id} is flagged for inflation caution")

    # Valid release processing
    return {"status": "valid", "release_id": release.id, "class": release.release_class.value}
