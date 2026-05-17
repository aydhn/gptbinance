# State Plane ve Lifecycle Status Transition Reconciliation Governance Mimarisi

Bu belge, sistemdeki state truth, lifecycle, status, transition ve reconciliation yönetiminin nasıl ele alındığını açıklar.

## Desired / Declared / Observed / Effective -> Reconciliation -> Terminal / Trust Akışı

Sistemimizde durum bilgisi (status) tek bir string alanla ifade edilmez. Bunun yerine, durumun farklı perspektiflerini ve bağlamlarını yakalayan bir yaklaşım benimsenmiştir:

1.  **Desired State:** Operatör veya sistem tarafından istenen hedeflenen durum.
2.  **Declared State:** Control plane veya yetkili bir kaynak tarafından resmi olarak ilan edilen durum.
3.  **Observed State:** Sistemden, telemetri veya testler aracılığıyla gözlemlenen mevcut durum.
4.  **Effective State:** Politika ve kuralların uygulanması sonrası ortaya çıkan, sistemin fiili durumu.

Bu durumlar arasındaki farklılıklar, reconciliation (mutabakat) süreci ile değerlendirilir ve convergence (yakınsama) veya divergence (ıraksama) tespit edilir.

## Neden Observed != Effective != Reconciled?

-   **Observed:** Sadece ne gördüğümüzdür. Gözlem eski (stale) olabilir veya geçici bir durumu yansıtabilir.
-   **Effective:** Gözlemlerin, politikaların ve yetkilerin birleşimiyle ortaya çıkan gerçek, fiili durumdur.
-   **Reconciled:** Desired/Declared ile Effective/Observed arasındaki farklılıkların giderildiği, uyumlu durumdur.

## Neden Phantom Completion'a İzin Verilmez?

Phantom completion, bir sürecin (örneğin migration veya release) gerçekte tamamlanmadan "completed" olarak işaretlenmesidir. State plane, transition'ların belirli ön koşulları (guards, invariants) karşılamasını ve reconciliation'ın sağlanmasını zorunlu kılarak bu durumu önler.

## State Governance Mantığı

State governance, "status theater" (durum tiyatrosu) yerine somut, kanıta dayalı ve denetlenebilir durum yönetimi sağlar. Split-brain, stuck state, illegal transition gibi durumlar görünür kılınır ve güven (trust) kararlarını doğrudan etkiler.
