#################
# Publications
#################

# to run include apiKey as first argument
# $ chmod 777 file.sh
# $ ./file.sh apiKey

curl -X POST 'https://api.molecularmatch.com/v4/publication/search' \
--data "apiKey=$1" \
--data-urlencode 'filters=[{"facet":"MUTATION","term":"BRAF V600E"}]'

curl 'https://api.molecularmatch.com/v4/publication/search' \
--data "apiKey=$1" \
--data-urlencode 'filters=[ {"facet" : "ID", "term" : "25265492"}]'

# publication details with GET
curl -G "https://api.molecularmatch.com/v4/publication/25265492?apiKey=$1"
