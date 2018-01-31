package main

import (
	"bytes"
	"fmt"
	"io/ioutil"
	"net/http"
)

func main() {
	url := "https://api.molecularmatch.com/v2/search/trials"
  var jsonStr = []byte(`
    {"filters":[
      {"facet":"CONDITION","term":"Lung cancer"},
      {"facet":"MUTATION","term":"EGFR T790M"}
    ]}
  `)

  apiKey:= "<your api key>"

  req, err := http.NewRequest("POST", url, bytes.NewBuffer(jsonStr))
	req.Header.Set("Content-Type", "application/json")
  req.Header.Set("Authorization", "Bearer " + apiKey)

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()
	body, _ := ioutil.ReadAll(resp.Body)

	fmt.Println(string(body))
}
