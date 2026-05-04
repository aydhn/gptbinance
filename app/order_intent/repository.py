from app.order_intent.models import IntentCompilationResult
from app.order_intent.storage import IntentStorage


class IntentRepository:
    def __init__(self, storage: IntentStorage):
        self.storage = storage

    def store_compilation(self, result: IntentCompilationResult):
        self.storage.save_result(result)

    def retrieve_compilation(self, run_id: str) -> IntentCompilationResult:
        result = self.storage.get_result(run_id)
        if not result:
            raise ValueError(f"No compilation result found for run_id {run_id}")
        return result
