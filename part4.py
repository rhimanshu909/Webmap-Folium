import folium
import pandas

data_frame = pandas.read_csv("Volcanoes_USA.csv")
map = folium.Map(location=[48.7767982,-121.810997])

fg = folium.FeatureGroup(name = 'My map')
lat = list(data_frame['LAT'])
lon = list(data_frame['LON'])

for i,j in zip(lat,lon):
    fg.add_child(folium.Marker(location=(i,j),popup="This is the information from Marker", icon=folium.Icon(color='green')))
map.add_child(fg)

map.save("Mymap3.html")
