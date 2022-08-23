import folium
import pandas

#Reading coordinates file
df = pandas.read_csv("Volcanoes.txt")
lat = list(df["LAT"])
lon = list(df["LON"])
elv = list(df["ELEV"])
name = list(df["NAME"])

#Adding title
html = """
Volcano name: <br>
<ahref="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m

"""

map = folium.Map(location=[19,74], zoom_start=6, tiles="Stamen Terrain")

#Creating a feature group to add Marker from folium objs
fg = folium.FeatureGroup(name="My Map")

#Customize the marker using for loop and zip function
for lt,ln,el,name in zip(lat, lon, elv, name):   
    iframe = folium.IFrame(html = html % (name, name, el), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt,ln], popup=folium.Popup(iframe), icon=folium.Icon(color='blue')))     
     #for popup you can use : popup=folium.Popup(str(nm), parse_html=True) 
     #to display elevation in popup :  popup=str(elv)+ " m"


map.add_child(fg)
map.save("Map_html_popup_advanced.html")
