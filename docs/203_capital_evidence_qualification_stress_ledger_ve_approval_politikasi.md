# Capital Evidence, Qualification, Stress, Ledger ve Approval Politikası

## Evidence Bundle
Escalation kararı verilebilmesi için gereken kanıtlar bohçasıdır. Bir tier artırımı için şu kanıtlara bakılır:
- `qualification_pass`: Profile onaylı mı?
- `ledger_clean`: Reconciliation başarılı mı? (Unexplained delta var mı?)
- `stress_pass`: Tail-risk senaryolarından geçildi mi?
- `observability_clean`: Son dönemde kritik hata üretildi mi?
- `performance_acceptable`: İşlem sayısına ve slippage miktarına göre sistem başarılı mı?

## Stale Evidence (Bayat Kanıt)
Yukarıdaki kanıtların hepsi tamam olsa dahi, eğer 60 dakikadan (yapılandırmaya bağlı) eskiyseler, Capital Governance katmanı bu kanıtları reddeder (`EvidenceFreshness.STALE`). Gerçek sermaye artırımı, ancak en güncel sağlık raporlarıyla yapılabilir.

## Escalation Blockers
Herhangi bir kanıt eksikse veya `stale` ise, sistem "Escalation Blocked" tavsiyesi oluşturur ve bir üst tier'a geçişe izin vermez.
