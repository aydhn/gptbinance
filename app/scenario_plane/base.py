class BaseManager:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def get(self, id):
        return next((x for x in self.items if getattr(x, 'id', None) == id), None)
