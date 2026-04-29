# Phase 17: Mainnet Start Gates ve Post-Trade Audit Politikası

## Start Gates (Canlıya Başlama Kapıları)
Sistemin mainnet'te bir saniye bile çalışabilmesi için şu kapıların firesiz geçilmesi zorunludur:
1. `mainnet_armed = True` (Ops manuel arm)
2. `ops_readiness_pass = True` (Control plane onayı)
3. `reconciliation_clean = True` (Askıda emir yok)
4. `active_maintenance = False`
5. `kill_switch_active = False`
6. `rollout_mode` != `full_live_locked`
7. Capital cap `allowlist` tanımlı.

## Post-Trade Audit & After-Action Summary
Canlı session'da gerçekleşen her Submit, Fill, Cancel, Cap Intervention veya Rollback bir `LiveAuditRecord` olarak loglanır. Session durduğunda (`stop`, `halt`, `flatten`) `LiveAfterActionSummary` json formatında diske yazılır. Canlı ortamda "hesaba ne oldu" sorusu asla cevapsız kalamaz.
