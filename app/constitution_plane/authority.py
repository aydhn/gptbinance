from app.constitution_plane.models import AuthorityScopeRecord

class AuthorityManager:
    def __init__(self):
        self._authorities = {}

    def register_authority(self, record: AuthorityScopeRecord):
        self._authorities[record.authority_id] = record
