class AssuranceIntegrityDomain:
    @staticmethod
    def evaluate(assurance_record) -> str:
        if not assurance_record.cases:
            return "caution"
        return "pass"
