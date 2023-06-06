import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import json
from shapely.geometry import Point
from streamlit_folium import st_folium

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
    gr1 = plt.figure(figsize=(24, 8))
    plt.xlabel("Years")
    plt.ylabel(option_disorder)
    plt.plot(data_disorders_c['Year'], data_disorders_c[option_disorder])
    st.pyplot(gr1)
    
    st.header("Comparison of morbidity rates in different countries")
    
    list_countries = st.multiselect("Countries: ", countries)
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
    data_centers = pd.read_csv ('data-605-2999-01-01.csv', delimiter=';')
    data_centers = data_centers[1:]
    geoData_centers = data_centers['geoData']
    centers_points = [Point(*json.loads(row)['coordinates']) for row in geoData_centers.values]
    data_centers['geometry'] = centers_points
    #!pip install folium matplotlib mapclassify
    geodata_centers = gpd.GeoDataFrame(data_centers, crs="EPSG:4326")
    ans = st_folium(geodata_centers.explore(), width = 725)
    ans
    
    
  
