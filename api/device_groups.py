import requests
import json
from helper import common
from helper import helpers
from helper.helpers import logger

base_auth = helpers.base_authentication()
cloud_url = helpers.get_cloud_url()
base_end_point = helpers.get_base_endpoint()
device_groups_end_point = helpers.get_device_groups_endpoint()


def end_url():
    return cloud_url + base_end_point + device_groups_end_point


def get_device_groups():

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic %s' % base_auth
    }

    response = requests.request("GET",
                                end_url(),
                                headers=headers,
                                verify=False)
    logger(response.text)
    return response


def create_device_group(device_group_name):

    headers = {
        'Authorization': 'Basic %s' % base_auth
    }

    files = {
        'name': (None, device_group_name),
        'acceptNewDevices': (None, False)
    }

    response = requests.request("POST", 
                                end_url() + '/new',
                                files=files, 
                                headers=headers, 
                                verify=False)
    logger(response.text)

    device_group_id = common.get_id(response.content)
    logger(device_group_id)
    return device_group_id


def remove_devices_from_device_group(device_id_list, device_group_id):
    # DELETE /api/v1/device-groups/{group-id}/devices/ - deviceIdList - String - device ids separated by commas
    headers = {
        'Authorization': 'Basic %s' % base_auth
    }

    files = {
        'deviceIdList': (None, device_id_list),
    }

    response = requests.request("DELETE",
                                end_url() + '/%s/devices/' % device_group_id,
                                files=files,
                                headers=headers,
                                verify=False)
    logger(response.text)
    return response


def assign_devices_to_device_group(device_id_list, device_group_id):
    # PUT /api/v1/device-groups/{group-id}/devices/ - deviceIdList - String - device ids separated by commas
    headers = {
        'Authorization': 'Basic %s' % base_auth
    }

    files = {
        'deviceIdList': (None, device_id_list),
    }

    response = requests.request("PUT",
                                end_url() + '/%s/devices/' % device_group_id,
                                files=files,
                                headers=headers,
                                verify=False)
    logger(response.text)
    return response


def delete_device_group(device_group_id):

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic %s' % base_auth
    }

    response = requests.request("DELETE",
                                end_url() + "/%s/" % device_group_id,
                                headers=headers,
                                verify=False)
    logger(response.text)
    return response


def get_devices_in_device_group(device_group_id):

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic %s' % base_auth
    }

    response = requests.request("GET",
                                end_url() + "/%s/devices" % device_group_id,
                                headers=headers,
                                verify=False)
    logger(response.text)
    return response


def get_device_group_id(device_group_name):

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic %s' % base_auth
    }

    response = requests.request("GET",
                                end_url(),
                                headers=headers,
                                verify=False)

    logger(find_device_group(device_group_name, response.content))
    # id = find_device_group(device_group_name, response.content)
    # logger(id)
    # return id


def find_device_group(value, response_content):
    data = json.loads(response_content)

    for key in data:
        if key == "data":
            for subKey in data['data']:
                logger(subKey)
                # split_lines = subKey[1].split(", ")
                # print(split_lines)
                # split_lines = subKey.split(", ")

                # split_data = data['data']
                # test = split_data.split(", ")[0]
                # logger(test)
                # for x in range(len(subKey)):
                #     logger(data['data'])
                # for x in range(len(data['data'])):
                #     logger(subKey)

                # deviceGroupId = subKey['id']
                # deviceGroupName = subKey['name']
                # # logger(projectName)
                # if deviceGroupName == value:
                #     return deviceGroupId