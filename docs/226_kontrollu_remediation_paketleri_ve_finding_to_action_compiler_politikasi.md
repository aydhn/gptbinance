# Phase 44: Remediation Orchestration Policy

Bu doküman, sistemin "drift", "orphan order", veya "reconciliation mismatch" gibi bulgulara (findings) nasıl tepki vereceğini tanımlar.

## Temel Kural
**SİSTEM KESİNLİKLE AUTO-FIX YAPMAZ.**
Venue state'i gizlice mutate eden otomatik repair motorları yasaktır.

## Finding -> Pack Derlemesi
1. **Intake**: Finding normalize edilir.
2. **Recipe Registry**: İlgili bulgu türü için uygun çözüm senaryosu bulunur.
3. **Compile**: Kapsam (Scope) ve Risk (Safety Class) belirlenerek bir `RemediationPack` üretilir.
