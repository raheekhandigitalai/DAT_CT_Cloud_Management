import requests
import json
from helper import common
from helper import helpers

base_auth = helpers.base_authentication()
access_key = helpers.get_access_key()
cloud_url = helpers.get_cloud_url()
base_end_point = helpers.get_base_endpoint()
devices_end_point = helpers.get_devices_endpoint()


def end_url():
    return cloud_url + base_end_point + devices_end_point


def get_devices():

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic %s' % base_auth
    }

    response = requests.request("GET",
                                end_url(),
                                headers=headers,
                                verify=False)
    helpers.logger(response.text)
    return response


def get_devices_by_device_query(device_query):

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic %s' % base_auth
    }

    response = requests.request("GET",
                                end_url() + '?query=%s' % device_query,
                                headers=headers,
                                verify=False)
    helpers.logger(response.text)
    return response


# def is_device_available(response):
#     devices = response["data"]
#     available_devices = []
#     for device in devices:
#         if "tags" in device != 0:


        # if "tags" in device and "unavailable" not in device["tags"]:
        #     available_devices.append(device)
    # return available_devices



def reserve_device(device_id, start_time, end_time, current_time):

    headers = {
        'Authorization': 'Basic %s' % base_auth
    }

    files = {
        'start': (None, start_time),
        'end': (None, end_time),
        'clientCurrentTimestamp': (None, current_time),
    }

    response = requests.request("POST",
                                end_url() + '/%s/reservations/new' % device_id,
                                files=files,
                                headers=headers,
                                verify=False)
    helpers.logger(response.text)
    return response


# Doesn't successfully release, need to investigate why
def release_device(device_id):

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic %s' % base_auth
    }

    response = requests.request("POST",
                                end_url() + '/%s/release' % device_id,
                                headers=headers,
                                verify=False)
    helpers.logger(response.text)
    return response


def remove_all_device_tags(device_id):

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % access_key
    }

    response = requests.request('DELETE',
                                end_url() + '/%s/tags' % device_id,
                                headers=headers,
                                verify=False)

    if response.status_code == 200:
        helpers.logger(
            'Python Script (function: remove_all_device_tags) - Successfully removed all device tags from device, '
            'response output: %s' % response.text)
    else:
        helpers.logger(
            'Python Script (function: remove_all_device_tags) - Unable to remove device tags from device, '
            'response output: %s' % response.text)

    return response


def add_device_tag(device_id, tag_value):

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % access_key
    }

    response = requests.request('PUT',
                                end_url() + '/' + str(device_id) + '/tags/' + str(tag_value),
                                headers=headers,
                                verify=False)

    if response.status_code == 200:
        helpers.logger(
            'Python Script (function: add_device_tag) - Successfully added device tag to device, '
            'response output: %s' % response.text)
        helpers.logger('Python Script (function: add_device_tag) - Device Tag Added: %s' % tag_value)
    else:
        helpers.logger(
            'Python Script (function: add_device_tag) - Unable to add device tag to device, '
            'response output: %s' % response.text)

    return response


def get_installed_certificates_from_device(device_id):
    # GET /api/v1/devices/{id}/cacerts

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % access_key
    }

    response = requests.request('GET',
                                end_url() + '/%s/cacerts' % device_id,
                                headers=headers,
                                verify=False)

    if response.status_code == 200:
        helpers.logger(
            'Python Script (function: get_installed_certificates_from_device) - '
            'Successfully retrieved all available Certificates from device, response output: %s' % response.text)
    else:
        helpers.logger(
            'Python Script (function: get_installed_certificates_from_device) - '
            'Unable to get Certificates from device, response output: %s' % response.text)

    return response
