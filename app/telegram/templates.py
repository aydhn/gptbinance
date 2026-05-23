class TelegramTemplates:
    TEMPLATES = [
        "precedent_manifest_ready",
        "controlling_precedent_conflict_detected",
        "fake_analogy_detected",
        "silent_override_detected",
        "precedent_review_required",
        "precedent_summary_digest"
    ]

# Precedent Plane Integration added

class TelegramTemplate:
    def __init__(self):
        self.authority_templates = ['authority manifest ready', 'wrong scope approval detected', 'shadow authority detected', 'invalid override detected', 'authority review required', 'authority summary digest']
