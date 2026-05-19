# Learning Integrity, Readiness, Constitution, Policy ve Assurance Entegrasyonu

## 1. Learning Integrity Domain
Learning Plane, diğer sistemlere bir güvenilirlik ölçütü sunar.
- **Learning Trust Verdict**: Bir öğrenmenin ne kadar geçerli, kanıtlanmış ve benimsenmiş olduğunu gösterir. `TRUSTED`, `CAUTION`, `DEGRADED`, `BLOCKED`, `REVIEW_REQUIRED` seviyelerinden oluşur.

## 2. Entegrasyon Noktaları

### Readiness Board
- Readiness Bundle'ları değerlendirilirken yeni bir alan olarak `learning_integrity` eklenir.
- Aynı hata sınıfında tekrar (recurrence) varsa veya sahipsiz/doğrulanmamış kritik dersler (buried lessons) mevcutsa, Readiness kararı `blocked` veya `caution` olur.

### Constitution & Policy Plane
- Learning Plane'den çıkan Constitutional ve Policy hedefleri, bu katmanlardaki kural değişikliklerini tetiklemelidir.
- Tekrarlanan "deny" veya "review_required" kararları, Policy Plane'den bir sinyal olarak Learning Plane'e aktarılır ve kural seti güncellenir.

### Assurance Plane
- Tekrar eden kontrol başarısızlıkları (failed controls) veya zayıf kanıt kalıpları, Learning Plane'de bir "Assurance Weakness" sinyali oluşturur ve operasyonel modelin iyileştirilmesini zorunlu kılar.

### State & Change Plane
- State split-brain durumları veya Change Plan'deki exception override istismarları doğrudan Learning Plane'e raporlanır.

## 3. Evidence Graph ve Review Packs
- Tüm öğrenme nesneleri (signal, finding, lesson, validation vb.) Evidence Graph'ta ilişkisel olarak tutulur.
- İnsan denetimi (Human Review Fabric) gerektiğinde, Learning Plane "Learning Integrity Review Pack"ler üreterek denetimi kolaylaştırır ve kanıta dayalı hale getirir.
