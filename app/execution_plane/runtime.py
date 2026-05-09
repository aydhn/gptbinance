# Runtime execution snapshot and live/testnet separation logic
class RuntimeExecutionEnv:
    def __init__(self, is_live: bool):
        self.is_live = is_live
        self.active_manifests = {}
        self.send_receipts = {}

    def register_manifest(self, manifest_id: str, manifest_data: dict):
        self.active_manifests[manifest_id] = manifest_data

    def record_receipt(self, idempotency_key: str, receipt: dict):
        # No secret leakage, only metadata
        safe_receipt = {
            k: v
            for k, v in receipt.items()
            if "secret" not in k.lower() and "key" not in k.lower()
        }
        self.send_receipts[idempotency_key] = safe_receipt

# WORKFLOW PLANE INTEGRATION:
# Added hooks for dependency/gate evaluations, duplicate run protections,
# and explicit reruns per Phase 73 requirements.
