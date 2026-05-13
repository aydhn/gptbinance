# Stub for revocation.py

class IdentityRevocation:
    def __init__(self, security_plane_revocation_propagation_refs: list = None):
        self.security_plane_revocation_propagation_refs = security_plane_revocation_propagation_refs or []

    def check_propagation(self):
        if not self.security_plane_revocation_propagation_refs:
            raise Exception("Revocation propagation failed")

class IdentityRevocationSecurityRef:
    pass
