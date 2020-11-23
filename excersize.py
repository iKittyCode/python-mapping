import requests
#import json
#import numpy

import geopandas as gpd
#import geoplot
import matplotlib.pyplot as plt

# USGS JSON description 
# https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php
myURL = "https://earthquake.usgs.gov/fdsnws/event/1/query?"
myParams = "format=geojson&starttime=2000-01-01&endtime=2020-01-02&minmagnitude=7.5"

# geopandas datasets are here 
# print(gpd.datasets.get_path('naturalearth_lowres'))
# /usr/local/lib/python3.9/site-packages/geopandas/datasets


# using a low resoluation map
world = gpd.read_file( gpd.datasets.get_path('naturalearth_lowres') )
ax = world.plot()
# plt.ion()

myRequest = requests.get(url = myURL, params = myParams)   
data = myRequest.json()

#24 features as per USGS json descriptor
print(len(data["features"]))

#iterate through all features
for i in range(0,len(data["features"])):
    print("The place of earth quake is " + data["features"][i]["properties"]["place"])
    
    #get latitude and longitude from geometry / coordinates
    lon = data["features"][i]["geometry"]["coordinates"][0]
    lat = data["features"][i]["geometry"]["coordinates"][1]

    #print(lon, lat, sep= " " )
    #plot
    ax.plot(lon ,lat, marker= ".", color="green" )
    
plt.show()
plt.ion(world)
