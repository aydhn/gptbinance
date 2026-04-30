# Meta-Labeling, Label Tasarımı ve Zaman Sırası Disiplini

Label tasarımı, hedeflenen elde tutma süresine (horizon) ve sinyal üretim anındaki referans fiyata dayanır.
Veri sızıntısını (leakage) önlemek için etiketlerin, yalnızca ilgili strateji niyetinin gelecekteki gerçekleşmesine bakması şarttır.
Rastgele `train_test_split` yasaktır, zaman sıralı `anchored` veya `expanding` pencereler kullanılmalıdır.
