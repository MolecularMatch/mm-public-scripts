#################
# Assertions
#################

# Get a key that has assertion sets activated
# to run include apiKey as first argument
# $ chmod 777 file.sh
# $ ./file.sh apiKey

#################
# Export the assertion datasets into a .csv
#################

# format=csv
curl "https://api.molecularmatch.com/v2/export/assertions?apiKey=$1" --data 'condition=Neoplasm of lung' --data 'format=csv' -o data.csv

curl "https://api.molecularmatch.com/v2/export/assertions?apiKey=$1" --data 'condition=Neoplasm of breast' --data 'format=csv' -o data.csv

curl "https://api.molecularmatch.com/v2/export/assertions?apiKey=$1" --data 'condition=Neoplasm of colorectum' --data 'format=csv' -o data.csv

# format=json
curl "https://api.molecularmatch.com/v2/export/assertions?apiKey=$1" --data 'condition=Neoplasm of breast' --data 'format=json' -o data.json

curl "https://api.molecularmatch.com/v2/export/assertions?apiKey=$1" --data 'condition=Neoplasm of colorectum' --data 'format=json' -o data.json

#################
# Search, return all assertions that have to do with BRAF V600E
#################

curl -X POST 'https://api.molecularmatch.com/v2/search/assertions' \
--data "apiKey=$1" \
--data-urlencode 'filters=[{"facet":"MUTATION","term":"BRAF V600E"}]'

#################
# Search, return all assertions that have to do with BRAF and are resistance assertions
#################

curl -X POST 'https://api.molecularmatch.com/v2/search/assertions' \
--data "apiKey=$1" \
--data-urlencode 'filters=[{"facet":"GENE","term":"BRAF"},{"facet":"CLINICAL_SIGNIFICANCE","term":"resistant"}]'
