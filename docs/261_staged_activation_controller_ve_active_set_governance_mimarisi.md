# Staged Activation Controller ve Active Set Governance Mimarisi

## Board Decision -> Activation Intent -> Rollout Plan Akışı
1. **Board Decision:** Readiness Board bir aday için "GO" veya "CONDITIONAL-GO" kararı verir.
2. **Activation Intent:** Karar, kapsam (scope), kısıtlamalar ve onay id'si ile bir `ActivationIntent` nesnesine çevrilir. (Scope Enforcer devreye girer).
3. **Rollout Plan:** Intent, ne kadar sürede hangi ortamlarda test edileceğine dair bir dizi `ActivationPlanStep` oluşturmak üzere `RolloutPlanner`'a aktarılır.
4. **Probation:** Her adımda, sistemin sağlığını doğrulayan `ProbationWindow` devreye girer.

## Neden Direct Activation Yok? (Why No Direct Activation)
Sistemde "deploy -> aktif et" gibi doğrudan bir süreç kasten yasaklanmıştır. Doğrudan aktivasyon, hataların tüm kapsama anında yayılmasına (blast radius) neden olur. Staged Activation, hatayı ilk dar kapsamda (stage_0_observe_only) yakalamayı hedefler.
