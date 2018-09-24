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

# search publications by condition and variant (find evidence for a patient)

# Example of how to get all pubs 10 at a time because there is a page limit of 10
page = 1
limit = 10
start = 0

url = mmService + "/v2/search/publications"
filters = [
	{'facet':'CONDITION','term':'Glioblastoma'},
	# {'facet':'MUTATION','term':'IDH1 c.394C>T'},
	# {'facet':'MUTATION','term':'IDH2 c.514A>G'}
]
payload = {
	'apiKey': apiKey,
	'filters': filters,
	'start': start,
	'limit': limit
}
# perform first request to get total
r = requests.post(url, json=payload)
total = r.json()['total']

# now go through them all 10 at a time
myrange = range(0, total, limit)
for count in myrange:
	payload['start'] = count
	r = requests.post(url, json=payload)

	for pub in r.json()['rows']:
		print(pub['link'])

# Result
# http://www.ncbi.nlm.nih.gov/pubmed/24549719
# http://www.ncbi.nlm.nih.gov/pubmed/22309944
# http://www.ncbi.nlm.nih.gov/pubmed/21641335
# http://www.ncbi.nlm.nih.gov/pubmed/19378339
# http://www.ncbi.nlm.nih.gov/pubmed/19915015
# http://www.ncbi.nlm.nih.gov/pubmed/23370430
# http://www.ncbi.nlm.nih.gov/pubmed/19117336
# ...
