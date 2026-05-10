class ArtefactFamily:
    RELEASE_DEFINITION = "release_definition"
    RELEASE_CANDIDATE = "release_candidate"
    RELEASE_BUNDLE = "release_bundle"
    BUNDLE_PIN = "bundle_pin"
    RELEASE_REPORT = "release_report" # Compatibility, Readiness, Rollout, Diff, Supersession, Hotfix, Rollback, Equivalence, Trust

class ArtefactRelation:
    RELEASED_UNDER = "released_under"
    BUNDLED_AS = "bundled_as"
    PINNED_BY = "pinned_by"
    ROLLED_OUT_AS = "rolled_out_as"
    SUPERSEDED_BY = "superseded_by"
    ROLLED_BACK_BY = "rolled_back_by"
    DIVERGED_RELEASE_FROM = "diverged_release_from"
