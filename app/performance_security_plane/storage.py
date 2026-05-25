from app.performance_security_plane.repository import PerformanceSecurityRepository

class StorageManager:
    def __init__(self, repository: PerformanceSecurityRepository):
        self.repository = repository
