import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler

# Veriyi yükle ve modeli eğit
@st.cache_resource
def load_and_train_model():
    # Veriyi oku
    df = pd.read_csv('Advertising Budget and Sales.csv')
    df = df.drop("Unnamed: 0", axis=1)
    
    # Veriyi hazırla
    X = df[["TV Ad Budget ($)","Radio Ad Budget ($)","Newspaper Ad Budget ($)"]]
    y = df["Sales ($)"]
    
    # Scaler oluştur ve uygula
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Ridge modelini eğit
    model = Ridge()
    model.fit(X_scaled, y)
    
    return model, scaler

# Model ve scaler'ı yükle
model, scaler = load_and_train_model()

# Sayfa konfigürasyonu
st.set_page_config(
    page_title="advertising budgeti - sales guess",
    layout="centered"
)

# Başlık
st.title("💰 Forecast Sales with Advertising Budget")
st.write("Enter your advertising budgets and learn your estimated sales figures!")

# Veriyi yükle ve modeli eğit
@st.cache_data
def predict_sales(tv, radio, newspaper):
    # Veriyi uygun formata dönüştür
    X_new = np.array([[tv, radio, newspaper]])
    
    # Veriyi ölçeklendir
    X_new_scaled = scaler.transform(X_new)
    
    # Tahmin yap
    prediction = model.predict(X_new_scaled)
    
    return prediction[0]

# Model ve scaler'ı yükle
model, scaler = load_and_train_model()

# Input alanları
st.write("### 📊 📊 Enter Advertising Budgets")

tv_budget = st.number_input(
    "📺 TV Advertising Budget ($)",
    min_value=0,
    max_value=300,
    value=150
)

radio_budget = st.number_input(
    "📻 Radio Advertising Budget ($)",
    min_value=0,
    max_value=100,
    value=50
)

newspaper_budget = st.number_input(
    "📰 Newspaper Advertising Budget ($)",
    min_value=0,
    max_value=100,
    value=30
)

# Tahmin fonksiyonu
def predict_sales(tv, radio, newspaper):
    # Veriyi uygun formata dönüştür
    X_new = np.array([[tv, radio, newspaper]])
    
    # Veriyi ölçeklendir
    X_new_scaled = scaler.transform(X_new)
    
    # Tahmin yap
    prediction = model.predict(X_new_scaled)
    
    return prediction[0]

# Tahmin butonu
if st.button("🎯Make a Sales Forecast", type="primary"):
    # Tahmin yap
    predicted_sales = predict_sales(tv_budget, radio_budget, newspaper_budget)
    
    st.markdown("---")
    st.write("### 💵 Estimated Sales")
    st.success(f"With the advertising budgets you enter **${predicted_sales:,.2f}** you are expected to sell.")
    
    # Toplam bütçeyi göster
    total_budget = tv_budget + radio_budget + newspaper_budget
    st.info(f"Total Advertising Budget: ${total_budget:,.2f}")