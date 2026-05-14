# Hot, Warm, Cold Standby, Failover/Failback ve Split-Brain Politikası

Bu doküman standby modları ile failover mekanizmalarını yönetir.

- **Hot/Warm/Cold Standby**: Her ikincil sistem (secondary) modunu net olarak belirtmeli. Hot demek synchronous replication ve transparent cutover demektir.
- **Planned Switchover vs Emergency Failover**: Beklenmedik acil durum recovery'si, planlı switchover'dan farklı "continuity lineage" kaydı üretir.
- **Failback Sequencing**: Bir primary'ye geri dönerken, mutlaka state reconciliation yapılmalıdır.
- **Split-Brain Riskleri**: İki node'un birbirinden habersiz leader olabileceği risk senaryoları açıkça ContinuityRegistry üzerinden ContinuityExposure olarak beyan edilir.
- **Read-Only Degraded Continuation**: Failover'da mutation (write) işlemleri riske atılıyorsa, sistem read-only olarak degraded continuation yapar.
- **No Hidden Dual-Active State**: Dual-active ambigutiy kesinlikle yasaktır, her service için active location registry'de bilinmek zorundadır.
