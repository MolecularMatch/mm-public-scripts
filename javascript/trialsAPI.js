var requestretry = require('requestretry')
var async = require('async')

// ////////////CONFIGS/////////////////////////////////
// ///////////////////////////////////////////////////

var apiConnectionString = 'https://api.molecularmatch.com'
var apiKey = '' // <your api key>
// or run as $ node assertionsAPI.js <key>
if (process.argv[2]) apiKey = process.argv[2]

// ///////////////////////////////////////////////////
// ///////////////////////////////////////////////////

var terms = [{
  'facet': 'CONDITION',
  'term': 'Lung cancer'
}, {
  'facet': 'MUTATION',
  'term': 'KRAS G12C'
},
  {
    'facet': 'STATUS',
    'term': 'Recruiting'
  },
  {
    'facet': 'TRIALTYPE',
    'term': 'Interventional'
  }
]

console.log(terms)

// Example of how to get all trials 10 at a time because there is a page limit of 10
var page = 1
var limit = 10
var start = 0
var totalPages
// async while loop: while our current page is less than or equal to total pages, keep making requests
async.whilst(
  function () {
    return (!totalPages || page <= totalPages) && totalPages !== 0
  },
  function (cbk) {
    // start at page 1 w/ 10 limit, then when you find the total number of trials, increment the pages
    // can put ratelimiting timeout in here
    console.log('page ' + page + ' of ' + totalPages)
    requestretry({
      url: apiConnectionString + '/v2/trial/search',
      maxAttempts: 2,
      retryDelay: 50,
      method: 'POST',
      headers: {
        'content-type': 'application/json'
      },
      json: {
        apiKey: apiKey,
        filters: terms,
        start: start,
        limit: limit
      }
    }, function (error, response, body) {
      if (error) throw error
      if (response.statusCode == '200') {
        // console.log(JSON.stringify(body))
        var ids = []
        for (var i of body.rows) ids.push(i.id)
        console.log(ids)
      } else {
        console.log(response)
        console.log('statusCode: ' + response.statusCode)
      }
      totalPages = body.totalPages
      page++
      start += limit
      cbk()
    })
  },
  function (err) {
    process.exit()
  }
)

// TODO: geolocation searches
