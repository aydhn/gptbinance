# Canary, Staged Rollout, Hold, Supersession ve Rollback Politikası

- **Canary Semantics**: Kapsamı daraltılmış test. Kanıt olmadan tam sürüm onayı alamaz.
- **Staged Rollout**: candidate_prepared -> canary_active -> probationary_active -> live_full.
- **Holds**: Risk veya inceleme beklendiğinde rollout durdurulur (TTL ile).
- **Supersession**: Önceki bir sürüm, yeni bir sürüm ile net şekilde yer değiştirilir.
- **Rollback**: Ön koşulları sağlayan hazır paketlerin geri alınması.
