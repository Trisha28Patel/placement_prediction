import streamlit as st
import requests
st.title(" Placement predictor")
cgpa=st.slider('CGPA',0.0,10.0,7.0)
aptitude=st.slider("Aptitude Score",0,100,70)
communication=st.slider("Communication",1,10,5)
projects=st.slider("Projects",0,5,2)
if st.button("Predict"):
    url="https://placement-prediction-1-2amy.onrender.com/predict" 
    data={
        'cgpa':cgpa,
        'aptitude':aptitude,
        'communication':communication,
        'projects':projects
    }
    response=requests.post(url,json=data)
    result =response.json()
    if result['prediction']==1:
        st.success("🎉 you wll get placed!")
    else:
        st.error("not likely to be placed")
