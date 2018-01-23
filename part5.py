import folium
import pandas

data_frame = pandas.read_csv("Volcanoes_USA.csv")
map = folium.Map(location=[48.7767982,-121.810997])

fg = folium.FeatureGroup(name = 'My map')
lat = list(data_frame['LAT'])
lon = list(data_frame['LON'])
name = list(data_frame['NAME'])
loc = list(data_frame['LOCATION'])
status = list(data_frame['STATUS'])
elev = list(data_frame['ELEV'])

for i,j,nm,lo,st,el in zip(lat,lon,name,loc,status,elev):
    fg.add_child(folium.Marker(location=(i,j), popup=folium.Popup(nm+', '+lo+', '+st+', '+str(el),parse_html=True), icon=folium.Icon(color='green')))
map.add_child(fg)

map.save("Mymap4.html")
