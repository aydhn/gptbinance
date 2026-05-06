# Evidence Graph ve Queryable Governance Memory Mimarisi

Bu doküman, Phase 55 kapsamında geliştirilen kanıt grafı (evidence graph) ve yönetişim belleği (governance memory) mimarisini tanımlar.

## Temel Felsefe
Sistem olgunlaştıkça kararlar (readiness board memo'lar, incident raporları, postmortem'ler vb.) çeşitli alanlara yayılır. Kararların hangi kanıtlara dayandığını, hangi olay zincirinin bir düzeltmeye yol açtığını sorgulamak zorlaşır. Evidence Graph, tüm bu bağımsız artefact'ları açık, tipli (typed) bir ilişki grafı içinde birleştirir.

**Önemli Kurallar:**
- **Serbest Yorum Yok (No Hallucination):** Graf yalnızca açıkça belirtilmiş tipli ilişkileri içerir. Metin madenciliği veya tahmine dayalı yapılar kullanılmaz.
- **Değişmezlik (Immutability):** Kaynak artefact'lar graf işlemleri tarafından değiştirilmez. Sadece referanslar (immutable ref) indekslenir.
- **Kapsam ve Kısıtlama (Scope & Redaction):** Kapsam dışı veya yetkisiz erişimler engellenir veya veriler (redaction notes ile birlikte) filtrelenir. Sessizce gizleme yapılmaz.

## Mimari Bileşenler

### 1. Artefact Registry (`artefacts.py`)
Tüm önemli çıktıların (policy decisions, readiness memos, incidents, vs.) değişmez referanslarla indekslendiği merkezi kayıt defteri. Her kayıt (`ArtefactRecord`), ait olduğu kapsam, etki alanı, ve orijinal verinin değişmez özetini (`immutable_hash`) tutar.

### 2. Typed Relations (`relations.py`)
Artefact'lar arası ilişkileri tanımlar. İlişkiler tiplidir (örn. `DERIVED_FROM`, `INVALIDATED_BY`, `FOLLOWS_INCIDENT`). İzin verilen artefact çiftleri arasındaki ilişkiler katı kurallarla doğrulanır.

### 3. Lineage ve Dependency Traversal (`lineage.py`, `dependencies.py`)
- **Lineage Traversal:** Bir karardan geriye doğru giderek kaynak kanıtları ("Neden bu karar alındı?") bulur.
- **Dependency Traversal:** Bir kanıttan ileriye giderek ondan etkilenen kararları ("Bu veri eskiyse kim etkilenir?") bulur.

### 4. Case Files ve Evidence Packs (`cases.py`, `packs.py`)
- **Case Files:** Belirli bir durum (ör. `incident_case`) için zincirleme kanıtları, olay sıralamasını ve eksik bilgileri yapısal olarak derleyen otomatik dosyalar.
- **Evidence Packs:** Yönetişim kurulu veya olay incelemesi (ör. `board_review_pack`) için oluşturulan, kanıtların ve ilişkilerin taşınabilir paketleri.

### 5. Queries, Scopes ve Redactions (`queries.py`, `scopes.py`, `redaction.py`)
Verilerin sembol, profil veya aday ID gibi belirli filtrelere göre doğru kapsamda (scope) ve izinler dahilinde sorgulanmasını sağlar. Kısıtlı erişimli veri silinmez, açıkça sansürlenmiş (redacted) olarak işaretlenir.

### 6. Graph Gaps ve History (`gaps.py`, `history.py`)
Bağlantısı kopmuş (dangling) artefact'ları veya geçmişteki belirli bir andaki graf durumunu analiz ederek denetlenebilirliği artırır.
