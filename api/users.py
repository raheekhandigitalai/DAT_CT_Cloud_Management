import requests
import json
import csv
from helper import common
from helper import helpers
from helper.helpers import logger

base_auth = helpers.base_authentication()
access_key = helpers.get_access_key()
cloud_url = helpers.get_cloud_url()
base_end_point = helpers.get_base_endpoint()
users_end_point = helpers.get_users_endpoint()
projects_end_point = helpers.get_projects_endpoint()


def end_url():
    return cloud_url + base_end_point + users_end_point


def get_users():

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


def create_user(username, first_name, last_name, email, project_id, role):
    headers = {
        'Authorization': 'Basic %s' % base_auth
    }

    files = {
        'username': (None, username),
        'firstName': (None, first_name),
        'lastName': (None, last_name),
        'email': (None, email),
        'project': (None, project_id),
        'role': (None, role)  # Admin / ProjectAdmin / User
    }

    response = requests.request("POST",
                                end_url() + "/new",
                                files=files,
                                headers=headers,
                                verify=False)
    logger(response.text)
    user_id = common.get_id(response.content)
    return user_id


def delete_user(user_id):
    # POST /api/v1/users/{userid}/delete
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic %s' % base_auth
    }

    response = requests.request("POST",
                                end_url() + '/%s/delete' % str(user_id),
                                headers=headers,
                                verify=False)
    logger(response.text)
    return response


def get_users_from_project_and_delete(project_id):
    # /api/v1/projects/{projectid}/users
    # endPoint = "/projects/" + str(project_id) + "/users"
    # endUrl = common.baseUrl + endPoint

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic %s' % base_auth
    }

    response = requests.request("GET", 
                                cloud_url + base_end_point + projects_end_point + '/%s/users' % project_id,
                                headers=headers, 
                                verify=False)
    logger(response.text)
    get_users_id_and_delete(response.content)


def get_users_id_and_delete(response_content):
    data = json.loads(response_content)

    for key in data:
        if key == "data":
            for subKey in data['data']:
                delete_user(subKey['id'])

                # logger(subKey['id'])
                # if 'digital.ai' in subKey['username']:
                # if subKey['username'].find('digital.ai'):
                #     logger(
                #         'Python Script (function: get_users_id_and_delete) - '
                #         'Not deleting User as User is part of Digital.ai.')
                # else:
                #     delete_user(subKey[id])
                #     logger(
                #         'Python Script (function: get_users_id_and_delete) - Deleting User.')


def user_exists(value, response_content):
    data = json.loads(response_content)

    for key in data:
        if key == "data":
            for subKey in data['data']:
                new_data = subKey['userName']
                # logger(newData)
                if new_data == value:
                    return True


def check_if_user_exists(username, response_content):
    json_response = response_content.json()

    for item in json_response['data']:
        username_list = []
        username = item['userName']
        username_list.append(username)
        logger(username)
        if username == "rahee":
            logger("username exists")
            break
    return username


def create_users_reading_csv_file(project_id, path_to_csv_file):
    with open(path_to_csv_file, newline='') as f:
        reader = csv.reader(f)
        data = [tuple(row) for row in reader]

        logger(data)

        for each in data:
            create_user(each[0],
                        each[1],
                        each[2],
                        each[3],
                        project_id,
                        each[4])
