class AssuranceIntegrityReliabilityDomain:
    @staticmethod
    def calculate_reliability(assurance_record) -> int:
        return 100 if assurance_record.cases and not (assurance_record.expiry and assurance_record.expiry.is_expired) else 50
