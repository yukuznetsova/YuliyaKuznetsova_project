import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import json
from shapely.geometry import Point
from streamlit_folium import st_folium
import requests
import geojson
import seaborn as sns

st.title ("Mental disorders")
st.text ("The main topic of this project is mental health and mental disorders.")
st.text ("After a long while of research and public discussions they still remain")
st.text ("stimatized, and sometimes people use names of mental disorders incorrectly,")
st.text ("for instance, as offensive name-calling. It is important for people to learn")
st.text ("more about this topic. For example, prevalence, symptoms, causes and treatment.")
st.divider ()
st.text ("Here is some information about several mental disorders.")
info_disorders = pd.read_csv("All_disorders.csv", ) #загружаю датафрейм, который получила в файле Working with selenium
info_disorders.drop (info_disorders.columns [0], axis= 1, inplace = True) #удаляю лишние колонки
info_disorders.drop (info_disorders.columns [0], axis= 1, inplace = True)
st.dataframe (info_disorders, hide_index = True) #отображение датафрейма на сайте
    
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
data_disorders_c['Schizophrenia'] = pd.to_numeric(data_disorders_c['Schizophrenia']) #три столбца были в текстовом формате
data_disorders_c['Bipolar_disorder'] = pd.to_numeric(data_disorders_c['Bipolar_disorder'])
data_disorders_c['Eating_disorders'] = pd.to_numeric(data_disorders_c['Eating_disorders'])
gr1 = plt.figure(figsize=(24, 8)) #с помощью matplotlib создаю график
plt.xlabel("Years")
plt.ylabel(option_disorder)
plt.plot(data_disorders_c['Year'], data_disorders_c[option_disorder])
st.pyplot(gr1) #отображаю полученный график в streamlit
    
st.header("Comparison of morbidity rates % in different countries in 2017")
   
list_countries = st.multiselect("Choose several countries: ", countries) #выбор стран для сравнения
option_disorder1 = st.selectbox( #выбор расстройства для сравнения
    'Choose the new disorder', 
    ('Schizophrenia', 'Bipolar_disorder', 'Eating_disorders', 'Anxiety_disorders', 'Drug_use_disorders', 'Depression', 'Alcohol_use_disorders'))
    
data_disorders_17 = data_disorders[data_disorders['Year']=='2017'] #датафрейм для 2017 года
data_disorders_17 = data_disorders_17[data_disorders_17 ['Entity'].isin (list_countries)] #датафрейм для 2017 года и списка стран
data_disorders_17_d = data_disorders_17[['Entity', option_disorder1]].head(len(list_countries)) #датафрейм для 2017 года, списка стран и выбранного расстройства
data_disorders_17_d[option_disorder1] = pd.to_numeric(data_disorders_17_d[option_disorder1]) #привожу строковые данные к числовым

gr2 = plt.figure(figsize=(24, 8)) #с помощью matplotlib создаю график
plt.bar(data_disorders_17_d['Entity'], data_disorders_17_d[option_disorder1])
st.pyplot(gr2) #отображаю полученный график в streamlit
    
st.header("Dependence betweeen GDP per capita and morbidity rate")
st.text("Sometimes there is no dependence")
data_gdp_1 = pd.read_csv ("GDP_per_capita.csv", sep = ";")
data_gdp = data_gdp_1[['Country Name', '2017']].copy()
data_gdp = data_gdp.sort_values(by=['Country Name'])
data_gdp.columns = ['Entity', 'GDP per capita']
    
data_disorders_2017 = data_disorders[data_disorders['Year']=='2017']
data_gdp_disorders = data_disorders_2017.merge(data_gdp[['Entity', 'GDP per capita']])
data_gdp_disorders = data_gdp_disorders.dropna()
#все данные оказались строками, поэтому для построения графика их нужно перевести в числовой формат
data_gdp_disorders['GDP per capita'] = data_gdp_disorders['GDP per capita'].replace(',', '.', regex = True)
data_gdp_disorders['GDP per capita'] = pd.to_numeric(data_gdp_disorders['GDP per capita'])
data_gdp_disorders['Eating_disorders'] = data_gdp_disorders['Eating_disorders'].replace(',', '.', regex = True)
data_gdp_disorders['Eating_disorders'] = pd.to_numeric(data_gdp_disorders['Eating_disorders'])
data_gdp_disorders['Schizophrenia'] = data_gdp_disorders['Schizophrenia'].replace(',', '.', regex = True)
data_gdp_disorders['Schizophrenia'] = pd.to_numeric(data_gdp_disorders['Schizophrenia'])
data_gdp_disorders['Bipolar_disorder'] = data_gdp_disorders['Bipolar_disorder'].replace(',', '.', regex = True)
data_gdp_disorders['Bipolar_disorder'] = pd.to_numeric(data_gdp_disorders['Bipolar_disorder'])
data_gdp_disorders['Anxiety_disorders'] = data_gdp_disorders['Anxiety_disorders'].replace(',', '.', regex = True)
data_gdp_disorders['Anxiety_disorders'] = pd.to_numeric(data_gdp_disorders['Anxiety_disorders'])
data_gdp_disorders['Drug_use_disorders'] = data_gdp_disorders['Drug_use_disorders'].replace(',', '.', regex = True)
data_gdp_disorders['Drug_use_disorders'] = pd.to_numeric(data_gdp_disorders['Drug_use_disorders'])
data_gdp_disorders['Depression'] = data_gdp_disorders['Depression'].replace(',', '.', regex = True)
data_gdp_disorders['Depression'] = pd.to_numeric(data_gdp_disorders['Depression'])
data_gdp_disorders['Alcohol_use_disorders'] = data_gdp_disorders['Alcohol_use_disorders'].replace(',', '.', regex = True)
data_gdp_disorders['Alcohol_use_disorders'] = pd.to_numeric(data_gdp_disorders['Alcohol_use_disorders'])
    
option_disorder2 = st.selectbox( #выбор расстройства для построения зависимости
    'Choose the new disorder again', 
    ('Schizophrenia', 'Bipolar_disorder', 'Eating_disorders', 'Anxiety_disorders', 'Drug_use_disorders', 'Depression', 'Alcohol_use_disorders'))
    
### FROM: https://habr.com/ru/articles/468295/
sns.set_style("white")
gr3 = sns.lmplot(x="GDP per capita", y=option_disorder2, data=data_gdp_disorders, 
                 height=7, aspect=1.6, robust=True, palette='tab10', 
                 scatter_kws=dict(s=60, linewidths=.7, edgecolors='black'))
### END FROM
st.pyplot(gr3)
    
st.header("The psychological assistance centers in Moscow") 
st.text ("Территориальный отдел психологической помощи населению в ЦАО")
st.text ("Территориальный отдел психологической помощи населению в СЗАО")
st.text ("Территориальный отдел психологической помощи населению в ЗАО")
st.text ("Территориальный отдел психологической помощи населению в СВАО")
st.text ("Территориальный отдел психологической помощи населению в ЮАО")
st.text ("Московская служба психологической помощи населению")
st.text ("Участковый отдел психологической помощи населения «Щербинка»")
st.text ("Территориальный отдел психологической помощи населению в САО")
st.text ("Территориальный отдел психологической помощи населению в ВАО")
st.caption ("Please, wait for the map to load")
#Получение данных с использованием API в файле API_centers_points.py. Данные загружены в файл centers_points.geojson
data_centers = gpd.read_file('centers_points.geojson') #читаю файл
centers_points = gpd.GeoDataFrame(data_centers, geometry = 'geometry', crs="EPSG:4326") #сохраняю в датафрейм координаты 
map_centers = st_folium(centers_points.explore(), width = 725) #отображение точек на интерактивной карте с помощью folium
    
   
