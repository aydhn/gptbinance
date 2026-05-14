# Continuity Integrity, Readiness, Activation, Release, Workflow ve Security Entegrasyonu Politikası

Diğer plane'lerle olan entegrasyonu tanımlar.

- **continuity_integrity domain**: Readiness board'a Continuity Verdictlerini sunar.
- **activation/release/workflow integration**: Release atılırken, secondary node'lara olan version compatibility (Stale Secondary Risk) blocker olarak görev yapar. Failover node ile primary version eşlenmeden release activate edilemez.
- **security/compliance/reliability linkage**: Veri kaybı riski yüksek bir RPO ihlali, direkt compliance incident yaratır. Şifreli yedeğe erişimin kaybedilmesi (Key availability) security incident'tır.
- **recovery evidence requirements**: Restore testleri ve verifications, Evidence Graph pack olarak kaydedilmelidir.
