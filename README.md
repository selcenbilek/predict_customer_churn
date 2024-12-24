# predict_customer_churn
Müşteri Kaybı Tahmini Projesi 

Projenin Amacı
Bu proje, makine öğrenimi tekniklerini kullanarak müşteri kaybını (churn) tahmin etmeyi amaçlamaktadır. Müşterilerin neden şirketimizi terk etmeyi düşündüklerini anlamak ve bu ayrılıkları önlemek için proaktif adımlar atmak, işletmeler için büyük önem taşır. Bu proje sayesinde, müşteri kaybına yol açabilecek faktörleri belirleyerek, hedefli pazarlama kampanyaları ve müşteri deneyimi iyileştirme stratejileri geliştirmek mümkün olacaktır.

Kullanılan Teknolojiler
**Python: Projenin temel programlama dili olarak kullanılmıştır. Veri analizi, modelleme ve görselleştirme işlemleri Python'un güçlü kütüphaneleri sayesinde gerçekleştirilmiştir.
**Pandas: Veri manipülasyonu ve analizinde en popüler Python kütüphanelerinden biridir. Veri temizleme, özellik mühendisliği ve veri çerçeveleriyle çalışma gibi işlemlerde kullanılmıştır.
**NumPy: Nümerik hesaplamalar için kullanılan temel bir kütüphanedir. Özellikle matematiksel işlemler ve büyük boyutlu dizilerle çalışmak için kullanılır.
**Scikit-learn: Makine öğrenimi algoritmalarının uygulanması için kapsamlı bir kütüphanedir. Sınıflandırma, regresyon, kümeleme gibi birçok algoritma içerir. Bu projede, müşteri kaybını tahmin etmek için bir sınıflandırma algoritması kullanılacaktır.
**Matplotlib ve Seaborn: Verileri görselleştirmek için kullanılan kütüphanelerdir. Modelin performansını değerlendirmek ve verileri analiz etmek için çeşitli grafikler oluşturmak için kullanılır.

Proje Adımları

**Veri Toplama ve Hazırlama:
Müşteri verilerinin toplanması (örneğin, demografik bilgiler, satın alma geçmişi, müşteri hizmetleri etkileşimleri).
Verilerin temizlenmesi ve düzenlenmesi (eksik değerlerin doldurulması, veri tiplerinin dönüştürülmesi).
Özellik mühendisliği: Yeni özellikler oluşturarak modelin performansını artırma (örneğin, satın alma sıklığı, ortalama sipariş değeri).

**Veri Analizi:
Verilerin keşfedici bir analizi yapılması (veri görselleştirme, istatistiksel analiz).
Müşteri kaybına etki eden önemli faktörlerin belirlenmesi.
Verilerin eğitim ve test setlerine ayrılması.
Modelleme:

**Uygun bir makine öğrenimi algoritmasının seçilmesi (örneğin, Lojistik Regresyon, Destek Vektör Makineleri, Random Forest).
Modelin eğitim verileri üzerinde eğitilmesi.
Modelin performansının test verileri üzerinde değerlendirilmesi (confusion matrix, classification report, ROC eğrisi gibi metrikler).
Modelin Değerlendirilmesi ve İyileştirilmesi:

**Modelin performansının farklı metrikler kullanılarak değerlendirilmesi.
Modelin karmaşıklığı ve aşırı öğrenme (overfitting) gibi sorunların kontrol edilmesi.
Hiperparametre optimizasyonu ile modelin performansının artırılması.
Sonuçların Yorumlanması ve Eyleme Geçirme:

**Modelin tahminlerine göre müşteri kaybı riskini yüksek olan müşterilerin belirlenmesi.
Bu müşterilere yönelik hedefli pazarlama kampanyaları ve müşteri deneyimi iyileştirme stratejileri geliştirilmesi.
Modelin düzenli olarak güncellenmesi ve yeniden eğitilmesi.

**Ek Notlar:

Proje için hazırlanan ara yüzün erişim linki: https://predictcustomerchurn-model.streamlit.app/

Data kaynağı :https://thecleverprogrammer.com/2020/05/26/predict-customer-churn-with-python-and-machine-learning/#google_vignett












