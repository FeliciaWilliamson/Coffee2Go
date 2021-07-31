import folium
import pandas as pd

my_map = folium.Map(location=[40.75726,-73.97609], tiles='OpenStreetMap', zoom_start =15)
my_map

shops = pd.read_csv('coffee_shops_NewYork.csv')
shops.head(4)

my_map = folium.Map(location=[40.75726,-73.97609], tiles='OpenStreetMap', zoom_start =15)

for _, shop in shops.iterrows():
    folium.Marker(
        location=[shop['Latitude'], shop['Longitude']], 
        popup=shop['Name'] + '\n' + shop['Address'],
        tooltip=shop['Name']
    ).add_to(my_map)

my_map

my_map.save('map.html')