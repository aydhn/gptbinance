# Apply Classes & Scope Security

## Apply Sınıfları
1. **DIRECT_SAFE**: Sadece `shadow_state` refresh gibi local-read işlemler.
2. **REQUEST_GENERATION**: Orphan order cancel gibi `venue_affecting` işlemler. Bunlar asla doğrudan uygulanmaz, kontrol katmanına (Control/Governance) approval isteği olarak düşer.
3. **MANUAL_INSTRUCTION**: Operatörün CLI üzerinden bizzat yürütmesi gereken adımlar.

Bu ayrım sayesinde "Blast Radius" her zaman tahmin edilebilir ve kontrol altındadır.
