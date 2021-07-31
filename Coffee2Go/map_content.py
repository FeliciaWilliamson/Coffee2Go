import folium
import pandas as pd
#Set the intital location of the map view
my_map = folium.Map(location=[40.75726,-73.97609], tiles='OpenStreetMap',  zoom_start =15)
my_map

#reads the csv file and will ouput the 4 column headers I specify in the for loop
shops = pd.read_csv('coffee_shops_NewYork.csv')
shops.head(4)

#reiterate of the map
my_map = folium.Map(location=[40.75726,-73.97609], tiles='OpenStreetMap', zoom_start =15)

#for loop to loop through the csv file to get the information
for _, shop in shops.iterrows():
    folium.Marker(
        location=[shop['Latitude'], shop['Longitude']], 
        popup=shop['Name'] + '\n' + shop['Address'],
        tooltip=shop['Name']
    ).add_to(my_map)

my_map

#Outputs map and information on the map.html file
my_map.save('map.html')