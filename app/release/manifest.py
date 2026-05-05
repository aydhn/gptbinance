def build_release_manifest(intent_id: str, candidate_id: str) -> dict:
    """
    Mock implementation for release manifest.
    In Phase 50, incorporates board decision refs.
    """
    return {
        "intent_id": intent_id,
        "candidate_id": candidate_id,
        "board_decision_ref": None,
        "board_memo_ref": None
    }
