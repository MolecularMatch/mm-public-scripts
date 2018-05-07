#################
# Trials
#################

# to run include apiKey as first argument
# $ chmod 777 file.sh
# $ ./file.sh apiKey

# List our semi-static data
# Note, this endpoint is not activated yet (as of 05/07/18)

curl -X GET 'https://api.molecularmatch.com/v2/list/ecog' \
--data "apiKey=$1"

curl -X GET 'https://api.molecularmatch.com/v2/list/trialstatus' \
--data "apiKey=$1"

# endpoints
# '/trialtype/list'
# '/trialphase/list'
# '/ecog/list'
# '/trialstatus/list'
# '/gender/list'
# '/city/list'
# '/state/list'
# '/country/list'
# '/stage/list'
# '/publicationtype/list'
# '/journal/list'
