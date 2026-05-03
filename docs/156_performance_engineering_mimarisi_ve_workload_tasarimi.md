# 156 - Performance Engineering Mimarisi ve Workload Tasarımı

## Neden Performans Katmanı?
Sistem modülerleştikçe ve yetenekleri arttıkça, canlı (veya paper) operasyonların ortalama bir yerel donanımda ne kadar kaynak tükettiğini bilmek zorunlu hale gelir. Aksi takdirde, backtest, analytics veya governance gibi yoğun işlemler scheduler tarafından başlatıldığında execution loop'unu ezebilir. Bu katman "micro-optimization" yapmaz; görünürlük, bütçe yönetimi ve regresyon tespiti sağlar.

## Workload Registry
"Performans" soyut bir kavramdır. Biz ölçümlerimizi spesifik iş yükleri (workloads) bağlamında yaparız.
- `PAPER_RUNTIME_CYCLE`
- `GOVERNANCE_REFRESH`
- `ANALYTICS_BATCH`
Her workload, hangi bileşenleri çalıştıracağını, beklenen concurrency seviyesini ve hangi modlarda çalışmasının güvenli olduğunu tanımlar.

## Profiling Primitives
Process düzeyinde CPU, Bellek (Memory), Disk I/O ve Network I/O örneklenir. Bunun yanında `LatencyTracker` ile kritik akışların (p50, p95, p99) gecikme süreleri kaydedilir.

## Budgets and Bottlenecks
Her profilin (örneğin paper, testnet, live) kendine ait kaynak (RAM/CPU/Disk) ve gecikme bütçeleri vardır. Bir profilleme çalışması bittiğinde, sonuçlar bu bütçelerle karşılaştırılır. Limitlerin aşılması durumunda `BottleneckAnalyzer` devreye girerek, örneğin "CPU-Bound: Main execution loop using > 80% CPU" gibi delile dayalı hipotezler üretir.

## Yerel-First ve Neden Auto-Tuning Yok?
Bu projenin amacı, kısıtlı kaynaklara sahip tek bir sunucuda güvenli işlem yapmaktır. Performans ölçümleri, sistemi "sessizce hızlandırmak" (auto-tuning, parametre değiştirme, throttling) için değil, **operatöre kapasite sınırı uyarısı vermek** için kullanılır. Sessizce değişen bir sistem, trade yaparken güvenilmezdir. Tüm kararlar deterministik ve ölçülebilir kalmalıdır.
