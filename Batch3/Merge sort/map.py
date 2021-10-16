# import folium
# m = folium.Map(location=[52.403599, 16.904025])
# m.save("index.html")

# import folium
# from IPython.display import HTML, display
# LDN_COORDINATES = (51.5074, 0.1278)
# myMap = folium.Map(location=LDN_COORDINATES, zoom_start=12)
# myMap.build_map()
# mapWidth, mapHeight = (400,500) # width and height of the displayed iFrame, in pixels
# srcdoc = myMap.HTML.replace('"', '&quot;')
# embed = HTML('<iframe srcdoc="{}" '
#              'style="width: {}px; height: {}px; display:block; width: 50%; margin: 0 auto; '
#              'border: none"></iframe>'.format(srcdoc, width, height))
# embed

# import geopandas
# import geoplot

# world = geopandas.read_file(
#     geopandas.datasets.get_path('naturalearth_lowres')
# )
# boroughs = geopandas.read_file(
#     geoplot.datasets.get_path('nyc_boroughs')
# )
# collisions = geopandas.read_file(
#     geoplot.datasets.get_path('nyc_injurious_collisions')
# )

import arcpy
aprx = arcpy.mp.ArcGISProject(r"C:\Projects\YosemiteNP\Yosemite.aprx")
lyt = aprx.listLayouts("Main Attractions*")[0]
mpFrm2D = lyt.listElements("mapframe_element", "Yose*")[0]
mpFrm3D = lyt.listElements("mapframe_element", "Inset1")[0]
for m in aprx.listMaps():
    if m.mapType == "MAP":
        m.defaultMapViewer = mpFrm2D.mapViewer
    elif m.mapType == "SCENE":
        m.defaultMapViewer = mpFrm3D.mapViewer
aprx.save()
del aprx