# MolecularMatch API (MM-DATA) Python Example Sheet
# Based on documentation at https://api.molecularmatch.com
# Author: Shane Neeley, MolecularMatch Inc., Jan. 30, 2018

import requests
import json
import sys

resourceURLs = {
	"assertionSearch": "/v2/search/assertions",
	"assertionExport": "/v2/export/assertions",
}
mmService = "https://api.molecularmatch.com"

# CHANGE THIS TO YOUR KEY or use as paramter (e.g. $ python3 publicationsAPI.py key)
apiKey = '<your api key>'
if apiKey == '<your api key>' and sys.argv[1]:
	apiKey = sys.argv[1]

# Note, conditions have to be added to your key before this will work. Customers pay per condition.

#################### search ##################################

url = mmService + resourceURLs["assertionSearch"]
filters = [{'facet':'CONDITION','term':'Lung cancer'}]
#filters = [{'facet':'CONDITION','term':'Breast cancer'}]
#filters = [{'facet':'CONDITION','term':'Colorectal cancer'}]
payload = {
	'apiKey': apiKey,
	'filters': json.dumps(filters)
}
r = requests.post(url, json=payload)
#print(json.dumps(r.json()))

#################### export csv ##################################

url = mmService + resourceURLs["assertionExport"]
payload = {
	'apiKey': apiKey,
	'format': 'csv',
	'condition': 'Neoplasm of lung',
	#'condition': 'Neoplasm of breast',
	#'condition': 'Neoplasm of colorectum',
}
r = requests.post(url, data=payload)
with open('data.csv', 'w') as f:
    f.write(r.text)

#################### export json ##################################

url = mmService + resourceURLs["assertionExport"]
payload = {
	'apiKey': apiKey,
	'format': 'json',
	'condition': 'Neoplasm of lung',
	#'condition': 'Neoplasm of breast',
	#'condition': 'Neoplasm of colorectum',
}
r = requests.post(url, data=payload)
with open('data.json', 'w') as f:
	f.write(r.text)
