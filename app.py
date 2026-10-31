import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(page_title='Student Marks Predictor', page_icon='🎓')
st.title('🎓 Student Marks Prediction')
st.write('Enter student details to estimate final exam marks.')
model = joblib.load('model.pkl')
hours = st.slider('Study hours per day', 1.0, 10.0, 6.0, 0.1)
attendance = st.slider('Attendance (%)', 50, 100, 85)
previous = st.slider('Previous marks', 30, 95, 70)
if st.button('Predict Final Marks'):
    features = pd.DataFrame({'Study_Hours':[hours], 'Attendance':[attendance], 'Previous_Marks':[previous]})
    predicted = np.clip(model.predict(features)[0], 0, 100)
    st.metric('Predicted Final Marks', f'{predicted:.1f} / 100')
    st.caption('Educational demonstration trained on synthetic data; not suitable for real academic decisions.')
