# Phase 13: Pozisyon Boyutlandırma ve Exposure Cap Politikası

## Pozisyon Boyutlandırma (Position Sizing)
Sistemin pozisyon boyutlandırma yaklaşımı basit ve deterministik olacak şekilde tasarlanmıştır:
- **Sabit Kesir (Fixed Fraction):** Temel sizing modeli, hesabın belirli bir oranını riske etmeye dayanır (Örn: %2).
- **Volatilite ve Rejim Ayarı:** Sabit kesir üzerinden çıkan boyut, pazarın mevcut rejimine (örneğin belirsizlik yüksekse) ve volatilitesine (ATR) göre küçültülebilir.

*Kurallar:*
- Kesinlikle agresif piramitleme veya kaldıraç büyütme (martingale vb.) yapılmayacaktır.
- Yüksek strateji skoru her zaman büyük pozisyon anlamına gelmez; boyutlandırma her zaman risk sınırları içinde kalmalıdır.

## Exposure Cap Politikası
Konsantrasyon ve toplam riski sınırlandırmak için katı limitler uygulanır.
- **Maksimum Brüt Exposure:** Portföyün toplam değeri üzerinden alınabilecek maksimum kaldıraç veya risk oranı.
- Eğer yeni bir intent bu sınırı aşıyorsa, Risk Engine tarafından `REJECT` veya `REDUCE` edilir.
