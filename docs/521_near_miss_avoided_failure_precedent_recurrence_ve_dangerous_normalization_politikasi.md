# Near Miss, Avoided Failure, Precedent, Recurrence ve Dangerous Normalization Politikası

## 1. Near Misses ve Avoided Failures
Öğrenme sadece bir şeyler patladığında gerçekleşmez.
- **Near Miss**: Kıl payı atlatılan olaylar, başarı olarak değil, sistemin şansı olarak ele alınır ve aynı ciddiyetle analiz edilir.
- **Avoided Failure**: Bir koruyucu guard'ın devreye girmesiyle veya başarılı bir rollback ile atlatılan durumlar. Bu başarılar, koruma mekanizmalarını doğrular ve öğretici değer taşır.

## 2. Recurrence (Tekrarlama)
Aynı başarısızlık sınıfının (`FailureClass`) tekrar etmesi, sistemdeki öğrenme süreçlerinin başarısız olduğunun en büyük kanıtıdır.
- Eğer bir hata tekrar ediyorsa, önceki öğrenme nesnesinin Trust Verdict'i `BLOCKED` veya `DEGRADED` konumuna düşer.
- Tekrarlama, Learning Plane tarafından aktif olarak takip edilir ve Readiness Board gibi diğer sistemlere bir blocker olarak yansır.

## 3. Dangerous Precedents
Alınan istisnai kararlar (waiver'lar, emergency override'lar) sisteme bir "precedent" (emsal) olarak işlenir.
- Eğer bu emsaller bir alışkanlığa dönüşürse (override abuse), bu durum tehlikeli bir norm oluşturur.
- Learning Plane, bu tehlikeli emsalleri takip eder ve anayasayı (constitution) veya kuralları (policy) bu normatif bozulmaya karşı uyarır veya güncelletir.

## 4. Workaround Normalization
Geçici çözümlerin (workaround) kalıcı hale gelmesi ve standart işlemmiş gibi kabul edilmesi kesinlikle yasaktır.
- Tekrar eden workaround'lar zayıf bir sinyal olarak toplanır ve kalıcı bir hardening lesson çıkarılmasını zorunlu kılar.
