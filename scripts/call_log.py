import datetime
import json

import requests

import localsettings


def fetch_logs():
    """
    Fetch Logs
    TODO: Exception Handling and validation for absence of keys.
    """
    payload = "token=" + localsettings.OPERATER_TOKEN
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.request("POST", localsettings.URL_LOGS, data=payload, headers=headers)
    response_data = json.loads(response.text)
    if response_data['code'] == 200:
        for hit in response_data['data']['hits']:
            print("Caller number: " + hit['_source']['caller_number'])
            print("Caller State: " + hit['_source']['state'])
            print("Call Start time: " + datetime.datetime.fromtimestamp(hit['_source']['start_time']).strftime(
                "%m/%d/%Y, %H:%M:%S"))
            print("Call End time: " + datetime.datetime.fromtimestamp(hit['_source']['end_time']).strftime(
                "%m/%d/%Y, %H:%M:%S"))
            print("Call Duration: " + hit['_source']['duration'])

            print("Call Duration: " + hit['_source']['additional_parameters'][0]['vl'])
            for each_attendee in hit['_source']['log_details']:
                print("Attendee ID: " + each_attendee['received_by'][0]['user_id'])
                print("Attendee name: " + each_attendee['received_by'][0]['name'])
                print("Attendee status: " + each_attendee['_ds'])


    else:
        print('Handle Error codes here..')


def fetch_logs_for_duration(start_datetime, end_datetime):
    """
    Fetch Logs
    TODO: Exception Handling and validation for absence of keys.
    """
    payload = "token=" + localsettings.OPERATER_TOKEN + "&from=" + start_datetime + "&to=" + end_datetime
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.request("POST", localsettings.URL_LOGS, data=payload, headers=headers)
    response_data = json.loads(response.text)
    if response_data['code'] == 200:
        for hit in response_data['data']['hits']:
            print("Caller number: " + hit['_source']['caller_number'])
            print("Caller State: " + hit['_source']['state'])
            print("Call Start time: " + datetime.datetime.fromtimestamp(hit['_source']['start_time']).strftime(
                "%m/%d/%Y, %H:%M:%S"))
            print("Call End time: " + datetime.datetime.fromtimestamp(hit['_source']['end_time']).strftime(
                "%m/%d/%Y, %H:%M:%S"))
            print("Call Duration: " + hit['_source']['duration'])

            print("Call Duration: " + hit['_source']['additional_parameters'][0]['vl'])
            for each_attendee in hit['_source']['log_details']:
                print("Attendee ID: " + each_attendee['received_by'][0]['user_id'])
                print("Attendee name: " + each_attendee['received_by'][0]['name'])
                print("Attendee status: " + each_attendee['_ds'])


    else:
        print('Handle Error codes here..')


if __name__ == "__main__":
    #fetch_logs()
    start_datetime = "1571615999"
    end_datetime = "1572047999"
    fetch_logs_for_duration(start_datetime, end_datetime)
