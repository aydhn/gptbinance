# Phase 13: Drawdown Brake, Kill Switch ve Hard Stop Politikası

## Drawdown Brake
Sistem, en yüksek hesap bakiyesini (Peak Equity) sürekli izler ve gerileme (drawdown) oranını hesaplar.
- **Normal:** İşlemler standart boyutlarda devam eder.
- **Caution:** Belirli bir eşik aşıldığında (Örn: %10), sistem dikkatli moduna geçer.
- **Reduce:** Daha yüksek bir eşikte (Örn: %15), pozisyon boyutları otomatik olarak küçültülür.
- **Hard Stop:** Kritik eşikte (Örn: %20), tüm yeni işlemler veto edilir.

## Kill Switch
Sistemin kontrol dışı hareket etmesini önlemek amacıyla, aşağıdaki durumlarda tetiklenir:
- Maksimum Drawdown ihlali.
- Kabul edilemez Exposure büyüklükleri (Konfigürasyon veya veri hatası ihtimali).
- Sürekli olarak reddedilen intent akınları (Reject Storm).
- Manuel müdahale veya config bozulması.

Tetiklendiğinde, Kill Switch aktif olur ve `KillSwitchEvaluator` raporu üzerinden sistemin işleyişini bloklamak için gerekli `Hard Stop` altyapısını sağlar. Operasyonel fazlarda (Live/Paper) bu bayrak emir gönderimini fiziksel olarak kesecektir.
