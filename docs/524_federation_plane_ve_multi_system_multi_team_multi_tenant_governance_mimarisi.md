# Federation Plane ve Multi-System / Multi-Team / Multi-Tenant Governance Mimarisi

Federation plane, sistemin domains/tenants -> boundaries/delegations -> portability/shared-risk -> federated verdict -> trust akışını kontrol eder.

Neden "local green != federated green"?
Çünkü lokalde güvenli olan bir eylem (örneğin bir değişikliğin yapılması), tenant isolation gap'leri veya external partner contract'ları nedeniyle globalde büyük bir shared risk oluşturabilir.

Neden "hidden shared risk" kabul edilemez?
Gizli bağımlılıklar, blast radius'un bilinmeyen bir boyuta çıkmasına sebep olur. Bu yüzden federation governance mantığı açık sınırlara ve evidence portability'e dayanır.
