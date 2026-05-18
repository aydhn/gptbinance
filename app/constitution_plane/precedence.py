from app.constitution_plane.models import PrecedenceRecord

class PrecedenceEvaluator:
    def __init__(self):
        self._precedences = []

    def add_precedence(self, record: PrecedenceRecord):
        self._precedences.append(record)

    def evaluate(self, domain_a: str, domain_b: str, scope: str):
        for p in self._precedences:
            if p.dominant_domain == domain_a and p.yielding_domain == domain_b and p.scope == scope:
                return domain_a
            elif p.dominant_domain == domain_b and p.yielding_domain == domain_a and p.scope == scope:
                return domain_b
        return None
