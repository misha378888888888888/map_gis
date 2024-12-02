import folium

map = folium.Map(
    location=[53.7156,91.4292],
    zoom_start = 13,
    tiles = 'OpenStreetmap'
)

map.save("map1.html")