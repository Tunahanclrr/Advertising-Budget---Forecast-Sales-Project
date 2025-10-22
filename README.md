# Reklam Bütçesi - Satış Tahmini Projesi

## Proje Hakkında
Bu proje, farklı reklam kanallarına (TV, Radyo, Gazete) yapılan yatırımların satışlar üzerindeki etkisini analiz eden ve gelecekteki satışları tahmin eden bir makine öğrenmesi uygulamasıdır.

## Problemin Tanımı
Şirketler reklam bütçelerini farklı medya kanalları arasında nasıl dağıtacakları konusunda zorlanmaktadır. Bu proje:
- Hangi reklam kanalının satışlar üzerinde daha etkili olduğunu belirlemeyi
- Belirli bir reklam bütçesi dağılımı ile elde edilebilecek potansiyel satışları tahmin etmeyi
- Reklam yatırımlarının geri dönüşünü optimize etmeyi hedeflemektedir

## Veri Seti
Veri seti şunları içermektedir:
- TV Reklam Bütçesi ($)
- Radyo Reklam Bütçesi ($)
- Gazete Reklam Bütçesi ($)
- Satışlar ($)

## Metodoloji ve Kullanılan Teknolojiler
1. **Veri Analizi ve Görselleştirme**
   - Pandas ve NumPy: Veri manipülasyonu
   - Seaborn ve Matplotlib: Veri görselleştirme
   - Korelasyon analizi ve dağılım grafikleri

2. **Model Geliştirme**
   - Sklearn: Makine öğrenmesi modelleri
   - Farklı regresyon modellerinin karşılaştırılması
   - Cross-validation ve model değerlendirme

3. **Arayüz Geliştirme**
   - Streamlit: Web tabanlı kullanıcı arayüzü
   - Interactive input ve anlık tahminler

## Neden Ridge Regresyon?
Ridge regresyon modelini seçmemizin nedenleri:

1. **Multicollinearity Yönetimi**: 
   - Reklam kanalları arasında yüksek korelasyon var
   - Ridge regresyon, bu durumu L2 regularization ile etkili şekilde yönetiyor

2. **Overfitting Kontrolü**: 
   - L2 regularization sayesinde modelin aşırı öğrenmesi engelleniyor
   - Daha genelleştirilebilir tahminler elde ediliyor

3. **Feature Importance**: 
   - Tüm özellikleri koruyarak her birinin etkisini uygun şekilde ağırlıklandırıyor
   - Özellik seçimi yapmak yerine özellik etkilerini düzenliyor

4. **Model Performansı**: 
   - En yüksek R² skoru Ridge modeli ile elde edildi
   - Tahminlerde daha tutarlı sonuçlar verdiği gözlemlendi

## Nasıl Kullanılır?
1. Streamlit uygulamasını başlatın: `streamlit run app.py`
2. Web arayüzünden reklam bütçelerini girin
3. "Satış Tahmini Yap" butonuna tıklayın
4. Tahmini satış rakamını görüntüleyin

## Gelecek Geliştirmeler
- Zaman serisi analizi eklenebilir
- Farklı sektörler için özelleştirilebilir
- Daha fazla reklam kanalı eklenebilir
- Mevsimsellik etkileri dahil edilebilir