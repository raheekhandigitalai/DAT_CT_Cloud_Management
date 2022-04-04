import requests
import json

baseUrl = "https://uscloud.experitest.com/api/v1"


def get_status(response_content):
    data = json.loads(response_content)
    status = data['status']
    return status


def get_id(response_content):
    data = json.loads(response_content)
    id = data['data']['id']
    return id


def get_id_test(response_content):
    data = json.loads(response_content)
    id = data['data'][0]
    print(id)
    return id

    # for value in range(data):
    # for i in range(len(data)):
    # for i in data:
    #     print(i)

    # for value in data.items():
    #     print(value)

    # id = data['data'][]
    # return id