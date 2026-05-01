# Automation Scheduler Mimarisi ve Gate'li Workflow Politikası

## Neden Local Scheduler Katmanı Gerekiyor?
Trading operasyonları, veri tazeleme, istatistik derleme ve health check gibi periyodik, deterministik ve denetlenebilir eylemlere ihtiyaç duyar.
Bu akışların tek tek manuel CLI komutları ile yürütülmesi operasyonel sürdürülebilirliği zedeler.
Bu nedenle zaman veya olay tabanlı çalışan, kendi execution geçmişini tutabilen yerel bir scheduler katmanı (Automation) kurulmuştur.

Önemli ayrım: Bu katman canlı konfigürasyonu kendi kendine karar verip değiştiren bir AI brain (beyin) değildir. Bu, salt önceden tanımlanmış `JobDefinition` ve `WorkflowDefinition` nesnelerini güvenlik kapılarından (gates) geçirerek işleten bir orchestration (orkestrasyon) motorudur.

## Bileşen Zinciri
`JobDefinition -> Trigger -> Preconditions -> JobRun -> WorkflowRun -> History`

- **Job**: Tekil bir çalışma birimi.
- **Workflow**: Aralarında dependency (DAG) tanımlanmış çoklu job dizisi.
- **Preconditions**: İşin başlamadan önce quiet hours, maintenance, incident gibi filtrelerden geçmesi.
- **History**: Tamamlanan işin `RunHistory` olarak loglanması.

## Safety Gates'in Yerini Almaz
Automation katmanı, `PreconditionChecker` yapıları sayesinde ops ve governance katmanlarındaki "Maintenance" (Bakım) veya "Incident" (Olay) flag'lerine saygı duyar.
Hiçbir güvenlik duvarı otomasyon var diye bypass edilemez. Live-affecting (canlıyı etkileyen) bir job'un precondition'ı "fail" verirse, job durdurulur (`DEFER` veya `BLOCK`).
