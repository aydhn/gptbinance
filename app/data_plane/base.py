class SourceRegistryBase:
    def register_source(self, definition):
        raise NotImplementedError


class SnapshotBuilderBase:
    def build_snapshot(self, data):
        raise NotImplementedError


class QualityEvaluatorBase:
    def evaluate(self, snapshot):
        raise NotImplementedError


class TrustEvaluatorBase:
    def evaluate_trust(self, quality_report):
        raise NotImplementedError
