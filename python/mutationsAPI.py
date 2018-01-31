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

# find more info on a mutation
url = mmService + "/v2/mutation/get"
payload = {
	'apiKey': apiKey,
	'name': 'BRAF V600E'
}
r = requests.get(url, params=payload)
#print(json.dumps(r.json()))

# print all genomic coordinates in .tsv format
fields = ['chr', 'start', 'stop', 'ref', 'alt', 'transcript', 'cdna', 'amino_acid_change']
print('\t'.join(fields))
for tcon in r.json()['transcriptConsequence']:
	string = ""
	for f in fields:
		string+=str(tcon[f])+'\t'
	print(string)
# Result
# chr	start	stop	ref	alt	transcript	cdna	amino_acid_change
# 7	140453136	140453136	A	T	NM_004333.4	c.1799T>A	V600E
# 7	140453135	140453136	CA	TT	NM_004333.4	c.1799_1800delTGinsAA	V600E
# 7	140453136	140453136	A	T	ENST00000288602	c.1799T>A	p.V600E
# 7	140453136	140453136	A	T	NM_004333	c.1799T>A	p.V600E
# 7	140453136	140453136	A	T	XM_005250047	c.1799T>A	p.V600E
# 7	140453136	140453136	A	T	XM_005250046	c.1799T>A	p.V600E
# 7	140453136	140453136	A	T	XM_005250045	c.1799T>A	p.V600E
# 7	140453136	140453136	A	T	CCDS5863	c.1799T>A	p.V600E

#################################

# find the parents of this mutation and perform trial searches with them
# this will bring in results for V600K, V600D and all children that fall under this parentage
print('\n\nTrial Counts')
for p in r.json()['parents']:
	url = mmService + "/v2/search/trials"
	filters = [{'facet':'MUTATION','term':p['name']}]
	payload = {
		'apiKey': apiKey,
		'filters': json.dumps(filters)
	}
	r = requests.post(url, data=payload)
	print(str(r.json()['total']) + ' trials found for parent mutation: ' + p['name'])

# Result
# Trial Counts
# 752 trials found for parent mutation BRAF exon 15 mutation
# 752 trials found for parent mutation BRAF Pkinase_Tyr domain
# 763 trials found for parent mutation BRAF V600

#################################

# What is the clinical interpretation of BRAF V600E? Are there trials, drugs, publications about it?

url = mmService + resourceURLs["mutationClassify"]
payload = {
	'apiKey': apiKey,
	'variant': 'BRAF V600E',
	'condition': 'Lung cancer'
}
r = requests.post(url, data=payload)

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
