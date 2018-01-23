import folium
map = folium.Map(location=[60,-120])

fg = folium.FeatureGroup(name = 'My map')
fg.add_child(folium.Marker(location=[60,-120],popup="This is the information from Marker", icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Mymap.html")
