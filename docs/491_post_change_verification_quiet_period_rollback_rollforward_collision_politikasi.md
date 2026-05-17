# Post-change Verification, Quiet Period, Rollback, Rollforward, Collision Politikası

- **Post-Change Verification:**
  Her uygun sınıf değişikliğin sonrasında, doğrulanması gerekir. Değiştiği için "verified" sayılmaz.

- **Quiet Period:**
  Değişiklik yapıldıktan sonra sistemin stabilitesini gözlemlemek için belirli bir sessiz döneme (quiet period) ihtiyaç vardır.

- **Rollback vs Rollforward:**
  Her major değişikliğin, uygulanabilir bir "tested ready" rollback planı olmalıdır. Sadece niyet olan bir plan yetersizdir. Rollforward stratejisi de gerektiğinde değerlendirilmeli ama "nasılsa ileri sararız" mantığı (forced optimism) yasaktır.

- **Collision Handling:**
  Aynı window içerisinde çakışan değişiklikler (overlapping windows, operator-load collisions) görünür kılınır ve trust'ı düşürür.

- **Blast Radius:**
  Her değişikliğin çapı bilinmeli, belirsiz (unknown) çapta olanlar güven (trust) notunu düşürmeli/bloklamalıdır.
