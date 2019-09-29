import folium as f
map=f.Map(location=[16.763657,80.6380532],zoom_control=6,tiles='Mapbox Bright ')
fg=f.FeatureGroup("Volcanos")
fg.add_child(f.Marker(location=[16.763657,80.6380532],popup="Hi Bhargav!",icon=f.Icon(color='green')))
map.add_child(fg)
#--->Map(FeatureGroup(add_child))
map.save("Location.html")
print(map)