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

data_centers = requests.get("https://apidata.mos.ru/v1/datasets/605/features?api_key=0c4259c55453af65f9b7052058e0bf28")
centers = data_centers.json()
centers_points = gpd.GeoDataFrame.from_features(centers, crs="EPSG:4326")
centers_points.to_csv('psich_centers_points.csv')

centers_points.explore()