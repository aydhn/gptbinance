# 157 - Latency, CPU, RAM, Disk, Network Bütçeleri Politikası

## Bütçelerin Tanımı
Her işletim modunun (paper, live, testnet vb.) kendine özgü sınırları vardır.
- **Latency**: Kritik execution path'inin işlem süreleri p95, p99 gibi yüzdelik dilimlerle ölçülür (örneğin, PaperExchange emir iletimi p95 < 50ms).
- **CPU**: Ortalama ve Peak CPU kullanımı.
- **RAM**: Peak memory ve Memory Growth (Leak tespiti için).
- **Disk/Network**: I/O throughput ve Network TX/RX rate sınırları.

## Soft vs Hard Budgets
- **Soft Budget**: Aşıldığında uyarı veya "Caution" üretir. Sistem çalışmaya devam eder ancak headroom azalmıştır.
- **Hard Budget**: Aşıldığında sistem bir "Blocker" veya "Failure" state üretebilir. Özellikle "Live" modlarda memory leak şüphesi (hard budget ihlali) çok kritik bir durumdur.

## Mode ve Profil Bazlı Bütçeler
`BudgetRegistry` üzerinden tanımlanan bütçeler statiktir ve sadece tanımlandıkları profillerde (applicable_modes) geçerlidir. Böylece `ANALYTICS_BATCH` gibi bir workload'un disk yazma limitleri, `PAPER_RUNTIME_CYCLE`'dan çok daha esnek olabilir.
