# 1 Good(Lower Risk)  0 Bad(Higher Risk)
import streamlit as st
import pandas as pd
import joblib

model = joblib.load("extra_trees_credit_model.pkl")
encoder = {col: joblib.load(f"{col}_encoder.pkl") for col in ['Sex','Housing','Saving accounts','Checking account']}

st.title("Credit Risk Prediction App")
st.write("Enter the Applicant info to predict if the credit risk is Good (Lower Risk) or Bad (Higher Risk)")
age = st.number_input("Age", min_value=18, max_value=80, value=30)
sex = st.selectbox("Sex",["male","female"])
job = st.number_input("Job (0-3)", min_value=0, max_value=3, value=1)
housing = st.selectbox("Housing",["own","free","rent"])
saving_accounts = st.selectbox("Saving accounts",["little","moderate","rich","quite rich"])
checking_account = st.selectbox("Checking account",["little","moderate","rich"])
credit_amount = st.number_input("Credit Amount", min_value=0, max_value=20000, value=1000)
duration = st.number_input("Duration (in months)", min_value=4, value=12)

input_data = pd.DataFrame({
    'Age':[age],
    "Sex":[encoder["Sex"].transform([sex])[0]],
    "Job":[job],
    "Housing":[encoder["Housing"].transform([housing])[0]],
    "Saving accounts":[encoder["Saving accounts"].transform([saving_accounts])[0]],
    "Checking account":[encoder["Checking account"].transform([checking_account])[0]],
    "Credit amount":[credit_amount],
    "Duration":[duration]
})

if st.button("Predict Risk"):
    pred = model.predict(input_data)[0]

    if pred ==1:
        st.success("The predicted credit risk: **GOOD**")

    else:
        st.error("The predicted credit risk: **BAD**")