# Risk Integrity, Readiness, Activation ve Incident Entegrasyonu Politikası

Phase 66 Risk Plane, sadece kendi içinde hesaplama yapmaz; tüm kontrol mimarilerine entegredir.

## Risk Integrity Domain & Readiness
Readiness Board artık `risk_integrity` adlı yeni bir evidence domain içerir. Bir staged activation yapılabilmesi için risk trust'ın "TRUSTED" dönmesi zorunludur.

## Activation Guards
Activation Plane, `TrustVerdict` üzerinden "DEGRADED" veya "BLOCKED" döndüren risk senaryolarında active hale geçmeyi durdurur.

## Risk Incidents
Emergency Breach'ler `app/incidents/intake.py` için bir tetikleyicidir. Bu bir "incident" olarak işaretlenir ve Reliability SLO bütçelerinden düşer.

## Evidence Graph
Tüm üretilen Risk Artifact'ları, manifest'ler ve limit yapıları `Evidence Graph`'e yazılır. Operasyonel bir problem yaşandığında, bu evidence graph üzerinden "Neden cooldown bypass edildi?" ya da "Hangi limit hard-blocked durumdaydı?" soruları audit edilebilir.
