# Quiet Hours, Maintenance ve Calendar-Aware Automation Politikası

## Quiet Hours (Sessiz Saatler)
Sistemin yoğun trading saatleri dışında veya yöneticilerin uyuduğu saatlerde daha az agresif eylem yapmasını sağlar.
Quiet Hours politikası `enabled`, `start_hour`, `end_hour` gibi değerler içerir. Bu saatlere denk gelen işler varsayılan olarak ertelenir (`DEFER`).

## Maintenance Windows (Bakım Pencereleri)
Ops katmanında aktif edilen bir maintenance window varsa, Automation katmanı `MaintenanceAwarePolicy` aracılığı ile bu durumu sorgular.
Eğer iş (job) "defer_during_maintenance" olarak işaretlenmişse, bakım bitene kadar bekler. Eğer "block" ise iptal olur.

## Takvim Farkındalığı
`calendar.py` içinde sunulan fonksiyonlar (örneğin hafta sonu kontrolü), işlerin borsa kapalıyken gereksiz yere çalışmasını engellemek için kullanılabilir.
Harici API bağımlılıkları en aza indirilerek local datetime tabanlı sade bir kontrol sağlanır.
