import streamlit as st
import joblib
st.title('Heart Disease prediction')
model=joblib.load('archive.joblib')
age=st.number_input('Enter the age')
sex=st.number_input('Enter the sex Male:0 Female:1')
cp=st.number_input('Enter the chest pain type')
trestbps=st.number_input('Enter the resting blood plessure ')
chol=st.number_input('Enter the serum cholestrol in mg')
fbs=st.number_input('Enter fasting blood sugar True:1 False:0')
restecg=st.number_input('Enter the resting electrocardiographic results')
thalach=st.number_input('Enter the maximum heart rate achieved')
exang=st.number_input('Enter the Exercise included angina yes:1 no:0')
oldpeak=st.number_input('Enter the ST depression induced by exercise relative to rest')
slope=st.number_input('Enter the slope value')
ca=st.number_input('Enter the ca value')
thal=st.number_input('Enter the thal value')
if st.button('Get the Diagnoise'):
    predictions=model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
    if predictions=='y':
        st.text('No Heart Disease Efected')
    else:
        st.text('There is a Heart Disease')
