from app.postmortem_plane.storage import PostmortemStorage
from app.postmortem_plane.models import PostmortemDefinition

class PostmortemRepository:
    def __init__(self):
        self.storage = PostmortemStorage()

    def write(self, postmortem: PostmortemDefinition):
        self.storage.save(postmortem)

    def read(self, postmortem_id: str) -> PostmortemDefinition:
        return self.storage.load(postmortem_id)
