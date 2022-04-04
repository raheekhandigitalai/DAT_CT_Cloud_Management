import requests
import json
import base64
import csv
from api import device_groups
from api import projects
from api import applications
from api import devices
from api import users
from api import reporter
from helper import common


def prepocfullflow(name):
    device_group_id = device_groups.create_device_group(name)
    project_id = projects.create_project(name, device_group_id)
    projects.set_max_concurrent_browser(project_id)
    applications.assign_experibank_application_to_project('https://demoapplications.s3.amazonaws.com/com.experitest.ExperiBank_.LoginActivity_ver_2527.apk', project_id)
    applications.assign_experibank_application_to_project('https://demoapplications.s3.amazonaws.com/com.experitest.ExperiBank_ver_4077.ipa', project_id)
    # users.create_users_reading_csv_file(projectId)


def getProjectsInDeviceGroup(groupId):
    # GET /api/v1/device-groups/{group-id}/projects
    endPoint = "/device-groups/" + str(groupId) + "/projects"
    endUrl = common.baseUrl + endPoint

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic cmFoZWU6U3VycmFoZWUyMg=='
    }

    response = requests.request("GET", endUrl, headers=headers, verify=False)
    print(response.text)


def getDeviceGroups():
    # GET /api/v1/device-groups
    endPoint = "/device-groups"
    endUrl = common.baseUrl + endPoint

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic cmFoZWU6U3VycmFoZWUyMg=='
    }

    response = requests.request("GET", endUrl, headers=headers, verify=False)
    findDeviceGroupId("", response.content)
    # print(response.text)


def findDeviceGroupId(value, responseContent):
    data = json.loads(responseContent)

    for key in data:
        if key == "data":
            for subKey in data['data']:
                print(subKey)

                # deviceGroupId = subKey['id']
                # deviceGroupName = subKey['name']
                # # print(projectName)
                # if deviceGroupName == value:
                #     return deviceGroupId


def findDeviceGroupIdInProject(projectId):
    deviceGroupId = device_groups.createDeviceGroup('RaheeTesting')
    print("Rahee: " + deviceGroupId)

    endPoint = "/projects/" + str(projectId) + "/notes"
    endUrl = common.baseUrl + endPoint

    headers = {
        # 'Content-Type': 'application/json',
        'Authorization': 'Basic cmFoZWU6U3VycmFoZWUyMg=='
    }

    files = {
        'notes': (None, str(deviceGroupId))
    }

    response = requests.request("POST", endUrl, files=files, headers=headers, verify=False)
    print(response.text)
    response = requests.request("GET", endUrl, headers=headers, verify=False)
    print(response.text)


def getProjectsNote(projectId):
    endPoint = "/projects/" + str(projectId) + "/notes"
    endUrl = common.baseUrl + endPoint

    headers = {
        # 'Content-Type': 'application/json',
        'Authorization': 'Basic cmFoZWU6U3VycmFoZWUyMg=='
    }

    response = requests.request("GET", endUrl, headers=headers, verify=False)
    print(response.text)
    print(getId(response.content))


def getId(responseContent):
    data = json.loads(responseContent)
    # id = data['data'][0:7]

    myList = []

    for value in data['data']:
        print(value)
        myList.append(value)

    # myList.replace('\n', '')

    print(myList + ' <<<--- ')

    # for value in data['data']:
    #     print(value)

    # return id


def findDeviceGroupIdInProjectNew(projectName):

    projectId = projects.getProjectId(projectName)

    endPoint = "/projects/" + str(projectId) + "/notes"
    endUrl = common.baseUrl + endPoint

    headers = {
        'Authorization': 'Basic cmFoZWU6U3VycmFoZWUyMg=='
    }

    response = requests.request("GET", endUrl, headers=headers, verify=False)
    deviceGroupId = common.getIdTest(response.content)
    print(response.text)
    print("DeviceGroupId in Notes:" + deviceGroupId)


def main():
    # getDeviceGroups()
    # getTestAPIResponse()
    # downloadfile()
    # download_file('https://uscloud.experitest.com/reporter/api/54673/attachments')
    # getUsers()
    # createDeviceGroup('raheetest')
    # createProject()
    # createUser("rahee.khan@digital.ai", "rahee", "khan", "rahee.khan@digital.ai", "User")

    # prepocfullflow('Virgin Voyages')

    devices.get_devices()

    # getApplications()
    # getDevices()
    # createUsersReadingCSVFile()
    # getProjects()
    # projectId = getProjectId('RaheeTestingAutomation')
    # getUsersFromProjectAndDelete(projectId)

    # deviceGroupId = device_groups.getDeviceGroupId('RaheeTestingAutomation')
    # device_groups.deleteDeviceGroup(deviceGroupId)

    # device_groups.getDeviceGroupId('RaheeTestingAutomation')
    # getProjectsInDeviceGroup(2495105)
    # findDeviceGroupIdInProject(2)

    # findDeviceGroupIdInProjectNew("Device Cleanup")

    # getProjectsNote(2)


if __name__ == "__main__":
    main()
