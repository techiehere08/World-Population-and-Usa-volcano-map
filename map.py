import pandas
import folium
map=folium.Map(location=[38,-99],tiles="Mapbox Bright",zoom_start=6,width='100%',height='100%',min_zoom=2)
df=pandas.read_csv("vol.txt")
lat=df["LAT"]
lon=df["LON"]
el=df["ELEV"]

def color(el):
    if el<1000:
        return 'green'
    elif el>=1000 and el<=3000:
        return 'orange'
    else:
        return 'red'

fgv=folium.FeatureGroup(name="Volcano")

fgp=folium.FeatureGroup(name="Population")

for lat,lon,el in zip(lat,lon,el):
    fgv.add_child(folium.CircleMarker(location=[lat,lon],popup=str(el),radius=6,fill_color=color(el),color='grey',fill_opacity=0.8))


fgp.add_child(folium.GeoJson(data=open("world.json",'r',encoding='utf-8-sig').read(),style_function= lambda x: {'fillColor':'green' if
x['properties']['POP2005']<10000000 else 'orange' if 10000000<x['properties']['POP2005']<20000000 else 'red'}))

map.add_child(fgv)

map.add_child(fgp)

map.add_child(folium.LayerControl())

map.save("layercontrol.html")