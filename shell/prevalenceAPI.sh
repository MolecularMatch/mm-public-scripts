#################
# Variant Prevalence
#################

# to run include apiKey as first argument
# $ chmod 777 file.sh
# $ ./file.sh apiKey


curl -X POST 'https://api-demo.molecularmatch.com/v2/aggregate/prevalence' \
-H "Content-Type:application/json" \
-H "Authorization: Bearer $1" \
-d '{
    "type": "AVG",
    "filters": [
        {
            "facet":"MUTATION",
            "term":"BRAF V600E"
        }
    ]
}'


curl -X POST 'https://api-demo.molecularmatch.com/v2/prevalence/search' \
-H "Content-Type:application/json" \
-H "Authorization: Bearer $1" \
-d '{
    "filters": [
        {
            "facet":"MUTATION",
            "term":"BRAF V600E"
        }
    ]
}'
