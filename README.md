# Advertising Budget - Sales Prediction Project

## About Project
This project is a machine learning application that analyzes the impact of investments in different advertising channels (TV, Radio, Newspaper) on sales and predicts future sales.

[English](#advertising-budget---sales-prediction-project) | [Türkçe](#reklam-bütçesi---satış-tahmini-projesi)

## Problem Definition
Companies struggle with how to distribute their advertising budgets across different media channels. This project aims to:
- Determine which advertising channel is more effective on sales
- Predict potential sales with a specific advertising budget distribution
- Optimize return on advertising investments

## Dataset
The dataset includes:
- TV Advertising Budget ($)
- Radio Advertising Budget ($)
- Newspaper Advertising Budget ($)
- Sales ($)

## Methodology and Technologies Used
1. **Data Analysis and Visualization**
   - Pandas and NumPy: Data manipulation
   - Seaborn and Matplotlib: Data visualization
   - Correlation analysis and distribution plots

2. **Model Development**
   - Sklearn: Machine learning models
   - Comparison of different regression models
   - Cross-validation and model evaluation

3. **Interface Development**
   - Streamlit: Web-based user interface
   - Interactive input and real-time predictions

## Why Ridge Regression?
Reasons for choosing Ridge regression model:

1. **Multicollinearity Management**: 
   - High correlation between advertising channels
   - Ridge regression effectively manages this with L2 regularization

2. **Overfitting Control**: 
   - L2 regularization prevents model overfitting
   - More generalizable predictions are obtained

3. **Feature Importance**: 
   - Maintains all features while properly weighting their effects
   - Regulates feature effects instead of feature selection

4. **Model Performance**: 
   - Highest R² score achieved with Ridge model
   - More consistent results in predictions

## How to Use?
1. Start Streamlit application: `streamlit run app.py`
2. Enter advertising budgets via web interface
3. Click "Make Sales Prediction" button
4. View estimated sales figure

## Future Improvements
- Time series analysis can be added
- Can be customized for different sectors
- More advertising channels can be added
- Seasonality effects can be included

---

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