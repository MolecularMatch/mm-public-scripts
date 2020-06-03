# MolecularMatch API (MM-DATA) Python Example Sheet
# Based on documentation at https://api.molecularmatch.com
# Author: Shane Neeley, MolecularMatch Inc., Jan. 30, 2018

import requests
import json
import numpy as np
import sys

mmService = "https://api.molecularmatch.com"

# CHANGE THIS TO YOUR KEY or use as parameter (e.g. $ python3 script.py key)
apiKey = '<your api key>'
if apiKey == '<your api key>' and sys.argv[1]:
	apiKey = sys.argv[1]

# search drugs by condition
url = mmService + "/v4/drug/search"
filters = [{'facet':'CONDITION','term':'Lung cancer'}]
payload = {
	'mode': 'discovery',
	'apiKey': apiKey,
	'filters': filters
}
r = requests.post(url, json=payload)
print(r.json())

# search drugs by the drug name

url = mmService + "/v4/drug/search"
filters = [{'facet':'DRUG','term':'nivolumab'}]
payload = {
	'mode': 'discovery',
	'apiKey': apiKey,
	'filters': filters
}
r = requests.post(url, data=payload)
# print(r.json())

# search drugs by the drug class
# find chemotherapy drugs

url = mmService + "/v4/drug/search"
filters = [
	{'facet':'DRUGCLASS','term':'Chemotherapy'}
]
payload = {
	'mode': 'discovery',
	'apiKey': apiKey,
	'filters': filters
}
r = requests.post(url, json=payload)
print(r.json())
