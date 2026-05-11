class PolicyIntegrityDomain:
    def evaluate(self, trust_verdict):
        return trust_verdict.verdict.name == "TRUSTED"
