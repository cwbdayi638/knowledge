import folium

# Earthquake data
earthquakes = [
    {"lat": -46.6443, "lng": 165.4903, "mag": 5.3, "place": "196 km W of Riverton, New Zealand"},
    {"lat": 51.8844, "lng": -176.4897, "mag": 5.1, "place": "43 km E of Adak, Alaska"},
    {"lat": -6.5908, "lng": 151.0788, "mag": 4.9, "place": "155 km SE of Kimbe, Papua New Guinea"},
    {"lat": -57.5469, "lng": -25.1411, "mag": 4.8, "place": "South Sandwich Islands region"},
    {"lat": -23.5977, "lng": 179.9337, "mag": 4.7, "place": "South of the Fiji Islands"},
    {"lat": 37.8121, "lng": 71.9641, "mag": 4.6, "place": "50 km NE of Khorugh, Tajikistan"},
    {"lat": 51.8537, "lng": 158.5676, "mag": 4.5, "place": "120 km S of Vilyuchinsk, Russia"},
    {"lat": -24.1919, "lng": -67.2778, "mag": 4.5, "place": "97 km W of San Antonio de los Cobres, Argentina"},
]

def get_color(mag):
    if mag >= 5.0: return 'red'
    if mag >= 4.8: return 'orange'
    if mag >= 4.6: return 'yellow'
    return 'green'

# Create map centered at [20, 0]
m = folium.Map(location=[20, 0], zoom_start=2, tiles='CartoDB dark_matter')

# Add markers
for eq in earthquakes:
    folium.CircleMarker(
        location=[eq['lat'], eq['lng']],
        radius=eq['mag'] * 2,
        popup=f"M {eq['mag']} - {eq['place']}",
        color=get_color(eq['mag']),
        fill=True,
        fill_color=get_color(eq['mag']),
        fill_opacity=0.7
    ).add_to(m)

# Save map
m.save('eq_folium_map.html')
print("Folium map saved as eq_folium_map.html")
