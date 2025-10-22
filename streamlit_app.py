import streamlit as st
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler

# Sayfa konfigürasyonu
st.set_page_config(
    page_title="Reklam Bütçesi - Satış Tahmini",
    layout="centered"
)

# Başlık
st.title("💰 Reklam Bütçesi ile Satış Tahmini")
st.write("Reklam bütçelerinizi girin, tahmini satış rakamını öğrenin!")

# Model ve veri hazırlama
@st.cache_resource
def create_model():
    # Örnek veri
    X = np.array([
        [230.1, 37.8, 69.2],
        [44.5, 39.3, 45.1],
        [17.2, 45.9, 69.3],
        [151.5, 41.3, 58.5],
        [180.8, 10.8, 58.4],
    ])
    y = np.array([22.1, 10.4, 9.3, 18.5, 12.9])
    
    # Scaler
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Model
    model = Ridge()
    model.fit(X_scaled, y)
    
    return model, scaler

# Model ve scaler'ı yükle
model, scaler = create_model()

# Input alanları
st.write("### 📊 Reklam Bütçelerini Girin")

tv_budget = st.number_input(
    "📺 TV Reklam Bütçesi ($)",
    min_value=0,
    max_value=300,
    value=150
)

radio_budget = st.number_input(
    "📻 Radio Reklam Bütçesi ($)",
    min_value=0,
    max_value=100,
    value=50
)

newspaper_budget = st.number_input(
    "📰 Gazete Reklam Bütçesi ($)",
    min_value=0,
    max_value=100,
    value=30
)

# Tahmin fonksiyonu
def predict_sales(tv, radio, newspaper):
    X_new = np.array([[tv, radio, newspaper]])
    X_new_scaled = scaler.transform(X_new)
    return model.predict(X_new_scaled)[0]

# Tahmin butonu
if st.button("🎯 Satış Tahmini Yap", type="primary"):
    predicted_sales = predict_sales(tv_budget, radio_budget, newspaper_budget)
    
    st.markdown("---")
    st.write("### 💵 Tahmini Satış")
    st.success(f"Girdiğiniz reklam bütçeleri ile **${predicted_sales:,.2f}** satış yapmanız bekleniyor.")
    
    total_budget = tv_budget + radio_budget + newspaper_budget
    st.info(f"Toplam Reklam Bütçesi: ${total_budget:,.2f}")