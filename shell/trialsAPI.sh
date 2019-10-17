#################
# Trials
#################

# to run include apiKey as first argument
# $ chmod 777 file.sh
# $ ./file.sh apiKey

# typical trial search w/ molecular info
curl -X POST 'https://api.molecularmatch.com/v3/search/trials' \
--data "apiKey=$1" \
--data-urlencode 'filters=[{"facet":"MUTATION","term":"BRAF V600E"}, {"facet":"STATUS", "term":"Enrolling"}, {"facet":"TRIALTYPE", "term":"Interventional"}]'

# filter for a single trial by ID search
curl 'https://api.molecularmatch.com/v3/search/trials' \
--data "apiKey=$1" \
--data-urlencode 'filters=[ {"facet" : "ID", "term" : "NCT03387111"}]'

# break condition search into all cancer trials tagged with a site of breast (mammary gland)
curl -X POST 'https://api.molecularmatch.com/v3/search/trials' \
--data "apiKey=$1" \
--data-urlencode 'filters=[{"facet":"CONDITION","term":"cancer"},{"facet":"SITE","term":"Breast"}]'

# case w/ age and gender
curl -X POST 'https://api.molecularmatch.com/v3/search/trials' \
--data "apiKey=$1" \
--data-urlencode 'filters=[{"facet":"AGE","term":"44"},{"facet":"CONDITION","term":"Invasive Ductal Carcinoma"},{"facet":"PHRASE","term":"chemotherapy"},{"facet":"STAGE","term":"Stage 2"},{"facet":"GENDER","term":"Female"},{"facet":"SITE","term":"breast"}]'

# regular medicalgroup + trial status search (doesn't guarantee locations for medicalgroup are enrolling)
# e.g., may be sponsored my M.D. Anderson, but trial takes place at a non-affiliated clinic
curl -X POST 'https://api.molecularmatch.com/v3/search/trials' \
--data "apiKey=$1" \
--data-urlencode 'filters=[{"facet":"STATUS","term":"Enrolling"}, {"facet":"MEDICALGROUP","term":"MD Anderson"}]'

# nested medicalgroup on location, and status on location search (guarantees locations for medicalgroup are enrolling)
# e.g. trial site is located at an MD Anderson facility, and this site is marked as enrolling
# see https://api.molecularmatch.com/#domainLocationMedicalGroup
curl -X POST 'https://api.molecularmatch.com/v3/search/trials' \
--data "apiKey=$1" \
--data-urlencode 'filters=[{"facet":"LOCATIONSTATUS","term":"Enrolling"}, {"facet":"LOCATIONMEDICALGROUP","term":"MD Anderson"}]'
