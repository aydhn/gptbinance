from app.constitution_plane.models import VerdictBundle

class BundleManager:
    def is_bundle_complete(self, bundle: VerdictBundle, required_domains: list) -> bool:
        present_domains = [dv.domain for dv in bundle.domain_verdicts]
        missing = [d for d in required_domains if d not in present_domains]
        bundle.missing_domains = missing
        return len(missing) == 0
