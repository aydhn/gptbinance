# Reduce-Only, Liquidation ve Maintenance Margin Politikası

Türev işlemlerde en büyük riskler: pozisyonu kapatırken yanlışlıkla ters yönde yeni pozisyon açmak ve hesap teminatının (margin) eriyip borsanın pozisyonu likide etmesidir.

## Reduce-Only Güvenliği
`app/execution/derivatives/reduce_only.py` kesin kurallar koyar:
- Bir order `is_reduce_only=True` olarak geldiyse, sistem bu emrin **asla** mevcut pozisyonun mutlak büyüklüğünü (absolute value) artırmasına izin vermez.
- Eğer mevcut pozisyon 2 BTC Long ise ve 5 BTC Short reduce-only emri gelirse, bu emir iptal edilmez ancak *güvenli bir şekilde 2 BTC'ye kırpılır* (`ADJUSTED`).
- Yanlış yönde (örneğin Long iken Long) gelen reduce-only emirleri anında reddedilir (`REJECTED`).

## Liquidation Yaklaşımı Politikası
Sistem bu fazda borsanın karmaşık liquidation motorunu birebir reverse-engineer etmez. Bunun yerine muhafazakar bir yaklaşık (approximate) model kullanır:
- Maintenance Margin: Belirli bir oran üzerinden (örn %0.5) hesaplanır.
- **Liquidation Proximity Band**: `SAFE`, `WARNING`, `DANGER` olmak üzere üç seviyeli bir şerit oluşturur.
- Eğer fiyat `WARNING` veya `DANGER` bandına girerse, sistem yeni pozisyon açılışlarını engeller. Sadece `reduce_only` emirlere (hayat kurtaran emirlere) izin verir. Telegram üzerinden anında uyarı gönderilir.
