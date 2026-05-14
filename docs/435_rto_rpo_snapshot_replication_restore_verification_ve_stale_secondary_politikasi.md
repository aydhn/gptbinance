# RTO, RPO, Snapshot, Replication, Restore Verification ve Stale Secondary Politikası

Bu doküman, continuity metrikleri (RTO/RPO) ve snapshot bazlı replikasyon standartlarını tanımlar.

- **RTO/RPO**: Katı ve ortam bazlı (live vs. paper) standartlardır.
- **Snapshot Cadence**: Belirlenen RPO hedeflerini karşılayacak sıklıkta olmalıdır.
- **Replication Lag**: Replikasyon gecikmeleri açıkça izlenir ve threshold'ları geçerse continuity review başlatır.
- **Restore Verification**: Bir snapshot, ancak integrity, consistency ve lack of regressions ile verify edildikten sonra geçerli bir continuity teminatı sayılır.
- **Stale Secondary Riskleri**: Uyumsuz şemaya (migration mismatch) sahip ikincil sunucular, recovery point olarak kullanılamaz, "Stale Secondary Risk" alarmı oluşturur.
