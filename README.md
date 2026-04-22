# 🩺 Diabetes Prediction Using Health Indicators



---
## 📌 Overview
This project predicts diabetes using health and lifestyle data.  
It identifies key risk factors and builds a machine learning model for early detection.

---

## 📊 Dataset
- **Records:** 254,000 → 229,781 (after cleaning)  
- **Features:** 22  
- **Target:**  
  - 0 = No diabetes  
  - 1 = Prediabetes  
  - 2 = Diabetes  

---

## 🔍 Key Insights
- Risk increases with **age**  
- **BMI** is a major factor  
- **HighBP & HighChol** strongly linked  
- Poor **general health** increases risk  
- Gender has minimal impact  

---

## 🤖 Models

| Model | Accuracy | Status |
|------|--------|--------|
| Logistic Regression | **83.4%** | ✅ Best |
| Decision Tree | 54.3% | ❌ Weak |

---

## 📊 Visualizations

### Diabetes Distribution
![Diabetes Pie Chart](images/diabetes_distribution.png)

### Age vs Diabetes
![Age Plot](images/age_diabetes.png)

### BMI vs Diabetes
![BMI Plot](images/bmi_diabetes.png)

### Correlation Heatmap
![Heatmap](images/correlation_heatmap.png)

---

## 🛠️ Tech Stack
- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Scikit-learn  

---

## 🧹 Data Preprocessing
- Removed duplicates (23,899 rows)  
- No missing values  
- Cleaned dataset  

---

## 🏆 Key Factors
- High Cholesterol  
- BMI  
- High Blood Pressure  
- General Health  
- Difficulty Walking  

---



---

## 📌 Author
Julius Musau
