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

curl -X POST 'https://api.molecularmatch.com/v2/search/trials' \
--data "apiKey=$1" \
--data-urlencode 'filters=[{"term":"Recruiting","facet":"LOCATIONSTATUS"},{"term":"Interventional","facet":"TRIALTYPE"},{"term":"EGFR p.L747_P753del","facet":"MUTATION"},{"term":"EGFR p.T790M","facet":"MUTATION"},{"term":"EGFR p.L858R","facet":"MUTATION"},{"term":"KRAS p.G12V","facet":"MUTATION"},{"term":"NRAS p.Q61K","facet":"MUTATION"},{"term":"ERBB2 p.Y772_A775dup","facet":"MUTATION"},{"term":"BRAF p.L597R","facet":"MUTATION"},{"term":"Phase 2","facet":"PHASE"},{"term":"Phase 3","facet":"PHASE"},{"term":"Phase 4","facet":"PHASE"},{"term":"Non-small cell lung carcinoma","facet":"CONDITION"}]'

curl -X POST 'https://api.molecularmatch.com/v2/search/trials' \
--data "apiKey=$1" \
--data-urlencode 'filters=[{"facet":"AGE","term":"44"},{"facet":"CONDITION","term":"Invasive Ductal Carcinoma"},{"facet":"PHRASE","term":"chemotherapy"},{"facet":"STAGE","term":"Stage 2"},{"facet":"GENDER","term":"Female"},{"facet":"SITE","term":"breast"}]'
