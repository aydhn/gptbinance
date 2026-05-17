# Environment Plane ve Environment Topology, Promotion Path, Isolation Governance Mimarisi

Bu belge, sistemdeki ortamların (environments) yönetimini açıklığa kavuşturur. Staging, live-like bir ortam demek değildir; her ortamın açıkça tanımlanmış topolojisi, sınırları (boundaries), paritesi, drift durumu ve izolasyon standartları vardır.

## Akış
1. **Topology:** Ortamın nasıl kurulduğu (shared, shadow, isolated vb.)
2. **Parity/Divergence:** Ortamın hedeflenen canlı ortama (live) ne kadar benzediği.
3. **Promotion:** Ortamın diğer ortamlara aktarılabilirliği (gates, readiness).
4. **Isolation/Contamination:** Ortamın diğer ortamlarla (özellikle live ile) veriyi, sırları (secrets) ne kadar ayırdığı.
5. **Trust:** Tüm bu faktörlerin birleşimiyle ortamın genel güvenilirlik durumu.

Environment governance mantığı: Fake parity ve hidden coupling kabul edilemez. Bir ortam ya tam paritelidir ya da açıkça belgelenmiş ve gerekçelendirilmiş bir diverjans (intended divergence) taşır.
