# 053 - Pozisyon Durum Makinesi ve Trade Ledger Politikası

Mevcut pozisyonların yönetimi ve ticaret kayıtlarının tutulması birbirinden ayrılmıştır.

## Position State Machine
Aşağıdaki durum geçişlerini destekler:
*   `FLAT` -> `LONG` / `SHORT`
*   `LONG` -> Reduce (azaltma) / Close (kapatma) / Reverse (tam tersine dönme)
*   `SHORT` -> Reduce / Close / Reverse

Pozisyonun ortalama giriş fiyatı (average entry) ve gerçekleşmemiş PnL (unrealized PnL) değerleri sürekli güncellenir.

## Trade Ledger
Ledger, sadece geçmişin denetlenebilir bir kaydıdır. Pozisyon sıfırlandığında (veya reverse edildiğinde), o trade "CLOSED" olarak işaretlenir ve ledger'a kaydedilir. Trade loglar, stratejinin hangi noktalarda para kazanıp kaybettiğini anlamak için hayati önem taşır.
