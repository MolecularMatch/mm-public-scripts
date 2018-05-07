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
# Note, this endpoint is not activated yet (as of 05/07/18)
url = mmService + "/v2/condition/search"
filters = [{'facet':'NAME','term':'Neoplasm of lung'}]
payload = {
	'apiKey': apiKey,
	'filters': filters
}
r = requests.post(url, json=payload)
print(r.json())
