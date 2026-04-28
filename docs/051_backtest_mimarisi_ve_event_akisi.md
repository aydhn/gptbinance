# 051 - Backtest Mimarisi ve Event Akışı

Backtest sistemi, sinyal üreten stratejilerin gerçek dünyada nasıl performans gösterebileceğini dürüstçe değerlendirmek için tasarlanmıştır. Bu yüzden event-driven bir akış kullanır.

## Zincir:
1.  **Replay Driver:** Tarihsel veriyi bar bar okur.
2.  **Strategy/Regime Evaluation:** Mevcut bar için strateji motoru çalışır, sinyaller üretilir.
3.  **Intent Generation:** Sinyaller, alım-satım niyetine (`SimulatedOrderIntent`) dönüşür.
4.  **Fill Model:** Sonraki barda niyet, belirlenmiş varsayımlarla (`FillAssumption.NEXT_BAR_OPEN` vb.) doldurulur (`SimulatedFill`).
5.  **Position State:** Doldurulan emre göre mevcut pozisyon güncellenir.
6.  **Ledger:** Trade kaydı oluşturulur/kapatılır.
7.  **Equity:** Hesap bakiyesi ve PnL güncellenir.
8.  **Performance:** Tüm run bittiğinde metrikler hesaplanır.

Bu katı ayrım, stratejilerin kendi performanslarını abartmasını engeller ve gerçeğe yakın bir simülasyon sunar.
