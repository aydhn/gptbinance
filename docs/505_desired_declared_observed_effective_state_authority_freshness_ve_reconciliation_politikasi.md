# Desired, Declared, Observed, Effective State: Authority, Freshness ve Reconciliation Politikası

Bu politika, state plane içindeki temel durum sınıflarını ve bunların nasıl değerlendirileceğini tanımlar.

## Desired vs Declared vs Observed vs Effective

-   **Desired:** Hedeflenen durum.
-   **Declared:** Resmi olarak bildirilen durum.
-   **Observed:** Gözlemlenen durum (telemetri, test).
-   **Effective:** Gerçekleşen, geçerli durum.

## Authoritative Source

Her state sınıfı için yetkili bir kaynak (authoritative source) belirlenmiştir. Örneğin, Declared state için control-plane, Observed state için telemetri yetkili kaynaktır. Kaynaklar arasında çelişki olduğunda (split-brain) öncelik kuralları uygulanır.

## Freshness

Durum bilgilerinin tazeliği kritiktir. Stale (eski) state'ler, güvenilir kararlar almak için kullanılamaz ve risk uyarıları üretir.

## Reconciliation ve Convergence

Desired/Declared ile Effective/Observed arasındaki farkların kapatılması (convergence) reconciliation sürecinin amacıdır.

## Neden Latest Status != True State?

Sadece "en son durum" bilgisi, durumun nasıl değiştiğini (transitions), kurallara uygunluğunu (guards/invariants) ve tazeliğini (freshness) göstermez. Gerçek durum (true state), tüm bu faktörlerin bütünsel bir değerlendirmesidir.
