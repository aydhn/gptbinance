class EvidencePack:
    pass

class ReleaseIntegrityPack(EvidencePack):
    pass
class RolloutReviewPack(EvidencePack):
    pass
class CanaryReviewPack(EvidencePack):
    pass
class RollbackReadinessPack(EvidencePack):
    pass


class ReviewPackBuilder:
    def build_rca_pack(self, postmortem_id: str) -> dict:
        return {"type": "rca_review", "id": postmortem_id}
