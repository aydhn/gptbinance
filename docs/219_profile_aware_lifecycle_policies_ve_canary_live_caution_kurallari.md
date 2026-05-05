# Profile Aware Lifecycle Policies

Lifecycle policies adapt strictly based on the execution profile.

- `paper_default`: more relaxed timeout rules.
- `canary_live_caution`: incredibly strict threshold for `TIMEOUT_UNKNOWN` and orphan orders. Immediate halt on anomalies.
