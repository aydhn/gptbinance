# Autonomy Plane ve Human/Agent Auto-Execution Bounded Delegation Governance Mimarisi

Autonomy Plane, sistemdeki otonom ajanların eylemlerini kontrol etmek, sınırlandırmak ve denetlemek için tasarlanmıştır.

## Akış
agents/tasks -> permissions/delegations -> guardrails/self-checks -> execution/intervention -> halt/trust

## Kavramlar
- capability != permission != autonomy
- Hiçbir ajan, yetkisini (permission) kendi kendine alamaz veya sınırını genişletemez (no self-approval).
- Otonomi denetimi, insan hesabı ve kontrolü (human-accountability) çerçevesinde değerlendirilir.
