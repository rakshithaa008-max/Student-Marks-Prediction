# Student Marks Prediction (End-to-End ML)

A beginner-friendly regression project using **synthetic** student data. Inputs: study hours, attendance, previous marks. Output: predicted final marks (0–100).

## Workflow
1. Generate synthetic dataset and perform EDA in Google Colab.
2. Split into train/test, train LinearRegression, evaluate with MAE/RMSE/R².
3. Save fitted model to `model.pkl` with `joblib.dump(model, 'model.pkl')`.
4. Put `model.pkl`, `app.py`, and `requirements.txt` in the same directory.
5. Run `pip install -r requirements.txt` and `streamlit run app.py`.
6. Push files to GitHub and deploy from Streamlit Community Cloud.

**Important:** Data is simulated for learning, so results are not validated for real-world educational decisions.
