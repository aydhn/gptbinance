# Scope, Redaction ve Graph Gap Politikası

Bu doküman, evidence graph üzerindeki kapsam (scope) kontrollerini, veri gizlemeyi (redaction) ve eksik ilişkilerin (gaps) nasıl yönetildiğini tanımlar.

## Kapsam Sınırları (Scope Enforcement)
Her sorgu ve artefact belirli bir kapsama (Workspace, Profile, Symbol, Session) aittir. Sistem, yanlış kapsamda (wrong-scope) yapılan aramaları genişletmez, reddeder.

## Gizleme Kuralları (Redaction Policy)
Bazı kanıtların (restricted evidence) belirli kullanıcılara veya süreçlere gösterilmesi yasak olabilir.
- **Sessizce Gizleme Yasaktır (No Silent Omission):** Eğer bir veri saklanıyorsa, listeden tamamen çıkarılmaz. Bunun yerine, "RedactionRecord" ile açıkça gizlendiği (sansürlendiği) sebebiyle birlikte belirtilir.
- Bu yaklaşım, eksik verinin sistem arızası mı yoksa erişim kısıtlaması mı olduğunu netleştirir.

## Graf Boşlukları (Graph Gaps)
Bağlantısı kopan veya kaynak verisi eksik olan ilişkiler "Graph Gap" olarak tanımlanır. `GapDetector`, bu tür kopuklukları tarayarak uyarır (INFO, WARNING, CRITICAL).
