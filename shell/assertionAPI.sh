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
curl "https://api.molecularmatch.com/v2/export/assertions?apiKey=$1" --data 'condition=Malignant tumor of lung' --data 'format=csv' -o data1.csv

curl "https://api.molecularmatch.com/v2/export/assertions?apiKey=$1" --data 'condition=Malignant tumor of breast' --data 'format=csv' -o data2.csv

curl "https://api.molecularmatch.com/v2/export/assertions?apiKey=$1" --data 'condition=Malignant tumor of colon' --data 'format=csv' -o data3.csv

# format=json
curl "https://api.molecularmatch.com/v2/export/assertions?apiKey=$1" --data 'condition=Malignant tumor of breast' --data 'format=json' -o data4.json

curl "https://api.molecularmatch.com/v2/export/assertions?apiKey=$1" --data 'condition=Malignant tumor of colon' --data 'format=json' -o data5.json

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
