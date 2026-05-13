class IdentityIntegrityEvidence:
    pass


class ObservabilityIntegrityEvidence:
    def __init__(self, trust_posture: str, gap_burden: int, sampling_opacity: bool):
        self.trust_posture = trust_posture
        self.gap_burden = gap_burden
        self.sampling_opacity = sampling_opacity

class SecurityIntegrityEvidence:
    def __init__(self, security_trust: str, exposure_burden: str, patch_rotation_hygiene: str, secret_cert_freshness: str, security_exception_burden: str):
         self.security_trust = security_trust
         self.exposure_burden = exposure_burden
         self.patch_rotation_hygiene = patch_rotation_hygiene
         self.secret_cert_freshness = secret_cert_freshness
         self.security_exception_burden = security_exception_burden
