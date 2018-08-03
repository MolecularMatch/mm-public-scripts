#################
# Trials
#################

# to run include apiKey as first argument
# $ chmod 777 file.sh
# $ ./file.sh apiKey

curl -X POST 'https://api.molecularmatch.com/v2/search/trials' \
--data "apiKey=$1" \
--data-urlencode 'filters=[{"facet":"MUTATION","term":"BRAF V600E"}, {"facet":"STATUS", "term":"Enrolling"}, {"facet":"TRIALTYPE", "term":"Interventional"}]'

curl 'https://api.molecularmatch.com/v2/search/trials' \
--data "apiKey=$1" \
--data-urlencode 'filters=[ {"facet" : "ID", "term" : "NCT03387111"}]'

curl -X POST 'https://api.molecularmatch.com/v2/search/trials' \
--data "apiKey=$1" \
--data-urlencode 'filters=[{"facet":"CONDITION","term":"cancer"},{"facet":"SITE","term":"Mammary gland"}]'
