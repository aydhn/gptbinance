def semantic_conflict_template(conflict_id: str, semantic_id: str, notes: str) -> str:
    return f"⚠️ SEMANTIC CONFLICT DETECTED ⚠️\nID: {conflict_id}\nSemantic Ref: {semantic_id}\nNotes: {notes}\nAction: Resolve for canonical trust."

def dangerous_alias_template(term: str, alias: str) -> str:
    return f"🚨 DANGEROUS ALIAS DETECTED 🚨\nTerm: {term}\nAlias: {alias}\nAction: Explicitly disambiguate or remove."
