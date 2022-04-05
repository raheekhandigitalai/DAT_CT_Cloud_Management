import requests
import json
from helper import common
from helper import helpers
from helper.helpers import logger

base_auth = helpers.base_authentication()
cloud_url = helpers.get_cloud_url()
base_end_point = helpers.get_base_endpoint()
projects_end_point = helpers.get_projects_endpoint()


def end_url():
    return cloud_url + base_end_point + projects_end_point


def get_projects():

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic %s' % base_auth
    }

    response = requests.request("GET",
                                end_url(),
                                headers=headers,
                                verify=False)

    # id = find_project_id('opportunity', response.content)
    # logger(id)
    logger(response.text)
    return response


def create_project(name, device_group_id):

    headers = {
        'Authorization': 'Basic %s' % base_auth
    }

    files = {
        'name': (None, name),
        'deviceGroupId': (None, device_group_id)
    }

    response = requests.request("POST",
                                end_url() + "/new",
                                files=files,
                                headers=headers,
                                verify=False)
    logger(response.text)

    project_id = common.get_id(response.content)
    logger(project_id)
    return project_id


def delete_project(project_id):

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic %s' % base_auth
    }

    response = requests.request("POST",
                                end_url() + "/%s/delete" % project_id,
                                headers=headers,
                                verify=False)

    logger(response.text)
    return response


def set_max_concurrent_browser(project_id):

    headers = {
        'Authorization': 'Basic %s' % base_auth
    }

    files = {
        'maxSeleniumSessions': (None, 0)
    }

    response = requests.request("POST",
                                end_url() + "/%s/max-concurrent-browser" % project_id,
                                files=files,
                                headers=headers,
                                verify=False)
    logger(response.text)


def set_web_cleanup_status(project_id, enable):

    headers = {
        'Authorization': 'Basic %s' % base_auth
    }

    files = {
        # Boolean - If yes > enabled Web Cleanup. If no > disabled Web Cleanup.
        'enable': (None, enable)
    }

    response = requests.request("POST",
                                end_url() + "/%s/web-cleanup" % project_id,
                                files=files,
                                headers=headers,
                                verify=False)
    logger(response.text)


def set_notes(project_id, notes):

    headers = {
        'Authorization': 'Basic %s' % base_auth
    }

    files = {
        'notes': (None, notes)
    }

    response = requests.request("POST",
                                end_url() + "/%s/notes" % project_id,
                                files=files,
                                headers=headers,
                                verify=False)
    logger(response.text)


def get_project_id(project_name):

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic %s' % base_auth
    }

    response = requests.request("GET",
                                end_url(),
                                headers=headers,
                                verify=False)

    project_id = find_project_id(project_name, response.content)
    return project_id


def find_project_id(value, response_content):
    data = json.loads(response_content)
    id = 0

    for key in data:
        if key == "data":
            for subKey in data['data']:
                project_id = subKey['id']
                project_name = subKey['name']
                # logger(project_name)
                if value in project_name:
                    logger('project found')
                    id = project_id
                    break
                else:
                    logger('project not found')

    return id

# def clean_up_devices():
#
#     return 0
#
#
# def enable_cleanup_mechanism_for_project():
#
#     return 0

