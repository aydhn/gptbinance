# Observability Plane & Telemetry Diagnostics Governance

## Neden Observability Plane Gerekiyor?
Alerts, incidents, postmortems ve reliability surfaces ancak altındaki telemetry gerçeği kadar sağlamdır. Bu katman "dashboard" yapmaz, sistemin "gerçeğini" ve "zamanını" doğru kaydettiğini yönetir.

## Metric != Log != Trace != Event
Log serbest bir form değildir, trace kopuk olamaz, olayların event_time'ları ile ingest_time'ları birleştirilemez.
