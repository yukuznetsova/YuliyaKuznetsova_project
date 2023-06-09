import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import json
from shapely.geometry import Point
from streamlit_folium import st_folium
import requests
import geojson

with st.echo(code_location='below'):
    info_disorders = pd.read_csv("All_disorders.csv", )
    info_disorders.drop (info_disorders.columns [0], axis= 1, inplace = True)
    info_disorders.drop (info_disorders.columns [0], axis= 1, inplace = True)
    info_disorders.set_index ("category")
    st.dataframe (info_disorders, hide_index = True)
    
    
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
    gr1 = plt.figure(figsize=(24, 8))
    plt.xlabel("Years")
    plt.ylabel(option_disorder)
    plt.plot(data_disorders_c['Year'], data_disorders_c[option_disorder])
    st.pyplot(gr1)
    
    st.header("Comparison of morbidity rates in different countries")
   
    list_countries = st.multiselect("Choose several countries: ", countries)
    option_disorder1 = st.selectbox(
        'Choose the new disorder', 
        ('Schizophrenia', 'Bipolar_disorder', 'Eating_disorders', 'Anxiety_disorders', 'Drug_use_disorders', 'Depression', 'Alcohol_use_disorders'))
    
    data_disorders_17 = data_disorders[data_disorders['Year']=='2017']
    data_disorders_17 = data_disorders_17[data_disorders_17 ['Entity'].isin (list_countries)]
    data_disorders_17_d = data_disorders_17[['Entity', option_disorder1]].head(len(list_countries))
    
    gr2 = plt.figure(figsize=(24, 8))
    plt.bar(data_disorders_17_d['Entity'], data_disorders_17_d[option_disorder1])
    st.pyplot(gr2)
    
    st.header("The psychological assistance centers in Moscow") 
    st.text ("Please, wait for the map to load")
    #Получение данных с использованием API в файле API_centers_points.py. Данные загружены в файл centers_points.geojson
    data_centers = gpd.read_file('centers_points.geojson')
    centers_points = gpd.GeoDataFrame(data_centers, geometry = 'geometry', crs="EPSG:4326")
    map_centers = st_folium(centers_points.explore(), width = 725)
    
    
    
    
