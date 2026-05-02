# Command Journal ve Operator Accountability Politikası

## Command Journal Neden Tutulur?
Operatörlerin sisteme yönelik tüm kritik talepleri ve verdikleri onay kararları mutlak bir izlenebilirlik gerektirir. Command Journal, sistemi kimin ne zaman, hangi bağlamla ve neden değiştirmek istediğinin değişmez (immutable) ve ekleme tabanlı (append-only) bir kanıtını sunar.

## Operator Accountability (Hesap Verebilirlik)
Her request, approval ve revocation eylemi kesin bir `OperatorIdentity` ve zaman damgası içerir. Ortak, genel "admin" hesapları yerine, spesifik rollere sahip operatör kimlikleri üzerinden işlem yapılır.

## Request vs Execution Ayrımı
Bir aksiyonun talep edilmesi (request), onaylanması (approval) ve nihai olarak çalıştırılması (execution) birbirinden farklı olaylardır. Journal, bir aksiyonun ne zaman talep edildiğini, kimlerin onayladığını ve execution katmanında ne zaman devreye alındığını (veya execution aşamasında stale/fail olup olmadığını) ayrı ayrı kayıt altına alır.

## Revoke / Expire / Reject Görünürlüğü
Bir onay sonradan geri çekilirse (Revoke), süresi dolarsa (Expire) veya reddedilirse (Reject), Journal üzerinde ilgili aksiyonun nihai durumu güncellenir. Bu, audit raporlarında "hangi aksiyonlar neden durduruldu" sorusunun net bir şekilde görünmesini sağlar.
