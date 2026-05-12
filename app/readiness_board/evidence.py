class IdentityIntegrityEvidence:
    pass


class ObservabilityIntegrityEvidence:
    def __init__(self, trust_posture: str, gap_burden: int, sampling_opacity: bool):
        self.trust_posture = trust_posture
        self.gap_burden = gap_burden
        self.sampling_opacity = sampling_opacity
