
import folium   #Importing library that provides base map and functions to customize it
#To explore folium-  dir(folium)
#-- help(folium.Map()) eg
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
        

#Adding title
html = """
Volcano name: <br>
<ahref="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m

"""

map = folium.Map(location=[19,74], zoom_start=2.5, tiles="Stamen Terrain")

#Creating a feature group to add Marker from folium objs
fgv = folium.FeatureGroup(name="Volcanoes")

#Customize the marker using for loop and zip function
for lt,ln,el,name in zip(lat, lon, elv, name):   
    iframe = folium.IFrame(html = html % (name, name, el), width=200, height=100)
    fgv.add_child(folium.CircleMarker(location=[lt,ln], radius = 10, popup=folium.Popup(iframe),color = color_dynamics(el), fill=True,
     fill_color=color_dynamics(el), fill_opacity=1))  #circular marker
     #fg.add_child(folium.Marker(location=[lt,ln], popup=folium.Popup(iframe), icon=folium.Icon(color=color_dynamics(el))))     
     #for popup you can use : popup=folium.Popup(str(nm), parse_html=True) 
     #to display elevation in popup :  popup=str(elv)+ " m"

fgp = folium.FeatureGroup(name="Population")
#open the world.json file containing population data
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x:{'fillColor':'green' if x['properties'] ['POP2005'] < 10000000    #Stylzing the map wrt population
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))



map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())  #Adding a control layer to switch on and off the styling layers for population and volcanoes resp.
map.save("Layered_Mapping.html")
