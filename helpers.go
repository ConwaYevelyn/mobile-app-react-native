package helpers

import (
	"encoding/json"
	"errors"
	"fmt"
	"log"
	"net/http"
	"strings"
)

func extractErrorMessage(err error) string {
	if err != nil {
		return err.Error()
	}
	return ""
}

func parseJSON(jsonString string, target interface{}) error {
	err := json.Unmarshal([]byte(jsonString), &target)
	if err != nil {
		return errors.New("failed to parse json: " + err.Error())
	}
	return nil
}

func makeAPIRequest(url string, method string, headers map[string]string, body string) (*http.Response, error) {
	req, err := http.NewRequest(method, url, strings.NewReader(body))
	if err != nil {
		return nil, err
	}
	for key, value := range headers {
		req.Header.Set(key, value)
	}
	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		return nil, err
	}
	if resp.StatusCode < 200 || resp.StatusCode >= 300 {
		return nil, errors.New(fmt.Sprintf("http request failed with status code %d", resp.StatusCode))
	}
	return resp, nil
}

func logError(message string, err error) {
	log.Printf("%s: %s", message, extractErrorMessage(err))
}