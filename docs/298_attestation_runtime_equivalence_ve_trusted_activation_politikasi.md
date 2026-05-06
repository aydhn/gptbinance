# Attestations, Runtime Equivalence and Trusted Activation

## Attestation
Build süreci sonunda bir attester tarafından imzalanmış payload record (AttestationRecord) oluşturulur. Attestation eksikliği "review_required" seviyesinde trust verdict oluşturur.

## Runtime Equivalence
Aktif çalışan config/bundle hash'i beklenen manifest hash'i ile aynı olmalıdır. Mismatch durumunda verdict anında "blocked" olur ve incident trigger'lanabilir.
