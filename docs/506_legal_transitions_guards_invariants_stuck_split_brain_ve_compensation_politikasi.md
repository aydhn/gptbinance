# Legal Transitions, Guards, Invariants, Stuck, Split-Brain ve Compensation Politikası

Bu politika, durum geçişlerinin (transitions) ve geçersiz durumların nasıl ele alınacağını tanımlar.

## Legal Transitions

Durum geçişleri, tanımlanmış bir lifecycle içinde yapılmalıdır. Geçerli olmayan geçişler (illegal jumps) reddedilir.

## Transition Guards ve Invariants

-   **Guards:** Bir geçişin yapılabilmesi için sağlanması gereken ön koşullar.
-   **Invariants:** Sistemin her zaman koruması gereken durum kuralları (örneğin, terminal state sonrası active state'e geçilemez).

## Stuck States ve Split-Brain

-   **Stuck State:** Bir işlemin uzun süre aynı durumda kalması (timeout).
-   **Split-Brain:** Farklı yetkili kaynakların aynı nesne için çelişkili durumlar bildirmesi.

Her iki durum da yüksek severity (önem derecesi) taşır ve güveni düşürür.

## Compensation ve Rollback

Hatalı veya eksik geçişlerde, telafi (compensation) ve geri alma (rollback) mekanizmaları kullanılır. Bu mekanizmaların da kendi lifecycle'ı ve kuralları vardır.

## Neden Impossible Jumps'a İzin Verilmez?

İmkansız durum sıçramaları (örneğin, onaylanmamış bir değişikliğin direkt olarak uygulanması), audit ve güvenlik açıklarına neden olur.
