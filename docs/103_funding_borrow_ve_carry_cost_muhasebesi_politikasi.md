# Funding, Borrow ve Carry Cost Muhasebesi Politikası

Kaldıraçlı işlemler "bedava" değildir. Futures tarafında periyodik olarak ödenen/alınan *Funding* ücretleri, Margin tarafında ise alınan borç üzerinden işleyen *Borrow Interest* maliyetleri vardır. Bu maliyetleri yok sayan herhangi bir backtest veya paper runtime *hatalıdır*.

## Carry Cost Engine (`carry_costs.py`)
- Sistem, türev pozisyonlarının zaman içerisinde taşıma maliyeti (Carry Cost) ürettiğini varsayar.
- `CarryCostAccounting` sınıfı bu birikimli maliyetleri takip eder ve net özetini çıkartır.

## Backtest & Paper Entegrasyonu
- Backtest simülasyonları sırasında `app/backtest/derivatives/costs.py` üzerinden belirli aralıklarla (örneğin saatlik step) funding ve borrow maliyetleri pnl'den düşülür.
- Kârlı görünen bir strateji, çok uzun süre pozisyon taşıdığı için yüksek funding maliyetlerinden dolayı zarara geçebilir. Bu sistem bu gerçeği simüle eder.
- Live Paper Trading sırasında da bu maliyetler takip edilir. Bu, strateji geliştiricilerin Live geçiş öncesinde gerçek taşıma maliyetlerini görmelerini sağlar.
