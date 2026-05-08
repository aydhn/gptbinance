from app.simulation_plane.storage import SimulationStorage
from app.simulation_plane.registry import SimulationRegistry


class SimulationRepository:
    def __init__(self):
        self.storage = SimulationStorage()
        self.registry = SimulationRegistry()
