import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load model files
@st.cache_resource
def load_model():
    model = joblib.load('model.pkl')
    scaler = joblib.load('scaler.pkl')
    feature_names = joblib.load('feature_names.pkl')
    return model, scaler, feature_names

model, scaler, feature_names = load_model()

st.title("🏥 Hospital Readmission Risk Predictor")
st.write("Enter patient details below to predict 30-day readmission risk")

# Input fields
age = st.slider("Age", 40, 100, 65)
time_in_hospital = st.slider("Days in Hospital", 1, 30, 5)
n_lab_procedures = st.number_input("Number of Lab Procedures", 0, 100, 20)
n_procedures = st.number_input("Number of Procedures", 0, 20, 1)
n_medications = st.number_input("Number of Medications", 0, 80, 10)
n_outpatient = st.number_input("Prior Outpatient Visits", 0, 20, 0)
n_inpatient = st.number_input("Prior Inpatient Visits", 0, 20, 1)
n_emergency = st.number_input("Prior Emergency Visits", 0, 20, 0)

if st.button("Predict Readmission Risk"):

    # Create a row of zeros for all 41 features
    input_dict = {col: 0 for col in feature_names}

    # Fill in the values user provided
    input_dict['age'] = age
    input_dict['time_in_hospital'] = time_in_hospital
    input_dict['n_lab_procedures'] = n_lab_procedures
    input_dict['n_procedures'] = n_procedures
    input_dict['n_medications'] = n_medications
    input_dict['n_outpatient'] = n_outpatient
    input_dict['n_inpatient'] = n_inpatient
    input_dict['n_emergency'] = n_emergency

    # Convert to dataframe with correct column order
    input_df = pd.DataFrame([input_dict])[feature_names]

    # Scale and predict
    input_scaled = scaler.transform(input_df)
    prob = model.predict_proba(input_scaled)[0][1]

    # Show result
    st.markdown("---")
    st.metric("Readmission Risk Score", f"{prob*100:.1f}%")

    if prob >= 0.6:
        st.error("⚠️ High Risk — Consider follow-up care and early intervention")
    elif prob >= 0.4:
        st.warning("🔔 Moderate Risk — Monitor patient closely after discharge")
    else:
        st.success("✅ Low Risk — Standard discharge process recommended")