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

def mark_color(elevation):
    if elevation>3000:
        return 'red'
    elif elevation in range(1000,3000):
        return 'orange'
    else:
        return 'green'

for i,j,nm,lo,st,el in zip(lat,lon,name,loc,status,elev):
    fg.add_child(folium.CircleMarker(location=(i,j), radius=5, popup=folium.Popup(nm+', '+lo+', '+st+', '+str(el),parse_html=True), color=mark_color(el), fill=True, fill_opacity=0.8))
map.add_child(fg)
map.save("Mymap6.html")
