# Ops Control Plane Mimarisi ve Session Supervisor

Operasyon kontrol düzlemi, sistemin execution/strategy motorunun dışında oturur. Bir oturumun (session) kontrollü başlatılması, durdurulması ve recovery süreçlerini izler.
Akış: Readiness Check -> Reconcile / Hydrate -> Session Supervisor (Active) -> Graceful Stop / Crash / Drain

Sistemin riskleri sadece algoritmik değildir, ayrıca çevresel hatalara ve operasyon hatalarına bağlıdır. Supervisor, bu riskleri merkezileştirip operasyonel kararlar alır.
