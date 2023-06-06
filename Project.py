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
    
    countries = data_disorders.Entity.unique()
    
    col_country, col_disorder = st.columns(2)
    
    with col_country:
    option_country = st.selectbox(
    'Выберите страну', 
    countries)
    )
    
    with col_disorder:
    option_disorder = st.selectbox(
    'Выберите расстройство', 
    ('Schizophrenia', 'Bipolar disorder', 'Eating disorders', 'Anxiety disorders', 'Drug use disorders', 'Depression', 'Alcohol use disorders'))
    )
    
