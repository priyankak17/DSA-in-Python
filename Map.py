import folium
import pandas

#Reading coordinates file
df = pandas.read_csv("Volcanoes.txt")
lat = list(df["LAT"])
lon = list(df["LON"])
elv = list(df["ELEV"])
name = list(df["NAME"])

#Function to add color to marker depending on volcano elevation
def color_dynamics(elevation):
    if elevation < 1000:
        return 'green'
    elif elevation >=1000 and elevation<1500:
        return 'blue'
    elif elevation >=1500 and elevation<2000:
        return 'orange'
    else:
        return 'red'
        

#Adding title with gogle search link
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
    fg.add_child(folium.CircleMarker(location=[lt,ln], radius = 10, popup=folium.Popup(iframe),color = color_dynamics(el), fill=True,
     fill_color=color_dynamics(el), fill_opacity=1))  #circular marker
     #fg.add_child(folium.Marker(location=[lt,ln], popup=folium.Popup(iframe), icon=folium.Icon(color=color_dynamics(el))))     
     #for popup you can use : popup=folium.Popup(str(nm), parse_html=True) 
     #to display elevation in popup :  popup=str(elv)+ " m"


map.add_child(fg)
map.save("Map_html_popup_advanced.html")
