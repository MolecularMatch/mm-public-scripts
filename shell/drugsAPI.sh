#################
# Drugs
#################

# to run include apiKey as first argument
# $ chmod 777 file.sh
# $ ./file.sh apiKey

curl 'https://api.molecularmatch.com/v2/search/drugs' \
--data "apiKey=$1" \
--data-urlencode 'filters=[{"facet" : "DRUGCLASS", "term" : "Chemotherapy"}, {"facet" : "CONDITION", "term" : "Osteosarcoma"}]'

curl 'https://api.molecularmatch.com/v2/search/drugs' \
--data "apiKey=$1" \
--data-urlencode 'filters=[{"facet" : "DRUGCLASS", "term" : "Chemotherapy"}]'

curl 'https://api.molecularmatch.com/v2/search/drugs' \
--data "apiKey=$1" \
--data-urlencode 'filters=[{"facet" : "DRUG", "term" : "Tarceva"}]'

curl 'https://api.molecularmatch.com/v2/search/drugs' \
--data "apiKey=$1" \
--data-urlencode 'filters=[{"facet" : "DRUG", "term" : "Erlotinib"}]'
