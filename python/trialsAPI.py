# MolecularMatch API (MM-DATA) Python Example Sheet
# Based on documentation at https://api.molecularmatch.com
# Author: Shane Neeley, MolecularMatch Inc., Jan. 30, 2018

import requests
import json
import numpy as np
import sys

resourceURLs = {
	"trialSearch": "/v2/search/trials",
	"drugSearch": "/v2/search/drugs",
	"publicationSearch": "/v2/search/publications",
	"mutationGet": "/v2/mutation/get",
	"geneGet": "/v2/gene/get",
	"mutationClassify": "/v2/mutation/classify",
	"validateTerms": "/v2/validate/terms",
	"assertionSearch": "/v2/search/assertions",
	"assertionExport": "/v2/export/assertions"
}
mmService = "https://api.molecularmatch.com"

# CHANGE THIS TO YOUR KEY or use as parameter (e.g. $ python3 publicationsAPI.py key)
apiKey = '<your api key>'
if apiKey == '<your api key>' and sys.argv[1]:
	apiKey = sys.argv[1]

#// TODO: geolocation searches

#####################search trials##################################

url = mmService + resourceURLs["trialSearch"]
filters = [{'facet':'CONDITION','term':'Lung cancer'}]
payload = {
	'apiKey': apiKey,
	'filters': filters
}
r = requests.post(url, json=payload)
print(json.dumps(r.json()))

#####################search w/ paging##################################

# Example of how to get all pubs 10 at a time because there is a page limit of 10
page = 1
limit = 10
start = 0
url = mmService + resourceURLs["trialSearch"]
filters = [{'facet':'CONDITION','term':'Lung cancer'}, {'facet':'GENE','term':'BRAF'}]
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
	for trial in r.json()['rows']:
		print(trial['link'])

# Output
# http://clinicaltrials.gov/ct2/show/NCT03533127
# http://clinicaltrials.gov/ct2/show/NCT03456063
# http://clinicaltrials.gov/ct2/show/NCT03428022
# ...

##################################################################
#####################SCENARIOS####################################
##################################################################

#### Clinical trial reporting

# When looking up trials for an actual patient, it is important to include the filters of Enrolling and Interventional
url = mmService + resourceURLs["trialSearch"]
filters = [
	{"facet":"CONDITION","term":"Colorectal cancer"},
	{"facet":"MUTATION","term":"BRAF V600E"},
	{"facet":"STATUS", "term":"Enrolling"},
	{"facet":"TRIALTYPE", "term":"Interventional"},
	{"facet":"COUNTRY", "term":"France"}
]
payload = {
	'apiKey': apiKey,
	'filters': filters
}
r = requests.post(url, json=payload)

# Question: how many trials for a patient with this mutation and disease are interventional and enrolling in France?
print(r.json()['total'])
# Answer: 4

# Question: what are these trials ClinicalTrials.gov IDs and titles and email addresses for contact?
for i in np.arange(0, len(r.json()['rows']) ):
	print(r.json()['rows'][i]['id'])
	print(r.json()['rows'][i]['briefTitle'])
	print(r.json()['rows'][i]['overallContact'])
# Answer:
# NCT02291289 - A Multi-Center Study of Biomarker-Driven Therapy in Metastatic Colorectal Cancer - global.rochegenentechtrials@roche.com
# NCT01677741 - A Study to Determine Safety, Tolerability and Pharmacokinetics of Oral Dabrafenib In Children and Adolescent Subjects - GSKClinicalSupportHD@gsk.com
# NCT02788279 - A Study to Investigate Efficacy and Safety of Cobimetinib Plus Atezolizumab and Atezolizumab Monotherapy Versus Regorafenib in Participants With Metastatic Colorectal Adenocarcinoma - global.rochegenentechtrials@roche.com
# NCT02751177 - Detection of KRAS, NRAS et BRAF Mutations in Plasma Circulating DNA From Patients With Metastatic Colorectal Cancer - v.gillon@nancy.unicancer.fr

# Question: what are all the mutations that are associated with trial NCT02291289?
filters = [
	{"facet":"ID","term":"NCT02291289"}
]
payload = {
	'apiKey': apiKey,
	'filters': filters
}
r = requests.post(url, json=payload)
# Note: must have tags activated on api key for this to work. Not all api key users get tags.
for tag in r.json()['rows'][0]['tags']:
	if tag['facet'] == "MUTATION":
		print(tag)

# Answer:
# 3 mutations are for inclusion criteria
# {'facet': 'MUTATION', 'term': 'EGFR P546S', 'alias': 'EGFR P546S', 'priority': '0', 'filterType': 'include'}
# {'facet': 'MUTATION', 'term': 'BRAF V600E', 'alias': 'BRAF V600E', 'priority': '0', 'filterType': 'include'}
# {'facet': 'MUTATION', 'term': 'Microsatellite instability', 'alias': 'Microsatellite instability', 'priority': '0', 'filterType': 'include'}
# 2 mutations are for exclusion criteria (filterType = 'exclude')
# {'facet': 'MUTATION', 'term': 'EGFR S492R', 'alias': 'EGFR S492R', 'priority': 1, 'filterType': 'exclude'}
# {'facet': 'MUTATION', 'term': 'BRAF G469L', 'alias': 'BRAF G469L', 'priority': 1, 'filterType': 'exclude'}

# See more about the trial data model at: https://api.molecularmatch.com/#trialDataModel

#####################search w/ medicalgroups##################################

# MEDICALGROUP filter will find trials by a sponsor or location
# LOCATIONMEDICALGROUP filter will find trials by location (trial site) only, and can be combined
# w/ "CITY", "STATE", "COUNTRY", "LOCATIONSTATUS", "DISTANCE" to make a nested search on the locations
# see https://api.molecularmatch.com/#domainLocationMedicalGroup

MGs = [
	"Washington University",
	"Pfizer",
	"Universitätsspital Basel"
]
for id in MGs:
    # a regular search
	# regular medicalgroup + trial status search (doesn't guarantee locations for medicalgroup are enrolling)
	# e.g., may be sponsored my M.D. Anderson, but trial takes place at a non-affiliated clinic
    filters = [
        {'facet': 'MEDICALGROUP', 'term': id},
        {'facet': 'STATUS', 'term': 'Enrolling'},
    ]
    payload = {
        'apiKey': apiKey, 'filters': filters
    }
    r = requests.post(url, json=payload).json()
    totalregular = str(r['total'])

    # now try nested
	# nested medicalgroup on location, and status on location search (guarantees locations for medicalgroup are enrolling)
	# e.g. trial site is located at an MD Anderson facility, and this site is marked as enrolling
    filters = [
        {'facet': 'LOCATIONMEDICALGROUP', 'term': id},
        {'facet': 'LOCATIONSTATUS', 'term': 'Enrolling'},
    ]
    payload = {
        'apiKey': apiKey, 'filters': filters
    }
    r = requests.post(url, json=payload).json()
    totalnested = str(r['total'])

    print('\t'.join([id, totalregular, totalnested]))
