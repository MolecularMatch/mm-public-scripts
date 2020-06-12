# MolecularMatch API (MM-DATA) Python Example Sheet
# Based on documentation at https://api.molecularmatch.com
# Author: Shane Neeley, MolecularMatch Inc., Jan. 30, 2018

import requests
import json
import numpy as np
import sys

resourceURLs = {
    "trialSearch": "/v5/trial/search",
}
mmService = "https://api-demo.molecularmatch.com"

# CHANGE THIS TO YOUR KEY or use as parameter (e.g. $ python3 publicationsAPI.py key)
apiKey = '<your api key>'
if apiKey == '<your api key>' and sys.argv[1]:
    apiKey = sys.argv[1]

#####################search w/ paging##################################

# Example of how to get all pubs 10 at a time because there is a page limit of 10
t1s = []

page = 1
limit = 10
start = 0
url = mmService + resourceURLs["trialSearch"]
q = 'colon carcinoma KRAS'
filters = [{"facet": "TRIALTYPE", "term": "Interventional"},
           {"facet": "TRIALSTATUS", "term": "Enrolling"}]
payload = {
    'apiKey': apiKey,
    'query': q,
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
        t1s.append(trial['id'])

################################

t2s = []
page = 1
limit = 10
start = 0
url = mmService + resourceURLs["trialSearch"]
q = 'colon carcinoma KRAS G12C'
filters = [{"facet": "TRIALTYPE", "term": "Interventional"},
           {"facet": "TRIALSTATUS", "term": "Enrolling"}]
payload = {
    'apiKey': apiKey,
    'query': q,
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
        t2s.append(trial['id'])

################################

for t in t2s:
    if t not in t1s:
        print(t, ' from second not in first')

for t in t1s:
    if t not in t2s:
        print(t, ' from first not in second')
