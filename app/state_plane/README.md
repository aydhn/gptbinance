# Phase 99: State Plane, Lifecycle / Status / Transition / Reconciliation Governance

Bu faz, sistemdeki state truth, lifecycle, status, transition ve reconciliation yönetiminin nasıl ele alınacağını gösteren bir governance katmanı kurar.

## Temel Felsefe

Sistemimizde durum bilgisi (status) tek bir string alanla ifade edilmez. Bunun yerine, durumun farklı perspektiflerini ve bağlamlarını yakalayan bir yaklaşım benimsenmiştir:
- **Desired State**: İstenen durum (Operatör tarafından).
- **Declared State**: Bildirilen durum (Control-plane tarafından).
- **Observed State**: Gözlemlenen durum (Telemetri tarafından).
- **Effective State**: Fiili durum.
- **Reconciled State**: Çelişkilerin giderildiği, doğrulanmış durum.

## Ne Sağlar?

1.  **Unified State Plane Framework:** Tüm objeler `StateObject` altında yönetilir, lifecycle ve class tabanlıdır.
2.  **Legal Transitions:** Sadece lifecycle dahilindeki `states` listesinde olan durumlara geçilebilir.
3.  **Stuck / Split-Brain Algılama:** Gözlemlenen ile bildirilen uyumsuz olduğunda split-brain tespit edilir ve trust düşer.
4.  **CLI Desteği:** `--show-state-registry`, `--show-state-object`, `--show-state-trust` gibi yeni komutlarla audit desteklenir.

## Dosya Yapısı

- `app/state_plane/models.py`: Dataclass temelli modeller.
- `app/state_plane/registry.py`: Canonical registry.
- `app/state_plane/desired.py` vb: State setter ve yönetim metotları.
- `app/state_plane/trust.py`: Trust verdict engine.
- `app/cli_state_plane.py`: CLI komutları, `app/main.py` ile entegredir.
