from datetime import datetime, timezone
from app.identity.models import AuthorizationRequest, AuthorizationProof
from app.identity.authorization import authorization_engine
from app.identity.storage import identity_storage


class AuthorizationProofBuilder:
    def build_proof(self, request: AuthorizationRequest) -> AuthorizationProof:
        decision = authorization_engine.evaluate(request)

        proof = AuthorizationProof(
            request=request,
            verdict=decision.verdict,
            denial_reasons=decision.reasons,
            generated_at=datetime.now(timezone.utc),
        )

        identity_storage.save_proof(proof)
        return proof


proof_builder = AuthorizationProofBuilder()
