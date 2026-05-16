# Commitment, Stage Funding, WIP Limits ve Zombie Initiative Politikası

## Commitment Levels
Her girişimin bir taahhüt sınıfı (investigated, prioritized, planned, funded, vb.) bulunur. Sahte taahhüt etiketleri önlenir.

## Stage Funding
Finansman aşamalıdır (discovery, pilot, canary, expansion, vb.). Tam bağlılık (full commitment) için kanıt gerekir.

## WIP Limits
Per-bucket ve per-team için Devam Eden İş (WIP) sınırları belirlidir. WIP limitlerinin aşılması sıkı bir şekilde izlenir ve durum (WIPClass.OVER_LIMIT) kaydedilir.

## Freeze / Kill / Defer
Bir girişim durdurulduğunda (frozen), iptal edildiğinde (killed) veya ertelendiğinde (deferred) gerekçeleriyle ve olası sona erme tarihleriyle kanıta bağlanır.

## Zombie Initiative Riskleri ve Neden Fake Commitment İstenmez
Hedefsiz ve sonsuz kaynak tüketen girişimler (zombie initiatives) otomatik algılanır. Sahte taahhütler, sistem kapasite ve bütçe kararlarında kör nokta oluşturacağı için reddedilir.
