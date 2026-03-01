import streamlit as st
import joblib
import numpy as np

model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')
feature_names = joblib.load('feature_names.pkl')

st.title("🏥 Hospital Readmission Risk Predictor")
st.write("Enter patient details to predict 30-day readmission risk")

age = st.slider("Age", 40, 100, 65)
num_medications = st.number_input("Number of Medications", 0, 50, 10)
num_lab_procedures = st.number_input("Number of Lab Procedures", 0, 100, 20)
num_inpatient = st.number_input("Prior Inpatient Visits", 0, 20, 1)
time_in_hospital = st.slider("Days in Hospital", 1, 30, 5)

if st.button("Predict"):
    features = np.array([[age, num_medications, num_lab_procedures,
                          num_inpatient, time_in_hospital]])
    prob = model.predict_proba(features)[0][1]
    st.metric("Readmission Risk", f"{prob*100:.1f}%")
    if prob > 0.5:
        st.error("⚠️ High Risk — Consider follow-up care")
    else:
        st.success("✅ Low Risk")