from app.reviews.storage import InMemoryReviewStorage


class ReviewRepository:
    def __init__(self, storage: InMemoryReviewStorage):
        self.storage = storage

    def save_item(self, item):
        self.storage.save_item(item)

    def get_pending_items(self):
        return [
            item
            for item in self.storage.items.values()
            if item.state.value in ["pending", "assigned"]
        ]
