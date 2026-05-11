# Policy Plane ve Invariant / Exception Governance Mimarisi

## Amaç
Bu döküman, sistemde policy, invariant ve obligation kavramlarının merkezi, typed ve context-aware olarak nasıl yönetildiğini tanımlar.

## Temel Akış
`policies -> contexts -> verdicts -> obligations -> exceptions/waivers`

1. **Policies**: `registry.py` içinde tanımlanır.
2. **Contexts**: `contexts.py` üzerinden oluşturulur, environment, stage ve risk seviyesini içerir.
3. **Verdicts**: `evaluations.py` tarafından üretilir (ALLOW, DENY, vb).
4. **Obligations**: Verdict'ler ile birlikte üretilebilir, manuel inceleme veya kanıt gerektirir.
5. **Exceptions/Waivers**: Yasaklanan işlemler sadece `exceptions_tokens.py` veya `waivers.py` üzerinden scope ve süre (TTL) kısıtlı olarak geçilebilir.

## Temel Kurallar
* **No Hidden Allow Path**: Her izin explict bir kural tarafından verilmelidir.
* **Allow != Allow_with_Review**: İzinler arasındaki fark nettir.
* **Exception creates Debt**: Her istisna sistemde bir borç (debt) oluşturur.
