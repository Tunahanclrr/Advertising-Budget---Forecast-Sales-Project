import streamlit as st
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler

# Page configuration
st.set_page_config(
    page_title="Advertising Budget - Sales Prediction",
    layout="centered"
)

# Title
st.title("💰 Advertising Budget Sales Predictor")
st.write("Enter your advertising budgets to predict potential sales!")

# Model and data preparation
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

# Input areas
st.write("### 📊 Enter Advertising Budgets")

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
    X_new = np.array([[tv, radio, newspaper]])
    X_new_scaled = scaler.transform(X_new)
    return model.predict(X_new_scaled)[0]

# Prediction button
if st.button("🎯 Make Sales Prediction", type="primary"):
    predicted_sales = predict_sales(tv_budget, radio_budget, newspaper_budget)
    
    st.markdown("---")
    st.write("### 💵 Predicted Sales")
    st.success(f"With your advertising budgets, expected sales are **${predicted_sales:,.2f}**")
    
    total_budget = tv_budget + radio_budget + newspaper_budget
    st.info(f"Total Advertising Budget: ${total_budget:,.2f}")