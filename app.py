import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open('model.pkl', 'rb'))

st.title("🏦 Loan Approval Prediction System")
st.write("Enter applicant details to predict if the loan will be Approved or Rejected")

# User input
no_of_dependents = st.number_input("Number of Dependents", 0, 10, 0)
income_annum = st.number_input("Annual Income (in $)", 0, 1000000, 50000)
loan_amount = st.number_input("Loan Amount (in $)", 0, 1000000, 10000)
loan_term = st.number_input("Loan Term (months)", 6, 360, 360)
cibil_score = st.number_input("CIBIL Score", 300, 900, 700)
residential_assets_value = st.number_input("Residential Assets Value", 0, 1000000, 50000)
commercial_assets_value = st.number_input("Commercial Assets Value", 0, 1000000, 20000)
luxury_assets_value = st.number_input("Luxury Assets Value", 0, 1000000, 10000)
bank_asset_value = st.number_input("Bank Assets Value", 0, 1000000, 15000)

education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])

# Encoding
education_map = {"Graduate":1, "Not Graduate":0}
self_employed_map = {"Yes":1, "No":0}

education = education_map[education]
self_employed = self_employed_map[self_employed]

# Predict button
if st.button("Predict Loan Status"):
    features = np.array([[no_of_dependents, education, self_employed, income_annum, loan_amount,
                          loan_term, cibil_score, residential_assets_value,
                          commercial_assets_value, luxury_assets_value, bank_asset_value]])
    prediction = model.predict(features)
    result = "Approved" if prediction[0]==1 else "Rejected"
    st.success(f"The loan is likely to be: {result}")