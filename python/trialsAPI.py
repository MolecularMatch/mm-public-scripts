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

#### Mutation details lookup

# So you want to know everything there is to know about BRAF V600E?

url = mmService + resourceURLs["mutationGet"]
payload = {
	'apiKey': apiKey,
	'name': 'BRAF V600E'
}
r = requests.get(url, params=payload)

# Question: what databases have reported this mutation?
print(r.json()['sources'])
# Answer: 'COSMIC', 'CIViC', 'DoCM', 'cBioPortal', 'ClinVar'

# Question: is there a known protein domain this mutation is in?
for i in r.json()['parents']:
	if (i['type'] == 'domain'):
		print(i)
# Answer: BRAF Pkinase_Tyr domain (protein tyrosine kinase domain)

# What is the clinical interpretation of BRAF V600E? Are there trials, drugs, publications about it?

url = mmService + resourceURLs["mutationClassify"]
payload = {
	'apiKey': apiKey,
	'variant': 'BRAF V600E',
	'condition': 'Lung cancer'
}
r = requests.post(url, json=payload)

# Question: How does MolecularMatch classify this mutation in this condition?
print(r.json()['classifications'][0]['classification'])
# Answer: actionable

# Question: How many drugs approved and on label for the condition provided?
print(r.json()['classifications'][0]['drugsApprovedOnLabelCount'])
# Answer: 0

# Question: How many drugs approved but off-label for the condition provided?
print(r.json()['classifications'][0]['drugsApprovedOffLabelCount'])
# Answer: 6

# Question: What about experimental drugs?
print(r.json()['classifications'][0]['drugsExperimentalCount'])
# Answer: 4

# Question: How many clinical trials are open for this mutation and condition?
print(r.json()['classifications'][0]['trialCount'])
# Answer: 24

# Question: Is there a lot of research publications about this mutation in this condition?
print(r.json()['classifications'][0]['publicationCount'])
# Answer: 47

# Question: Ok, what are these 4 experimental drugs?
url = mmService + resourceURLs["drugSearch"]
# set geneExpand for Drug to False so drugs return only for V600E, not BRAF (see https://api.molecularmatch.com/#geneExpansion)
filters = [
	{'facet':'CONDITION','term':'Lung cancer'},
	{'facet':'MUTATION','term':'BRAF V600E', "geneExpand": {"Drug": False}}
]
payload = {
	'apiKey': apiKey,
	'filters': filters,
	'mode': 'discovery'
}
r = requests.post(url, json=payload)
for drug in r.json()['rows']:
	print(drug)
	if drug['approved'] == False:
		print(drug['name'])

# Answer:
# Lgx818
# Plx8394
# BGB-283
# Cep-32496

##################################################################
#####################BASIC QUERIES################################
##################################################################

####################search drugs##################################

url = mmService + resourceURLs["drugSearch"]
filters = [{'facet':'CONDITION','term':'Lung cancer'}]
payload = {
	'apiKey': apiKey,
	'filters': filters,
	'mode': 'discovery' # 'criteriaunmet' # multiple modes avaiable for drugsearch. see api docs.
}
r = requests.post(url, json=payload)
print(json.dumps(r.json()))

#####################search trials##################################

url = mmService + resourceURLs["trialSearch"]
filters = [{'facet':'CONDITION','term':'Lung cancer'}]
payload = {
	'apiKey': apiKey,
	'filters': filters
}
r = requests.post(url, json=payload)
print(json.dumps(r.json()))

# Search trials by various ID types
filters = [
	{"facet":"ID","term":"EUDRACT2017-003305-18"}
]
payload = {
	'apiKey': apiKey,
	'filters': filters
}
r = requests.post(url, json=payload)
print('r here')
print(r.json())

#####################search publications#############################

url = mmService + resourceURLs["publicationSearch"]
filters = [{'facet':'CONDITION','term':'Lung cancer'}]
payload = {
	'apiKey': apiKey,
	'filters': filters
}
r = requests.post(url, json=payload)
print(json.dumps(r.json()))

####################get mutation###################################

url = mmService + resourceURLs["mutationGet"]
payload = {
	'apiKey': apiKey,
	'name': 'BRAF V600E'
}
r = requests.get(url, params=payload)
print(json.dumps(r.json()))

######################get gene#################################

url = mmService + resourceURLs["geneGet"]
payload = {
	'apiKey': apiKey,
	'symbol': 'BRAF'
}
r = requests.get(url, params=payload)
print(json.dumps(r.json()))

######################classify mutation##############################

url = mmService + resourceURLs["mutationClassify"]
payload = {
	'apiKey': apiKey,
	'variant': 'EGFR T790M',
	'condition': 'Lung cancer'
}
r = requests.post(url, json=payload)
print(json.dumps(r.json()))
