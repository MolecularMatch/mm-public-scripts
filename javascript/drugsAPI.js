var requestretry = require('requestretry')

// ////////////CONFIGS/////////////////////////////////
// ///////////////////////////////////////////////////

var apiConnectionString = 'https://api.molecularmatch.com'
var apiKey = '' // <your api key>
// or run as $ node assertionsAPI.js <key>
if (process.argv[2]) apiKey = process.argv[2]

// ///////////////////////////////////////////////////
// ///////////////////////////////////////////////////

var terms = [{'facet': 'CONDITION', 'term': 'Lung cancer'}]

requestretry({
  url: apiConnectionString + '/v4/drug/search',
  maxAttempts: 2,
  retryDelay: 50,
  method: 'POST',
  headers: {
    'content-type': 'application/json'
  },
  json: {
    apiKey: apiKey,
    filters: terms,
    mode: 'discovery' // defaults to 'criteriaunmet', which performs an assertion guided drug search (see: https://api.molecularmatch.com/#drugs)
  }
},
	function (error, response, body) {
  if (error) throw error
  if (response.statusCode == '200') {
    console.log(JSON.stringify(body))
  } else {
    console.log(response)
    console.log('statusCode: ' + response.statusCode)
  }
  process.exit()
})
