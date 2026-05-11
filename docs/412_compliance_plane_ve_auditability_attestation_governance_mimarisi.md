# Compliance Plane ve Auditability Governance Mimarisi

Compliance Plane, sistemin yalnızca politika veya güvenlik kurallarına sahip olmasıyla yetinmeyip, bu kuralların **uygulandığını kanıtlanabilir, denetlenebilir ve onaylanabilir** hale getiren katmandır.

## Temel Akış
1. **Requirements**: Sistemin uyması gereken zorunluluklar (örn. "Her manuel işlem onay gerektirir").
2. **Controls**: Requirement'ı karşılayan mekanizmalar (örn. "Dual-approval workflow").
3. **Evidence**: Kontrolün çalıştığını gösteren kanıtlar (örn. "Approval receipt").
4. **Attestation**: Kanıtların incelenip kontrolün geçerli olduğuna dair verilen onay.
5. **Exception/Debt**: İstisnalar ve giderilmeyen eksikliklerin yönetimi.
6. **Audit Readiness**: Denetime her an hazır olma durumu.

## Neden "Reviewed != Attested != Compliant"?
- **Reviewed**: Birinin baktığı anlamına gelir.
- **Attested**: Birinin inceleyip "bu kanıtlar doğrultusunda kontrol çalışıyor ve etkilidir" beyanında bulunduğu anlamına gelir.
- **Compliant**: Tüm requirements'ların kanıtlarla, taze attestation'larla ve kabul edilebilir seviyede bir exception/debt ile karşılandığı durumdur.

## Sınırlar
Bu katman otomatik olarak hukuki uyumluluk (regülasyon) yorumlamaz. Hangi teknik kontrollerin, hangi kanıtlarla hangi policy gereksinimlerini karşıladığını ve bu durumun zaman içindeki bütünlüğünü (freshness, equivalence) yönetir. Evidence olmadan "compliant" etiketi verilmez.
