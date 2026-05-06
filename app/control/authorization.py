def authorize_action(action_name: str, user_id: str, candidate_id: str = None) -> bool:
    """
    Mock implementation for control authorization.
    In Phase 50, staged promotion review requires readiness_board decision.
    """
    if action_name == "promote_to_live":
        if not candidate_id:
            return False
        from app.readiness_board.storage import ReadinessBoardStorage
        from app.readiness_board.repository import ReadinessBoardRepository
        from app.readiness_board.enums import BoardVerdict

        repo = ReadinessBoardRepository(ReadinessBoardStorage())
        dec = repo.get_latest_decision(candidate_id)
        if not dec or dec.verdict not in [BoardVerdict.GO, BoardVerdict.CONDITIONAL_GO]:
            print(f"Authorization denied: Candidate {candidate_id} does not have a GO decision.")
            return False
    return True


# Incident integration: authorize containment review requests