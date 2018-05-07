# MolecularMatch API (MM-DATA) Python Example Sheet
# Based on documentation at https://api.molecularmatch.com
# Author: Shane Neeley, MolecularMatch Inc., Jan. 30, 2018

import requests
import json
import numpy as np
import sys


mmService = "https://api.molecularmatch.com"

# CHANGE THIS TO YOUR KEY or use as parameter (e.g. $ python3 publicationsAPI.py key)
apiKey = '<your api key>'
if apiKey == '<your api key>' and sys.argv[1]:
	apiKey = sys.argv[1]

#####################search trials and plot geolocations##################################

url = mmService + "/v2/search/trials"
filters = [
	{'facet':'CONDITION','term':'Lung cancer'},
	{'facet':'COUNTRY','term':'United States'},
	{'facet':'COUNTRY','term':'Mexico'},
	{'facet':'COUNTRY','term':'Canada'},
	{'facet':'STATUS','term':'Enrolling'}
]
payload = {
	'apiKey': apiKey,
	'filters': filters
}
r = requests.post(url, json=payload)
r = r.json()

# follow instructions to install basemap:
# https://stackoverflow.com/questions/42299352/installing-basemap-on-mac-python
# map based on: https://matplotlib.org/basemap/users/mapcoords.html
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
# setup Lambert Conformal basemap.
m = Basemap(width=12000000,height=9000000,projection='lcc',
            resolution='c',lat_1=45.,lat_2=55,lat_0=50,lon_0=-107.)
# draw a boundary around the map, fill the background.
# this background will end up being the ocean color, since
# the continents will be drawn on top.
m.drawmapboundary(fill_color='aqua')
# fill continents, set lake color same as ocean color.
m.fillcontinents(color='coral',lake_color='aqua')
# draw parallels and meridians.
# label parallels on right and top
# meridians on bottom and left
parallels = np.arange(0.,81,10.)
# labels = [left,right,top,bottom]
m.drawparallels(parallels,labels=[False,True,True,False])
meridians = np.arange(10.,351.,20.)
m.drawmeridians(meridians,labels=[True,False,False,True])

# get points from MolecularMatch
# for all results, need to page through
for trial in r['rows']:
	# just take some from each trial or too much to plot
	for loc in trial['locations'][0:1000]:
		try:
			lon, lat = loc['geo']['lon'], loc['geo']['lat']
			print(lon,lat)
			# convert to map projection coords.
			# Note that lon,lat can be scalars, lists or numpy arrays.
			xpt,ypt = m(lon,lat)
			# convert back to lat/lon
			lonpt, latpt = m(xpt,ypt,inverse=True)
			m.plot(xpt,ypt,'bo', markersize=2)  # plot a blue dot there
			# put some text next to the dot, offset a little bit
			# (the offset is in map projection coordinates)
			# plt.text(xpt+100000,ypt+100000,loc['name'])
		except:
			continue

plt.suptitle("Clinical Trial Sites for Lung Cancer", fontsize=20)
plt.show()
