//  DEPRECATION NOTE. mutation/get is no longer a supported endpoint.

// var requestretry = require('requestretry')
// var async = require('async')
//
// //////////////CONFIGS/////////////////////////////////
// /////////////////////////////////////////////////////
//
// var apiConnectionString = "https://api.molecularmatch.com"
// var apiKey = "" // <your api key>
// // or run as $ node assertionsAPI.js <key>
// if (process.argv[2]) apiKey = process.argv[2]
//
// /////////////////////////////////////////////////////
// /////////////////////////////////////////////////////
//
// var mutation = "BRAF V600E"
//
// async.series([
// 	function(cback) {
// 		// perorm a get mutation (gets enriched data on a variant)
// 		var url = apiConnectionString + "/v2/mutation/get" + "?name=" + mutation + "&apiKey=" + apiKey
// 		requestretry({
// 				url: url,
// 				maxAttempts: 2,
// 				retryDelay: 50,
// 				method: "GET"
// 			},
// 			function(error, response, body) {
// 				if (error) return cback(error)
// 				if (response.statusCode == "200") {
// 					//console.log(body)
// 				}
// 				else {
// 					console.log(url + 'statusCode: ' + response.statusCode)
// 				}
// 				cback()
// 			})
// 	},
// 	function(cback) {
// 		// perorm a get mutation classification with a condition to see how it should be classified
// 		// https://app.molecularmatch.com/search/BRAF%20V600E%20Colorectal%20cancer
// 		var url = apiConnectionString + "/v2/mutation/classify"
// 		requestretry({
// 				url: url,
// 				maxAttempts: 2,
// 				retryDelay: 50,
// 				method: "POST",
// 				json: {
// 					apiKey: apiKey,
// 					variant: mutation,
// 					condition: "Colorectal cancer"
// 				}
// 			},
// 			function(error, response, body) {
// 				if (error) return cback(error)
// 				if (response.statusCode == "200") {
// 					console.log('classification: ' + body.classifications[0].classification)
// 					console.log('trialCount: ' + body.classifications[0].trialCount)
// 					console.log('publicationCount: ' + body.classifications[0].publicationCount)
// 					console.log('drugsApprovedOnLabelCount: ' + body.classifications[0].drugsApprovedOnLabelCount)
// 					console.log('drugsApprovedOffLabelCount: ' + body.classifications[0].drugsApprovedOffLabelCount)
// 					console.log('drugsExperimentalCount: ' + body.classifications[0].drugsExperimentalCount)
// 				}
// 				else {
// 					console.log(url + ' statusCode: ' + response.statusCode)
// 				}
// 				cback()
// 			})
// 	}
//
// ], function(err) {
// 	if (err) throw error
// 	process.exit()
// })
//
// // Result
// // classification: actionable
// // trialCount: 19
// // publicationCount: 239
// // drugsApprovedOnLabelCount: 0
// // drugsApprovedOffLabelCount: 1
// // drugsExperimentalCount: 7
