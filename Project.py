import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import altair as alt

with st.echo(code_location='below'):
    data_disorders = pd.read_csv('Mental health Depression disorder Data.csv', delimiter=',', index_col='index')
    data_disorders.columns = ['Entity', 'Code', 'Year', 'Schizophrenia', 'Bipolar_disorder', 'Eating_disorders', 'Anxiety_disorders', 'Drug_use_disorders', 'Depression', 'Alcohol_use_disorders']
    data_disorders_world = data_disorders[data_disorders['Entity']=='World'].head(28)
    data_disorders = data_disorders[data_disorders['Entity']!='World']
    
    st.header("The dinamics of the disorders from 1990 to 2017")
    
    col_country, col_disorder = st.columns(2)
    
    countries = data_disorders.Entity.unique()
    with col_country:
        option_country = st.selectbox(
        'Choose the country', 
        countries)
    
    with col_disorder:
        option_disorder = st.selectbox(
        'Choose the disorder', 
        ('Schizophrenia', 'Bipolar_disorder', 'Eating_disorders', 'Anxiety_disorders', 'Drug_use_disorders', 'Depression', 'Alcohol_use_disorders'))
    
    data_disorders_c = data_disorders[data_disorders['Entity']==option_country].head(28)
    #gr1 = plt.figure(figsize=(24, 8))
    #plt.xlabel("Years")
    #plt.ylabel(option_disorder)
    #plt.plot(data_disorders_c['Year'], data_disorders_c[option_disorder])
    #st.pyplot(gr1)
    
    st.header("Comparison of morbidity rates in different countries")
    
    list_countries = st.multiselect("Countries: ", countries)
    option_disorder1 = st.selectbox(
        'Choose the new disorder', 
        ('Schizophrenia', 'Bipolar_disorder', 'Eating_disorders', 'Anxiety_disorders', 'Drug_use_disorders', 'Depression', 'Alcohol_use_disorders'))
    
    data_disorders_17 = data_disorders[data_disorders['Year']=='2017']
    data_disorders_17 = data_disorders_17[data_disorders_17 ['Entity'].isin (list_countries)]
    data_disorders_17_d = data_disorders_17[['Entity', option_disorder1]].head(len(list_countries))
    st.dataframe(data_disorders_17_d)
    
    #gr2 = plt.figure(figsize=(24, 8))
    
