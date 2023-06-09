#!pip install requests
import requests
#!pip install geojson
import geojson
import pandas as pd
import matplotlib.pyplot as plt
#!pip install geopandas
import geopandas as gpd
#!pip install folium matplotlib mapclassify
#!pip install geographiclib

data_centers = requests.get("https://apidata.mos.ru/v1/datasets/605/features?api_key=<...>") #загружаю данные с data.mos.ru, используя API key. ключ убрала, так как проект публичный
centers = data_centers.json() #преобразование в json
centers_points = gpd.GeoDataFrame.from_features(centers, crs="EPSG:4326") #создаю из json датафрейм
centers_points.to_csv('psich_centers_points.csv') #загружаю датафрейм

centers_points.explore()
