import streamlit as st
import numpy as np
import pickle

# Load trained model
with open("model.pkl", "rb") as p:
    model = pickle.load(p)

st.title("Heart Disease Prediction")
st.write("Please enter required values to predict heart disease")

# Input fields
age = st.number_input("Enter age", min_value=0, max_value=120, step=1)

sex = st.selectbox("Sex", ("Male", "Female"))
sex = 1 if sex == "Male" else 0

cp = st.selectbox("Chest pain type", ["typical", "atypical", "non-anginal"])
cp_typical = 1 if cp == "typical" else 0
cp_atypical = 1 if cp == "atypical" else 0
cp_non_anginal = 1 if cp == "non-anginal" else 0

trestbps = st.number_input("Enter resting blood pressure", min_value=0)

chol = st.number_input("Enter cholesterol", min_value=0)

fbs = st.selectbox("Fasting blood sugar > 120 mg/dl", ("Yes", "No"))
fbs = 1 if fbs == "Yes" else 0

restecg = st.selectbox("Resting ECG", ["normal", "ST abnormality"])
restecg_normal = 1 if restecg == "normal" else 0
restecg_abnormality = 1 if restecg == "ST abnormality" else 0

thalach = st.number_input("Enter max heart rate achieved", min_value=0)

exang = st.selectbox("Exercise induced angina", ("Yes", "No"))
exang = 1 if exang == "Yes" else 0

oldpeak = st.number_input("Enter oldpeak", format="%.2f")

slope = st.selectbox("Slope of peak exercise ST segment", ["flat", "upsloping"])
slope_flat = 1 if slope == "flat" else 0
slope_upsloping = 1 if slope == "upsloping" else 0

thal = st.selectbox("Thalassemia", ["normal", "reversible defect"])
thal_normal = 1 if thal == "normal" else 0
thal_reversible = 1 if thal == "reversible defect" else 0

# Final input array
features = np.array([
    age, trestbps, chol, thalach, oldpeak,
    sex, fbs, exang,
    cp_typical, cp_atypical, cp_non_anginal,
    restecg_normal, restecg_abnormality,
    slope_flat, slope_upsloping,
    thal_normal, thal_reversible
]).reshape(1, -1)

# Predict button
if st.button("Predict"):
    
    result = model.predict(features)[0]
    if result == 1:
        st.error("⚠️Person is likely to have heart disease.")
    else:
        st.success("✅Person is unlikely to have heart disease.")