from typing import Any
from app.postmortems.storage import PostmortemStorage


class PostmortemRepository:
    def __init__(self):
        self.storage = PostmortemStorage()

    def get_by_id(self, postmortem_id: str):
        return self.storage.load(postmortem_id)

    def save(self, postmortem: Any):
        pass
