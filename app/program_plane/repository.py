from app.program_plane.storage import ProgramStorage

class ProgramRepository:
    def __init__(self, storage: ProgramStorage):
        self.storage = storage

    def get_latest_trusted_program(self, program_id: str):
        return self.storage.load(f"trusted_{program_id}")
