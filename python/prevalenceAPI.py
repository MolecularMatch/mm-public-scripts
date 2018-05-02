# MolecularMatch API (MM-DATA) Python Example Sheet
# Based on documentation at https://api.molecularmatch.com
# Author: Shane Neeley, MolecularMatch Inc., Jan. 30, 2018

import requests
import json
import numpy as np
import sys

mmService = "https://api.molecularmatch.com"

# CHANGE THIS TO YOUR KEY or use as paramter (e.g. $ python3 publicationsAPI.py key)
apiKey = '<your api key>'
if apiKey == '<your api key>' and sys.argv[1]:
	apiKey = sys.argv[1]

# find how prevalent a mutation is in all conditions with prevalence aggregate
# AVG will calculate average prevalence for all conditions, MAX calculates the maximum condition prevalence
url = mmService + "/v2/prevalence/aggregate"
filters = [{'facet':'MUTATION','term':'BRAF V600E'}]
payload = {
	'apiKey': apiKey,
	'type': 'AVG', # 'MAX'
	'filters': filters
}
r = requests.post(url, json=payload)
r = r.json()
print(''.join(['total aggregate average = ', str(r['aggregation']['frequency']), " (", str(r['aggregation']['count']), '/', str(r['aggregation']['samples']), ")"]))

# find how prevalent a mutation is in a single condition
url = mmService + "/v2/prevalence/aggregate"
filters = [{'facet':'MUTATION','term':'BRAF V600E'}, {'facet':'CONDITION','term':'Colorectal cancer'}]
payload = {
	'apiKey': apiKey,
	'type': 'AVG', # 'MAX'
	'filters': filters
}
r = requests.post(url, json=payload)
r = r.json()
print(''.join(['total colorecal average = ', str(r['aggregation']['frequency']), " (", str(r['aggregation']['count']), '/', str(r['aggregation']['samples']), ")"]))

# look at discrete samples with prevalence search
url = mmService + "/v2/prevalence/search"
filters = [{'facet':'MUTATION','term':'BRAF V600E'}, {'facet':'CONDITION','term':'Colorectal cancer'}]
payload = {
	'apiKey': apiKey,
	'filters': filters
}
r = requests.post(url, json=payload)
for study_record in r.json()['hits']:
	print(str(study_record['percent']) + ' percent positive in study: ' + study_record['studyId'])

# Result
# total aggregate average = 0.0572 (915/15998)
# total colorecal average = 0.103 (212/2059)
# 7.46 percent positive in study: msk_impact_2017_Colorectal_Cancer
# 8.93 percent positive in study: coadread_tcga_pub
# 1.45 percent positive in study: coadread_mskcc
# 5.56 percent positive in study: coadread_genentech
# 17.93 percent positive in study: coadread_dfci_2016
