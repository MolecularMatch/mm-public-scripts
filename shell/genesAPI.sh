#################
# Genes
#################

# to run include apiKey as first argument
# $ chmod 777 file.sh
# $ ./file.sh apiKey

curl -G "https://api.molecularmatch.com/v2/gene/get" \
-H "Authorization: Bearer $1" \
--data-urlencode "symbol=BRAF"
