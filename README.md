# 🏥 Hospital Readmission Prediction
*Can we predict which patients will return to the hospital within 30 days?*

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Live-App-red)
![Status](https://img.shields.io/badge/Status-Deployed-brightgreen)

## 🔴 [Try the Live App](https://hospitalreadmission-oymn8nfwarxdejjsm7xvrk.streamlit.app/)

---

## 💡 Why This Matters
Hospital readmissions cost the U.S. healthcare system **$26 billion annually**.
Early identification of high-risk patients allows providers to intervene 
before discharge — saving lives and reducing costs.

---

## 🔍 What I Did
- Analyzed **25,000 patient records** across 17 clinical features
- Built and compared Logistic Regression, Random Forest, and XGBoost
- Handled class imbalance using **SMOTE**
- Used **SHAP values** to explain which features drive readmission risk
- Deployed an interactive risk prediction tool using **Streamlit**

---

## 📊 Model Results
| Model | AUROC |
|-------|-------|
| **Logistic Regression ⭐** | **0.6429** |
| XGBoost | 0.6362 |
| Random Forest | 0.6274 |

> 🔑 Key Insight: Logistic Regression outperformed complex models —
> indicating that readmission risk follows largely linear patterns 
> in this dataset. Prior inpatient visits, time in hospital, and 
> number of medications were the strongest predictors.

---

## 🛠️ Tech Stack
`Python` `Pandas` `Scikit-learn` `XGBoost` `SHAP` `Streamlit` `Git`

---

## ▶️ Run Locally
```bash
git clone https://github.com/gkammidi-prog/hospital_readmission.git
pip install -r requirements.txt
python -m streamlit run app.py
```

---

## 👩‍💻 Author
**Gayathri Kammidi**
[GitHub](https://github.com/gkammidi-prog) •
[LinkedIn](your-linkedin-url)

---
⭐ Star this repo if you found it useful!