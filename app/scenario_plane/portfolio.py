# portfolio
from app.scenario_plane.models import *
from app.scenario_plane.enums import *
from app.scenario_plane.exceptions import *

class PortfolioManager:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def get(self, id):
        return next((x for x in self.items if getattr(x, 'id', None) == id), None)
