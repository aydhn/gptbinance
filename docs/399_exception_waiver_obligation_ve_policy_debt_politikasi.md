# Exception, Waiver, Obligation ve Policy Debt Politikası

## Exceptions ve Waivers
* Exception'lar scoped ve TTL-bound olmalıdır.
* Süresiz waiver (permanent silent waiver) yasaktır.

## Obligations
* Belirli işlemler için kanıt sunma (`MUST_ATTACH_EVIDENCE`) veya onay bekleme (`MUST_WAIT_FOR_APPROVAL`) zorunlulukları vardır.

## Policy Debt
* Kullanılan exception ve waiver'lar sistemde borç (debt) yaratır ve izlenir (`debt.py`).
