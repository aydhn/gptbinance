from app.config_plane.storage import ConfigStorage


class ConfigRepository:
    def __init__(self):
        self.storage = ConfigStorage()
