#################
# Drugs
#################

# to run include apiKey as first argument
# $ chmod 777 file.sh
# $ ./file.sh apiKey
# --data "mode=discovery" set for a regular drug search, not assertion evidence guided drug search (--data "mode=criteriaunmet" \

curl 'https://api.molecularmatch.com/v4/drug/search' \
--data "apiKey=$1" \
--data "mode=discovery" \
--data-urlencode 'filters=[{"facet" : "DRUGCLASS", "term" : "Chemotherapy"}, {"facet" : "CONDITION", "term" : "Osteosarcoma"}]'

curl 'https://api.molecularmatch.com/v4/drug/search' \
--data "apiKey=$1" \
--data "mode=discovery" \
--data-urlencode 'filters=[{"facet" : "DRUGCLASS", "term" : "Chemotherapy"}]'

curl 'https://api.molecularmatch.com/v4/drug/search' \
--data "apiKey=$1" \
--data "mode=discovery" \
--data-urlencode 'filters=[{"facet" : "DRUG", "term" : "Tarceva"}]'

curl 'https://api.molecularmatch.com/v4/drug/search' \
--data "apiKey=$1" \
--data "mode=discovery" \
--data-urlencode 'filters=[{"facet" : "DRUG", "term" : "Erlotinib"}]'
