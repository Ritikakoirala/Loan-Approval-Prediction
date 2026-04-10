# Loan Approval Prediction System

## Project Overview
This project is a **Loan Approval Prediction System** built using **Random forest** and **Logistic Regression**.  
The goal is to predict whether a loan application will be **Approved** or **Rejected** based on applicant features like income, assets, CIBIL score, education, and employment status.

This project includes:
- Data cleaning and preprocessing
- Feature encoding and scaling
- Model training and evaluation using Logistic Regression
- A demo-approved case prediction
- Saving the model and scaler for deployment
## Dataset
- **File:** `loan_dataset.csv`  
- **Rows:** 4269  
- **Features:** 
  1. `loan_id` - Unique identifier for the loan  
  2. `no_of_dependents` - Number of dependents  
  3. `education` - Applicant's education (Graduate / Not Graduate)  
  4. `self_employed` - Self employed? (Yes / No)  
  5. `income_annum` - Annual income ($)  
  6. `loan_amount` - Requested loan amount ($)  
  7. `loan_term` - Loan term (months)  
  8. `cibil_score` - Credit score  
  9. `residential_assets_value` - Value of residential assets  
  10. `commercial_assets_value` - Value of commercial assets  
  11. `luxury_assets_value` - Value of luxury assets  
  12. `bank_asset_value` - Value of bank assets  
  13. `loan_status` - Target variable (Approved / Rejected)

---

## Project Steps

1. **Data Preprocessing**
   - Handle missing values (if any)
   - Encode categorical variables (`education`, `self_employed`, `loan_status`) using `LabelEncoder`
   - Split data into features (`X`) and target (`y`)

2. **Feature Scaling**
   - Standardized numerical features using `StandardScaler` to improve Logistic Regression performance

3. **Model Training**
   - Used **Logistic Regression** as the classifier
   - Split data into training and testing sets
   - Trained the model on scaled features

4. **Model Evaluation**
   - Metrics used: Accuracy, Precision, Recall, F1-score
   - Evaluated predictions on test data

5. **Model Saving**
   - Saved the trained model and scaler using `pickle` for later deployment

6. **Demo Prediction**
   - Provided a pre-filled approved case from the dataset to demonstrate model prediction
   - Shows **loan approval probability** and final decision (Approved / Rejected)
ibraries Used
pandas
numpy
scikit-learn
pickle
streamlit (for web deployment)
Demo Approved Case
Feature	Value
Education	Graduate
Self Employed	Yes
Income	2,900,000
Loan Amount	11,200,000
No of Dependents	2
CIBIL Score	547
Residential Assets	8,100,000
Commercial Assets	4,700,000
Luxury Assets	9,500,000
Bank Assets	3,100,000
Loan Status	Approved
Prediction Output:
Loan Approval Probability: ~95%
Decision: Approved ✅


