# Drift Plane ve Baseline Regression Recurrence Restriction Reimposition Governance Mimarisi

Drift Plane, kurumsal sistemlerde "normalleşme" sonrasında yavaş yavaş veya aniden ortaya çıkan sapmaları, gerilemeleri ve tekrarlayan sorunları typed, kanonik ve audit edilebilir bir şekilde yöneten katmandır.

## Temel Kavramlar

*   **Baseline:** Onaylanmış işletim zarfı (approved operating envelope).
*   **Signal:** Sapmanın ilk belirtileri.
*   **Breach:** Eşik değerlerinin (threshold) aşılması.
*   **Restriction Reimposition:** Kısıtlamaların yeniden getirilmesi.
*   **Scar:** Geçmiş hasarların (scars) yeniden aktive olması.
*   **Renormalization:** Sapmanın giderilip yeni bir baseline kurulması.
*   **Trust Verdict:** Sistemin genel güvenilirlik durumu.

## Neden Drift Plane?

Sistemlerin sadece "yeşil" (healthy) görünmesi yeterli değildir. Görünürde yeşil olan bir sistemde:
*   Küçük sapmalar (minor drift) birikerek büyük sorunlara yol açabilir (material breach).
*   Koruyucu önlemler (guardrails) sessizce kaldırılmış veya işlevsizleşmiş olabilir.
*   Yetkiler (authority) yavaşça genişlemiş (creep) olabilir.
*   Geçmiş sorunlar (scars) sinsice tekrarlıyor olabilir.

Drift Plane, "monitored != controlled != stable" ilkesiyle bu gizli riskleri görünür kılar ve engeller.

## Akış

1.  Baselines ve Signals tanımlanır.
2.  Breaches ve Restrictions yönetilir.
3.  Scars ve Renormalization ele alınır.
4.  Nihai Trust Verdict üretilir.
