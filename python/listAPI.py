
import requests
import json
import numpy as np
import sys
import time

mmService = "https://api.molecularmatch.com/v2"

# CHANGE THIS TO YOUR KEY or use as parameter (e.g. $ python3 listAPI.py key)
apiKey = '<your api key>'
if apiKey == '<your api key>' and sys.argv[1]:
	apiKey = sys.argv[1]

# endpoints for listing our semi-static data
# Note, this endpoint is not activated yet (as of 05/07/18)
eps = [
	'/trialtype/list',
    '/trialphase/list',
    '/ecog/list',
    '/trialstatus/list',
    '/gender/list',
    '/city/list',
    '/state/list',
    '/country/list',
    '/stage/list',
    '/publicationtype/list',
    '/journal/list'
]

for ep in eps:
	time.sleep(0.5)
	url = mmService + ep
	payload = {
		'apiKey': apiKey
	}
	r = requests.get(url, params=payload)
	r = r.json()
	print('\n\nENDPOINT: ' + ep)
	print(r)




#
