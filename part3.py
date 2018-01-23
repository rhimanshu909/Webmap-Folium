import folium
map = folium.Map(location=[60,-120])

fg = folium.FeatureGroup(name = 'My map')
for coordinates in [[60,-120],[66,-115]]:
    fg.add_child(folium.Marker(location=coordinates,popup="This is the information from Marker", icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Mymap2.html")
