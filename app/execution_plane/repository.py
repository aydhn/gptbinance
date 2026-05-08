from app.execution_plane.storage import ExecutionStorage


class ExecutionRepository:
    def __init__(self, storage: ExecutionStorage):
        self.storage = storage

    def save_trusted_execution(self, verdict):
        pass  # stub

    def query_attempt_history(self, spec_id: str):
        pass  # stub
