# 194. Universe Snapshot, Diff ve Downstream Impact Politikası

Universe katmanı, strateji, portföy ve risk kararlarının dayandığı temeli temsil eder. Bu temeldeki değişikliklerin takip edilebilir olması kritik önem taşır.

## Universe Snapshots
Sistem, belirli bir anda geçerli olan sembol setini (eligible, caution, blocked) içeren "Snapshot"lar üretir. Bu snapshot'lar, strateji kararlarının ve portföy tahsislerinin hangi evrene dayanarak yapıldığını belgeler ve geriye dönük (replay) analizleri mümkün kılar.

## Diff Engine
Yeni bir snapshot üretildiğinde, sistem önceki snapshot ile karşılaştırma yaparak bir "Diff" oluşturur. Bu diff şunları gösterir:
- Eklenen (Added) semboller
- Çıkarılan (Removed) semboller
- Durumu veya uygunluğu değişen (Changed) semboller

## Downstream Etkisi ve Historical Replay
- Bir sembol evrenden çıktığında veya engellendiğinde, bu durum portföy yöneticisine ve risk motoruna bildirilir (örneğin, açık pozisyonların izlenmesi veya kapatılması gerekebilir).
- Backtest ve Replay motorları, işlemleri gerçekleştirirken geçmiş Universe Snapshot'larını kullanarak "zamanında doğru olan" evrene göre hareket ederler. Güncel evrendeki değişiklikler geçmiş testleri bozmaz.
