# 159 - Bottleneck Attribution ve Operating Envelope Politikası

## Bottleneck (Darboğaz) Hipotezleri
Performans düşüklüğü tespit edildiğinde, sistem şu hipotezlerden birini test eder:
- **CPU_BOUND**: Ortalama işlemci kullanımı > %80.
- **MEMORY_BOUND**: Bellek kullanımında belirgin ve sürekli bir artış (Memory Leak Suspicion).
- **IO_BOUND**: Süreye oranla çok yüksek Disk Write MB.
- **NETWORK_BOUND**: Süreye oranla çok yüksek Network TX/RX.

## Evidence Refs
Darboğazlar birer varsayımdır, kesin kanıt gerektirir. Sistem, hangi metriklerin (Örn: `Average CPU utilization was 92.5%`) bu karara yol açtığını `evidence` alanında açıklar.

## Recommended Operating Envelope ve Admission
`AdmissionController`, hangi iş yüklerinin yan yana çalışmasının (concurrency) riskli olduğuna dair öneriler (caution) üretir. Bu bir **enforcement (zorlama)** değil, bir **recommendation (öneri)** motorudur. Opsiyonlar (örneğin, "Testnet sırasında ağır Governance Refresh çalıştırmak Lock Contention yaratabilir") Telegram uyarılarına veya CLI raporlarına yansır ancak runtime'ı bloke edip crash ettirmez.
