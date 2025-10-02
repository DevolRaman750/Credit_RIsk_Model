# 🏦 Credit Risk Prediction App

## Overview
Credit risk refers to the possibility that a borrower may fail to repay a loan or meet contractual obligations. Banks and financial institutions assess **credit scores** and other personal/financial factors to predict whether lending to a person is a **good (low risk)** or **bad (high risk)** decision.

This project demonstrates a **Credit Risk Prediction System** built using **Machine Learning & Streamlit**, using the **German Credit Risk Dataset (Kaggle)** to predict credit risk.

The project showcases the **end-to-end Data Science pipeline**:  
1. Data Analysis & Visualization  
2. Data Cleaning & Feature Engineering  
3. Model Training & Evaluation  
4. Deployment as a Web App with Streamlit  

---

## Why Credit Risk Prediction is Important
- Financial institutions lose billions annually due to **loan defaults**.  
- Credit risk scoring helps lenders:  
  - Reduce **default losses**  
  - Approve loans faster  
  - Ensure **financial stability**  
  - Improve decision-making with **data-driven insights**  

**For FinTech companies**, a reliable credit risk predictor is essential to:  
- Automate loan approval systems  
- Detect risky customers early  
- Offer customized interest rates  
- Scale financial products securely  

---

## Project Workflow
1. **Data Acquisition**  
   - Dataset: [German Credit Risk Data (Kaggle)](https://www.kaggle.com/)  

2. **Exploratory Data Analysis (EDA)**  
   - Visualizations using **Matplotlib & Seaborn**  
   - Distribution analysis of categorical & numerical features  

3. **Data Cleaning & Feature Engineering**  
   - Handling missing values  
   - Label encoding categorical variables  
   - Feature selection  

4. **Model Training**  
   - Trained multiple models: Logistic Regression, XGBoost, RandomForest, ExtraTrees  
   - Selected **ExtraTreesClassifier** as final model (best accuracy & stability)  
   - Saved model as `extra_trees_credit_model.pkl`  

5. **Web Application (Deployment)**  
   - Built interactive UI with **Streamlit**  
   - Users can input applicant data and get instant prediction  
   - Prediction Output:  
     - ✅ **GOOD (Low Risk)**  
     - ❌ **BAD (High Risk)**  

---

## Tech Stack
- **Python**  
- **Libraries**:  
  - `scikit-learn` → Model training  
  - `xgboost` → Boosting model comparison  
  - `pandas`, `numpy` → Data handling  
  - `matplotlib`, `seaborn` → Visualization  
  - `joblib` → Save & load trained models  
  - `streamlit` → Web application  
- **Dataset**: German Credit Data (Kaggle)  

---


        
---

## How to Run the App

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/DevolRaman750/Credit_RIsk_Model.git
cd Credit_Risk_Prediction
     # Project Documentation
pip install pandas numpy scikit-learn xgboost matplotlib seaborn streamlit joblib
streamlit run App.py
4️⃣ Open in Browser

Local URL: http://localhost:8501

Network URL: Shown in terminal
Contact

👤 Raman Tripathi
📩 Email: ramantripathi0707@gmail.com
