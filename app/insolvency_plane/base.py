class InsolvencyRegistryBase:
    def register(self, obj):
        pass
    def get(self, obj_id):
        pass

class EstateEvaluatorBase:
    def evaluate(self, estate):
        pass

class PlanEvaluatorBase:
    def evaluate(self, plan):
        pass

class TrustEvaluatorBase:
    def evaluate(self, insolvency):
        pass
