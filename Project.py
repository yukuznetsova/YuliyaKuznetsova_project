import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import json
from shapely.geometry import Point
from streamlit_folium import st_folium
import requests
import geojson

with st.echo(code_location='below'): #не была уверена, нужно ли вставлять основной код в сайт, поэтому решила вставить
    st.title ("Mental disorders")
    st.text ("The main topic of this project is mental health and mental disorders.")
    st.text ("Now they still remain being stigmatized and sometimes people use names")
    st.text ("of mental disorders incorrectly, for instance, as offensive name-calling.")
    st.text ("It is important for people to learn more about this topic.")
    st.divider ()
    st.text ("Here is some information about several mental disorders.")
    info_disorders = pd.read_csv("All_disorders.csv", ) #загружаю датафрейм, который получила в файле Working with selenium
    info_disorders.drop (info_disorders.columns [0], axis= 1, inplace = True) #удаляю лишние колонки
    info_disorders.drop (info_disorders.columns [0], axis= 1, inplace = True)
    info_disorders.set_index ("category")
    st.dataframe (info_disorders, width = 800, height = 800, hide_index = True) #отображение датафрейма на сайте
    
    
    data_disorders = pd.read_csv('Mental health Depression disorder Data.csv', delimiter=',', index_col='index') #загружаю датафрейм, взятый с https://www.kaggle.com/datasets/thedevastator/uncover-global-trends-in-mental-health-disorder
    data_disorders.columns = ['Entity', 'Code', 'Year', 'Schizophrenia', 'Bipolar_disorder', 'Eating_disorders', 'Anxiety_disorders', 'Drug_use_disorders', 'Depression', 'Alcohol_use_disorders']
    data_disorders_world = data_disorders[data_disorders['Entity']=='World'].head(28)
    data_disorders = data_disorders[data_disorders['Entity']!='World'] #в датафрейме есть ещё и усредненные данные по миру. они не понадобятся
    
    st.header("The dinamics of the disorders from 1990 to 2017")
    
    col_country, col_disorder = st.columns(2) #для удобного выбора страны и расстройства
    
    countries = data_disorders.Entity.unique() #список всех стран, которые есть в датафрейме
    with col_country:
        option_country = st.selectbox( #выбор страны
        'Choose the country', 
        countries)
    
    with col_disorder:
        option_disorder = st.selectbox( #выбор расстройства
        'Choose the disorder', 
        ('Schizophrenia', 'Bipolar_disorder', 'Eating_disorders', 'Anxiety_disorders', 'Drug_use_disorders', 'Depression', 'Alcohol_use_disorders')) #названия опций совпадают с названиями столбцов датафрейма
    
    data_disorders_c = data_disorders[data_disorders['Entity']==option_country].head(28) #создаю датафрейм из старого только для одной страны
    gr1 = plt.figure(figsize=(24, 8)) #с помощью matplotlib создаю график
    plt.xlabel("Years")
    plt.ylabel(option_disorder)
    plt.plot(data_disorders_c['Year'], data_disorders_c[option_disorder])
    st.pyplot(gr1) #отображаю полученный график в streamlit
    
    st.header("Comparison of morbidity rates in different countries in 2017")
   
    list_countries = st.multiselect("Choose several countries: ", countries) #выбор стран для сравнения
    option_disorder1 = st.selectbox( #выбор расстройства для сравнения
        'Choose the new disorder', 
        ('Schizophrenia', 'Bipolar_disorder', 'Eating_disorders', 'Anxiety_disorders', 'Drug_use_disorders', 'Depression', 'Alcohol_use_disorders'))
    
    data_disorders_17 = data_disorders[data_disorders['Year']=='2017'] #датафрейм для 2017 года
    data_disorders_17 = data_disorders_17[data_disorders_17 ['Entity'].isin (list_countries)] #датафрейм для 2017 года и списка стран
    data_disorders_17_d = data_disorders_17[['Entity', option_disorder1]].head(len(list_countries)) #датафрейм для 2017 года, списка стран и выбранного расстройства
    
    gr2 = plt.figure(figsize=(24, 8)) #с помощью matplotlib создаю график
    plt.bar(data_disorders_17_d['Entity'], data_disorders_17_d[option_disorder1])
    st.pyplot(gr2) #отображаю полученный график в streamlit
    
    st.header("The psychological assistance centers in Moscow") 
    st.text ("Please, wait for the map to load")
    #Получение данных с использованием API в файле API_centers_points.py. Данные загружены в файл centers_points.geojson
    data_centers = gpd.read_file('centers_points.geojson') #читаю файл
    centers_points = gpd.GeoDataFrame(data_centers, geometry = 'geometry', crs="EPSG:4326") #сохраняю в датафрейм координаты 
    map_centers = st_folium(centers_points.explore(), width = 725) #отображение точек на интерактивной карте с помощью folium
    
    
    
    
