// DEPRECATION NOTE. prevalence is no longer a supported endpoint.

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
// async.series([
// 	// find how prevalent a mutation is in all conditions with prevalence aggregate
// 	// type = AVG will calculate average prevalence for all conditions, MAX calculates the maximum condition prevalence
// 	function(cback) {
// 		requestretry({
// 				url: apiConnectionString + "/v2/prevalence/aggregate",
// 				maxAttempts: 2,
// 				retryDelay: 50,
// 				method: "POST",
// 				headers: {
// 					'content-type': 'application/json'
// 				},
// 				json: {
// 					apiKey: apiKey,
// 					type: "AVG", // "MAX"
// 					filters: [{'facet':'MUTATION','term':'BRAF V600E'}]
// 				}
// 			},
// 			function(error, response, body) {
// 				if (error) throw error
// 				if (response.statusCode == "200") {
// 					//console.log(JSON.stringify(body))
// 					console.log(['total aggregate average = ', body['aggregation']['frequency'], " (", body['aggregation']['count'], '/', body['aggregation']['samples'], ")"].join(""))
// 				}
// 				else {
// 					console.log('statusCode: ' + response.statusCode)
// 				}
// 				cback()
// 			})
// 	},
// 	// find how prevalent a mutation is in a single condition
// 	function(cback) {
// 		requestretry({
// 				url: apiConnectionString + "/v2/prevalence/aggregate",
// 				maxAttempts: 2,
// 				retryDelay: 50,
// 				method: "POST",
// 				headers: {
// 					'content-type': 'application/json'
// 				},
// 				json: {
// 					apiKey: apiKey,
// 					type: "AVG", // "MAX"
// 					filters: [{'facet':'MUTATION','term':'BRAF V600E'}, {'facet':'CONDITION','term':'Colorectal cancer'}]
// 				}
// 			},
// 			function(error, response, body) {
// 				if (error) throw error
// 				if (response.statusCode == "200") {
// 					//console.log(JSON.stringify(body))
// 					console.log(['total colorecal average = ', body['aggregation']['frequency'], " (", body['aggregation']['count'], '/', body['aggregation']['samples'], ")"].join(""))
// 				}
// 				else {
// 					console.log('statusCode: ' + response.statusCode)
// 				}
// 				cback()
// 			})
// 	},
// 	// look at discrete samples with prevalence search
// 	function(cback) {
// 		requestretry({
// 				url: apiConnectionString + "/v2/prevalence/search",
// 				maxAttempts: 2,
// 				retryDelay: 50,
// 				method: "POST",
// 				headers: {
// 					'content-type': 'application/json'
// 				},
// 				json: {
// 					apiKey: apiKey,
// 					filters: [{'facet':'MUTATION','term':'BRAF V600E'}, {'facet':'CONDITION','term':'Colorectal cancer'}]
// 				}
// 			},
// 			function(error, response, body) {
// 				if (error) throw error
// 				if (response.statusCode == "200") {
// 					//console.log(JSON.stringify(body))
// 					for (var i = 0; i<body.hits.length; i++) {
// 						var study_record = body.hits[i]
// 						console.log(study_record['percent'] + ' percent positive in study: ' + study_record['studyId'])
// 					}
// 				}
// 				else {
// 					console.log('statusCode: ' + response.statusCode)
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
// // total aggregate average = 0.0572 (915/15998)
// // total colorecal average = 0.103 (212/2059)
// // 7.46 percent positive in study: msk_impact_2017_Colorectal_Cancer
// // 8.93 percent positive in study: coadread_tcga_pub
// // 1.45 percent positive in study: coadread_mskcc
// // 5.56 percent positive in study: coadread_genentech
// // 17.93 percent positive in study: coadread_dfci_2016
