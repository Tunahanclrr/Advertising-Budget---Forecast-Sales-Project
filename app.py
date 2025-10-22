import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Modeli ve scaler'ı yükle
@st.cache_resource
def load_model():
    with open('ridge_model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    return model, scaler

# Model ve scaler'ı yükle
model, scaler = load_model()

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