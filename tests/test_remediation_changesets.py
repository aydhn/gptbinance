from app.remediation.changesets import RemediationChangeSet
from app.remediation.compiler import RemediationCompiler
from app.remediation.findings import FindingIntake


def test_changeset_accumulation():
    compiler = RemediationCompiler()
    intake = FindingIntake()
    finding = intake.normalize_finding("F-1", "shadow_state", "low", {})
    pack = compiler.compile_pack(
        finding, explicit_recipe_id="refresh_venue_shadow_snapshot"
    )

    changeset = RemediationChangeSet(pack)
    changeset.add_cache_invalidation("shadow_BTC")
    changeset.add_metadata_update("last_refresh", "now")

    summary = changeset.summarize()
    assert summary["cache_invalidations_count"] == 1
    assert summary["metadata_updates_count"] == 1
    assert summary["recipe_name"] == "Refresh Venue Shadow Snapshot"
