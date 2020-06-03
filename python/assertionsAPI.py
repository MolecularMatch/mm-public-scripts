# MolecularMatch API (MM-DATA) Python Example Sheet
# Based on documentation at https://api.molecularmatch.com
# Author: Shane Neeley, MolecularMatch Inc., Sep. 26, 2018

import requests
import json
import sys

url = 'https://api.molecularmatch.com/v4/assertion/search'

# CHANGE THIS TO YOUR KEY or use as parameter (e.g. $ python3 publicationsAPI.py key)
apiKey = '<your api key>'
if apiKey == '<your api key>' and sys.argv[1]:
	apiKey = sys.argv[1]

#################### search ##################################

# Scenario: Looking for treatments with `supporting` evidence
# where the `biomarker` provided is `predictive` of drug `sensitivity`.

filters = [
	{
		"facet":"ASSERTION-DIRECTION",
		"term":"supports" # can be: Supports, Does Not Support
	},
	{
		"facet":"BIOMARKER_CLASS",
		"term":"predictive" # can be: Predictive/Theranostic, Diagnostic, Prognostic, Unknown
	},
	{
		"facet":"CLINICAL_SIGNIFICANCE",
		"term":"sensitive" # can be: Resistant, No Response, Sensitive, Favorable, Unfavorable, Unknown
	},
	{
		"facet":"MUTATION",
		"term":"BRAF V600E"
	},
	{
		"facet":"CONDITION",
		"term":"Lung cancer"
	}
]

payload = {
	'apiKey': apiKey,
	'filters': json.dumps(filters),
	'tieringTemplate': 'AMPCAP', # or MVLD
	'mode': 'strict' # or criteriaunmet
}
r = requests.post(url, json=payload)
print(json.dumps(r.json()))

#################### simple search w/ paging ###########################

# Scenario: just show me all AML assertions
# For more than 10 results, you must perform a query for each page of results.

filters = [{'facet':'CONDITION','term':"Acute myeloid leukemia"}]
payload = {
	'apiKey': apiKey,
	'filters': filters,
	'start': 0,
	'limit': 10, # max limit = 10 records
	'mode': 'strict',
	'tieringTemplate': 'AMPCAP'
}
# perform first request to get total
r = requests.post(url, json=payload)
total = r.json()['total'] * r.json()['totalPages'] # TODO: bug - 'total' should have total of all rows

# now go through them all 10 at a time
myrange = range(0, total, payload['limit'])
for count in myrange:
	payload['start'] = count
	r = requests.post(url, json=payload)
	for assertion in r.json()['rows']:
		print(assertion['narrative'])

# Result:
# IDH1 R132G confers sensitivity to Ag-120 in patients with Acute myeloid leukemia
# IDH1 R132S confers sensitivity to Ag-120 in patients with Acute myeloid leukemia
# NPM1 W288Lfs*12 is Prognostic in patients with Acute myeloid leukemia
# FLT3 D593_F594insSPEDNEYFYVD confers sensitivity to Quizartinib in patients with Acute myeloid leukemia
# ...

##############################################################



##############################################################
