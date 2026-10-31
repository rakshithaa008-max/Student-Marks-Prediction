# 🎓 Student Marks Prediction — End-to-End ML Project

## 📌 Project Overview
An end-to-end Machine Learning project that predicts student final exam marks based on study hours, attendance percentage, and previous exam marks.

The project includes data generation, exploratory data analysis (EDA), model training, evaluation, and deployment using Streamlit.

**Note:** This project uses synthetic student data for educational purposes.

## 🚀 Live Application
[Try the Student Marks Prediction App](https://student-marks-prediction-hgwkbja7nbxdedryh5f7rp.streamlit.app/)

## 🛠️ Technologies Used
- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Scikit-learn
- Linear Regression
- Google Colab
- Streamlit
- GitHub

## 📊 Dataset
The dataset contains 500 synthetic student records.

**Input Features:**
- Study Hours — Daily study time
- Attendance — Attendance percentage
- Previous Marks — Previous exam score

**Target Variable:**
- Final Marks — Predicted final exam score

## 🔄 Project Workflow
1. Generate synthetic student data
2. Perform Exploratory Data Analysis (EDA)
3. Check missing values and analyze correlations
4. Split dataset into training and testing sets (80:20)
5. Train Linear Regression model
6. Evaluate using MAE, RMSE, and R² Score
7. Save the trained model using Joblib
8. Build an interactive Streamlit application
9. Deploy the application using Streamlit Community Cloud

## 🤖 Machine Learning Model
**Algorithm:** Linear Regression

**Model Evaluation:**
- MAE: Add actual result
- RMSE: Add actual result
- R² Score: Add actual result

## 🎯 Example Prediction

| Feature | Value |
|---|---|
| Study Hours | 6 hours |
| Attendance | 85% |
| Previous Marks | 70 |
| Predicted Final Marks | 68.8 / 100 |

## 📁 Project Structure

```text
Student-Marks-Prediction/
├── README.md
├── Student_Marks_Prediction_ipynb_.ipynb
├── app.py
├── model.pkl
├── requirements.txt
└── student_data.csv
```

## ▶️ Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the application:

```bash
streamlit run app.py
```

## 📈 Future Improvements
- Train on a real, appropriately sourced dataset
- Compare multiple regression algorithms
- Add feature importance analysis
- Improve the application interface
- Evaluate generalization on unseen data

## ⚠️ Disclaimer
This application uses synthetic data and is intended for learning and demonstration only. Predictions are not validated for real academic decisions.
