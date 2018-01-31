#################
# Mutations
#################

# to run include apiKey as first argument
# $ chmod 777 file.sh
# $ ./file.sh apiKey

# When you have the amino acid change:
curl -G "https://api.molecularmatch.com/v2/mutation/get" \
-H "Authorization: Bearer $1" \
--data-urlencode "name=BRAF V600E"

# If you have genomic coordinates:
curl -G "https://api.molecularmatch.com/v2/mutation/get" \
-H "Authorization: Bearer $1" \
--data "chr=7" \
--data "start=55242483" \
--data "stop=55242506" \
--data "ref=ATCTCCGAAAGCCAACAAGGAAAT" \
--data "alt=-"

# If you have gene and pdot (amino acid change):
curl -G "https://api.molecularmatch.com/v2/mutation/get" \
-H "Authorization: Bearer $1" \
--data-urlencode "gene=BRAF" \
--data-urlencode "pdot=p.V600E"

# If you have gene and cdot (cdna change):
curl -G "https://api.molecularmatch.com/v2/mutation/get" \
-H "Authorization: Bearer $1" \
--data-urlencode "gene=BRAF" \
--data-urlencode "cdot=c.1799T>A"
