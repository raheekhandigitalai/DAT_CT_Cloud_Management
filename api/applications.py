import requests
import json
from helper import common
from helper import helpers

base_auth = helpers.base_authentication()
access_key = helpers.get_access_key()
cloud_url = helpers.get_cloud_url()
base_end_point = helpers.get_base_endpoint()
applications_end_point = helpers.get_applications_endpoint()


def end_url():
    return cloud_url + base_end_point + applications_end_point


def get_applications():

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


def upload_application_to_project(url, project_id):

    headers = {
        'Authorization': 'Basic %s' % base_auth
    }

    files = {
        'url': (None, url),
        'camera': (None, True),
        'touchId': (None, True),
        'project': (None, 'id:' + str(project_id))
    }

    response = requests.request("POST", 
                                end_url() + '/new-from-url',
                                files=files, 
                                headers=headers, 
                                verify=False)
    helpers.logger(response.text)
    return response
