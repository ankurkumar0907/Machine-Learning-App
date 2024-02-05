import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


#loading save models

Heart_Disease_models = pickle.load(open('/home/ankur09/ML Project/Heart Disease Prediction/Heart_disease_Predicition.sav',"rb"))

Tabular_Kidney_Stone_models = pickle.load(open('/home/ankur09/ML Project/Tabular Kidney Stone Prediction/Tabular-kidney-stone_Prediction.sav','rb'))

# Sidebar for navigate
with st.sidebar:
    selected = option_menu('Prediction',
                           ['Heart Disease prediction',
                           'Tabular Kidney Stone prediction'],
                           icons = ["bag-heart-fill","file-medical"],
                           default_index = 0)
    
# Heart Disease prediction Page
if (selected == "Heart Disease prediction"):
    #Page title
    st.title('Heart Disease prediction Using ML')
    
    link_col1,link_col2 = st.columns(2)
        
    GitHub = '[GitHub](https://github.com/ankurkumar0907/Machine-Learning-App)'
    with link_col1:
        st.markdown(GitHub, unsafe_allow_html=True)
    
    Dataset = '[Dataset Source](https://www.kaggle.com/datasets/utkarshx27/heart-disease-diagnosis-dataset)'
    with link_col2:
        st.markdown(Dataset, unsafe_allow_html=True)
    
    # create columns
    col1, col2, col3 = st.columns(3)
    #input
    with col1:
        Age = st.text_input("Age")
    with col2:
        sex = st.text_input("Sex")
    with col3:
        chest_pain_type = st.text_input("Chest Pain Type")
    with col1:
        resting_blood_pressure = st.text_input("Resting Blood Pressure")
    with col2:
        serum_cholestoral = st.text_input("Serum Cholestoral")
    with col3:
        fasting_blood_sugar = st.text_input("Fasting Blood Sugar")
    with col1:
        resting_electrocardiographic_results = st.text_input("Resting Electrocardiographic Results ")
    with col2:
        max_heart_rate = st.text_input("Max Heart Rate")
    with col3:
        exercise_induced_angina = st.text_input("Exercise Induced Angina")
    with col1:
        oldpeak = st.text_input("Oldpeak")
    with col2:
        ST_segment = st.text_input("ST Segment")
    with col3:
        major_vessels = st.text_input("Major Vessels")
    with col1:
        thal = st.text_input("Thal")

    #code for prediction
    dignosis = ''
    # create a button for predict
    if st.button("Heart Disease Predict"):
        Heart_disease_Predict = Heart_Disease_models.predict([[int(Age),int(sex),int(chest_pain_type),
                                                               int(resting_blood_pressure),int(serum_cholestoral),
                                                               int(fasting_blood_sugar),int(resting_electrocardiographic_results),
                                                               int(max_heart_rate),int(exercise_induced_angina),float(oldpeak),
                                                               int(ST_segment),int(major_vessels),int(thal)]])
        if (Heart_disease_Predict[0]==1):
            dignosis = 'Heart Disease Absence'
        else :
            dignosis = 'Heart Disease Presence'
    st.success(dignosis)
        
    
    
    
if  (selected == "Tabular Kidney Stone prediction"):
    
    st.title("Tabular Kidney Stone prediction Using ML")
    
        
    link_col1,link_col2 = st.columns(2)
        
    GitHub = '[GitHub](https://github.com/ankurkumar0907/Machine-Learning-App)'
    with link_col1:
        st.markdown(GitHub, unsafe_allow_html=True)
    
    Dataset = '[Dataset Source](https://www.kaggle.com/competitions/playground-series-s3e12/overview)'
    with link_col2:
        st.markdown(Dataset, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        gravity = st.text_input("Gravity")
    with col2:
        ph = st.text_input("Ph")
    with col3:
        osmo = st.text_input("Osmo")
    with col1:
        cond = st.text_input("Cond")
    with col2:
        urea = st.text_input("Urea")
    with col3:
        calc = st.text_input("Calc")
        
    stone_predict = ""
    
    if st.button("Tabular Kidney Stone Predict"):
        tks_predict = Tabular_Kidney_Stone_models.predict([[gravity,ph,osmo,cond,urea,calc]])
        
        if tks_predict[0]==1:
            stone_predict = "Kidney Stone Being Present"
        else:
            stone_predict = "Kidney Stone Not Present"
    st.success(stone_predict)
        
    