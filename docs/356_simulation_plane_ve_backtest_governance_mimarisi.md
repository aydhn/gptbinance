# Simulation Plane ve Backtest Governance Mimarisi

Bu doküman, Phase 70 ile kurulan Simulation Plane'in (Simülasyon Düzlemi) yapısını ve Backtest Governance (Geriye Dönük Test Yönetişimi) mimarisini açıklamaktadır.

## Temel Felsefe
- **Runs -> Assumptions -> OOS/Walk-Forward -> Results -> Sensitivities -> Trust Akışı:** Bir simülasyonun sonucu kendi başına değerlendirilemez. Her sonuç, belirli varsayımlar (assumptions) üzerine kuruludur ve OOS (Out-of-Sample) testleri ile desteklenmelidir.
- **Replay != Backtest:** Replay, olayın gerçeğe uygun şekilde canlandırılmasıdır (event-truth). Backtest ise bar verilerine dayalı bir yaklaşımdır (approximation) ve ikisi aynı güvenilirlikte değildir.
- **Hidden Assumptions Yok:** Tüm fill (doldurma), slippage (kayma), latency (gecikme) varsayımları açık ve denetlenebilir olmalıdır. Gizli varsayımlar yasaktır.

## Bileşenler
- **Registry:** Tüm simülasyon tanımlarının ve koşularının canonical olarak tutulduğu yer.
- **Modes:** Replay, Backtest, Paper vb. simülasyon modlarının tanımları.
- **Partitions:** Train, Validation, Test, OOS, Walk-Forward ayrımlarının yönetimi.
- **Assumptions:** Simülasyonun dayandığı varsayımların manifestosu.
- **Equivalence & Divergence:** Farklı simülasyon modları arasındaki eşdeğerlik ve sapmaların analizi.
- **Trust:** Simülasyon sonuçlarının güvenilirliğine dair nihai karar motoru.
