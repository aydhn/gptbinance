# Continuity Plane ve Disaster Recovery / Failover Governance Mimarisi

Bu doküman, Continuity Plane'in mimari hedeflerini açıklar.

## services -> backups/snapshots/replication -> restore/failover/failback -> trust
Continuity Plane bir zincirden oluşur. Objective ve RTO/RPO hedefleri service/criticality üzerinden hesaplanır, bu backup/snapshot stratejisine bağlanır, bu test edilmiş ve doğrulanmış (verified) bir restore/failover işlemi ile sağlamlaştırılır, ve en son Continuity Trust Engine'in ürettiği verdict olarak sistem geri kalanına sunulur.

## why backup != restore != failover != failback
Yedek (backup) bir snapshot almanızı sağlar, restore ise o state'in gerçekten çalışır şekilde geri dönülebildiğini kanıtlar. Failover ise tüm request flow'un oraya döndüğünü, failback ise origin'in güvenle yeniden main node olduğunu belirtir.

## why incident resolved != continuity restored
Uygulama çöktüğünde geçici olarak workaround yapılabilir ("incident resolved"), ancak primary state'in restore edilmesi ("continuity restored") farklı bir validation adımıdır.
