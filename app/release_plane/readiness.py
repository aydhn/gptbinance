class ReleaseReadiness:
    def __init__(self):
        self.identity_integrity = True
        self.observability_coverage = True

    def update_security_burden(self, vulnerable_bundle_burden: bool = False, stale_patch_burden: bool = False, exposed_secret_dependency: bool = False, stale_cert_burden: bool = False):
        if vulnerable_bundle_burden or stale_patch_burden or exposed_secret_dependency or stale_cert_burden:
            self.identity_integrity = False
            self.observability_coverage = False
