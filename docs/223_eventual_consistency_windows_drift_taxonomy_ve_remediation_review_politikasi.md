# Eventual Consistency Windows & Drift Taxonomy

Because networks are imperfect, slight divergences right after a submit or cancel are normal.
- **Windows**: We allow `SUBMIT_ACK_TOLERANCE` and `FILL_PROPAGATION` windows to account for this.
- **Drift Classes**: `TRANSIENT_DIVERGENCE`, `SUSPICIOUS_DIVERGENCE`, `CRITICAL_DIVERGENCE`.
- **Remediation Plan**: Emits plans that are explicitly **Review-Only**. We never automatically overwrite the ledger or order state.
