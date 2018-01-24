import folium
import pandas

data_frame = pandas.read_csv("Volcanoes_USA.csv")
map = folium.Map(location=[48.7767982,-121.810997])

lat = list(data_frame['LAT'])
lon = list(data_frame['LON'])
name = list(data_frame['NAME'])
loc = list(data_frame['LOCATION'])
status = list(data_frame['STATUS'])
elev = list(data_frame['ELEV'])

fg_vol = folium.FeatureGroup(name = 'Volcanoes_USA')

def mark_color(elevation):
    if elevation>3000:
        return 'red'
    elif elevation in range(1000,3000):
        return 'orange'
    else:
        return 'green'

for i,j,nm,lo,st,el in zip(lat,lon,name,loc,status,elev):
    fg_vol.add_child(folium.CircleMarker(location=(i,j), radius=5, popup=folium.Popup(nm+', '+lo+', '+st+', '+str(el),parse_html=True), color=mark_color(el), fill=True, fill_opacity=0.8))


fg_popul = folium.FeatureGroup(name = 'Population')

fg_popul.add_child(folium.GeoJson(data=open('world.json','r',encoding='UTF-8-sig').read(),style_function = lambda x: {'fillColor':'yellow' if x['properties']['POP2005'] < 10000000
else 'green' if x['properties']['POP2005'] in range(10000000,50000000) else 'red'}))

map.add_child(fg_vol)
map.add_child(fg_popul)
map.add_child(folium.LayerControl()) #Always add this after the FeatureGroup because LayerControl will be finding it on Map
map.save("Mymap8.html")
