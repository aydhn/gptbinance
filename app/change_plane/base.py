class ChangeRegistryBase:
    def register(self, change):
        raise NotImplementedError

    def get_change(self, change_id):
        raise NotImplementedError

    def get_all(self):
        raise NotImplementedError

class ImpactEvaluatorBase:
    def evaluate(self, change):
        raise NotImplementedError

class VerificationEvaluatorBase:
    def evaluate(self, change):
        raise NotImplementedError

class TrustEvaluatorBase:
    def evaluate(self, change):
        raise NotImplementedError
