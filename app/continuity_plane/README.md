# Continuity Plane

## Neden Continuity Plane Gereklidir?
Reliability ve incident katmanları olsa bile, service veya state gerçekten başka bir yerde sürdürülebilir değilse sistem kırılgandır.
Snapshot vardır ama restore test edilmemiştir, replication vardır ama RPO ölçülmemiştir, failover planı vardır ama workflow ordering bozulur, secondary ayaktadır ama release/config/policy drift yüzünden güvenli değildir.
Sonuçta kriz anında continuity gerçeği yerine umut çalışır.
Bu yüzden continuity definitions -> objectives -> backups/snapshots/replication -> restore verification -> failover/failback -> debt/exposure zinciri ayrı bir governance katmanı gerektirir.

## Continuity Akışı
services -> backups/snapshots/replication -> restore/failover/failback -> trust

## Kavramsal Ayrımlar
* Backup != Restore != Failover != Failback
  - Yedek olması restore edilebildiğini göstermez. Restore edilmesi failover'ın başarılı olduğunu göstermez. Failover ise failback'in güvenli olduğunu göstermez.

* Incident Resolved != Continuity Restored
  - Incident çözülmüş olabilir ama business continuity tam sağlanmamış olabilir veya failback henüz tamamlanmamış olabilir.

## Bu Fazın Sınırları
Bu faz "DR wiki sayfası yaz ve geç" fazı değildir.
Bu faz "backup alıyoruz işte" fazı değildir.
Bu faz generic backup tool kopyası yazmaz.
Bu faz hidden manual failover path açmaz.
