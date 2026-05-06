from datetime import datetime, timezone
from app.supply_chain.models import AttestationRecord
from app.supply_chain.enums import AttestationClass
from app.supply_chain.hashes import generate_hash


class LocalAttestationGenerator:
    def generate(
        self, build_id: str, payload_hash: str, attester: str
    ) -> AttestationRecord:
        # Simple local signing substitute for demonstration
        sig_data = f"{build_id}:{payload_hash}:{attester}:secret"
        signature = generate_hash(sig_data)

        timestamp = datetime.now(timezone.utc)
        return AttestationRecord(
            id=f"att_{generate_hash(build_id+str(timestamp.timestamp()))[:8]}",
            build_id=build_id,
            attestation_class=AttestationClass.BUILD_SYSTEM,
            attester=attester,
            timestamp=timestamp,
            signature=signature,
            payload_hash=payload_hash,
        )


class LocalAttestationVerifier:
    def verify(self, record: AttestationRecord) -> bool:
        expected_sig = generate_hash(
            f"{record.build_id}:{record.payload_hash}:{record.attester}:secret"
        )
        return record.signature == expected_sig
