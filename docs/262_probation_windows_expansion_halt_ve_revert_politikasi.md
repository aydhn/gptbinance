# Probation Windows, Expansion, Halt ve Revert Politikası

## Probation Nedir?
Probation (gözetim süresi), bir adayın (candidate) canlı veya paper ortama kontrollü şekilde dahil edildikten sonra geçmesi gereken test süresidir. Bu süre boyunca sistemin temel health metrikleri (Market Truth, Shadow Cleanliness, Lifecycle Orphans vb.) sürekli izlenir.

## Neden Otomatik Expansion Yok? (Why No Automatic Expansion)
Sistem "probation pass" olduğunda otomatik olarak bir sonraki faza geçmez. Bunun yerine "Expansion Recommendation" üretilir. Otoritenin, piyasa koşullarını ve macro riskleri gözeterek bu adımı bizzat atması (veya CLI üzerinden onaylaması) gerekir. Bu, kontrolü insanda (Human-in-the-Loop) tutar ve sessiz, riskli büyümeleri engeller.

## Halt Koşulları
Bir stage sırasında şu koşullar oluşursa anında Halt kararı önerilir:
1. Critical Market Truth Stale (Piyasa verisi geri kalması)
2. Unresolved Shadow Drift (Gölge ortam ile gerçek ortam uyumsuzluğu)
3. Lifecycle Orphan Spike (Takip edilemeyen emirlerin artması)
4. Capital Posture Breach (Beklenmedik sermaye aşımı/riski)

## Revert-to-Prior-Active-Set
Eğer bir aday başarısız olursa (Fail veya Halt), sistem derhal bir "Revert Plan" üretir. Bu plan, "Active-Set Registry" içinde tutulan bir önceki aktif konfigürasyon/aday versiyonuna (lineage) güvenli dönüşü sağlar. Gizli veya geçmişe dair audit trail bırakmayan geçişler kesinlikle yasaktır.
