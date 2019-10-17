#################
# Publications
#################

# to run include apiKey as first argument
# $ chmod 777 file.sh
# $ ./file.sh apiKey

curl -X POST 'https://api.molecularmatch.com/v3/search/publications' \
--data "apiKey=$1" \
--data-urlencode 'filters=[{"facet":"MUTATION","term":"BRAF V600E"}]'

curl 'https://api.molecularmatch.com/v3/search/publications' \
--data "apiKey=$1" \
--data-urlencode 'filters=[ {"facet" : "ID", "term" : "25265492"}]'

curl -G "https://api.molecularmatch.com/v3/publications/25265492?apiKey=$1"
