# -*- coding: utf-8 -*-
"""
Created on Wed Apr 05 18:06:17 2023

"""



import pandas as pd
import streamlit as st 

from pickle import dump
from pickle import load

st.title('Model Deployment: Forecasting')

st.sidebar.header('User Input Parameters')

    
Days = st.sidebar.number_input("number of days for forecasting",min_value=1, step=1)
st.subheader('User Input parameters')
st.write(Days)



# load the model from disk
loaded_model = load(open('/blob/main/final_model.sav', 'rb'))

prediction = loaded_model.forecast(Days)




st.subheader('Predicted Values')
st.write(prediction)


