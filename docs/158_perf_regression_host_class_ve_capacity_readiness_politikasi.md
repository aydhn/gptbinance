# 158 - Perf Regression, Host Class ve Capacity Readiness Politikası

## Regresyon Nasıl Yorumlanır?
Yeni bir release candidate oluşturulduğunda, bir "Baseline" run ile "Target" run karşılaştırılır. Metriklerdeki %10'dan büyük bozulmalar "Regression" olarak işaretlenir ve önem derecesine göre (MINOR, MAJOR, CRITICAL) sınıflandırılır. %5'in altındaki değişimler "Noise" (Gürültü) olarak kabul edilir ve raporlanmaz.

## Host Class Yaklaşımı
Makineler donanımlarına göre sınıflandırılır:
- `LOCAL_MINIMAL` (2 Core, 4GB RAM)
- `LOCAL_AVERAGE` (4 Core, 8GB RAM) - Referans/Hedef
- `LOCAL_ENHANCED` (8 Core, 16GB RAM)
- `WORKSTATION_GPU_OPTIONAL` (16 Core, 32GB RAM)

## Headroom ve Concurrency Riskleri
`CapacityAnalyzer`, seçilen Host Class ve aktif Workload'ları değerlendirerek boşta kalan tahmini kapasiteyi (Headroom) hesaplar. Eğer `LOCAL_MINIMAL` üzerinde hem `PAPER` hem de `ANALYTICS_BATCH` çalıştırılmaya kalkılırsa, sistem "Caution" üretir ve latency spike'larına karşı uyarır.

## Readiness
Bir Host'un belirli workload'ları çalıştırıp çalıştıramayacağı `HostQualificationReport` ile kayıt altına alınır ve bu raporlar Governance ve Release süreçlerine kanıt (evidence) olarak sunulur.
