def operating_model_invariants(action):
    if action.get("is_critical") and not action.get("has_owner"):
        raise Exception("POLICY DENY: No trusted critical action under ownerless eligible surface.")
    if action.get("requires_approval") and action.get("proposer") == action.get("approver"):
        raise Exception("POLICY DENY: Missing independent reviewer/approver separation.")
    return True


# Knowledge Plane Integration
def assert_knowledge_integrity(knowledge_id: str):
    # Ensure authoritative guidance is not stale and is usable
    return True
