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


def main():
    print('some values')
    # devices.get_devices()
    # projects.create_project('opportunity', 254111)
    # projects.set_max_concurrent_browser(3484499)
    # projects.get_projects()
    # projects.get_project_id('opportunity')
    # projects.delete_project(3484498)
    # projects.set_web_cleanup_status(3484499, True)
    # projects.set_notes(3484499, 'Project created by rahee')

    # device_groups.create_device_group('opportunity') # 3484505
    # device_groups.delete_device_group(3484505)
    # device_groups.get_device_groups()
    # device_group_id = 3484251
    # device_groups.assign_devices_to_device_group('731332', device_group_id)
    # device_groups.get_devices_in_device_group(device_group_id)
    # device_groups.remove_devices_from_device_group('731332', device_group_id)
    # devices.get_devices()
    # devices.get_devices_by_device_query("@os='ios' and @category='PHONE'")
    # devices.reserve_device(1937530, start_time='2022-04-04-15-00-00', end_time='2022-04-04-15-30-00', current_time='2022-04-04-14-30-00')
    # devices.release_device(1937530)
    # devices.add_device_tag(1937530, 'rahee')
    # devices.remove_all_device_tags(1937530)
    # applications.get_applications()
    # applications.upload_application_to_project('https://demoapplications.s3.amazonaws.com/com.experitest.ExperiBank_.LoginActivity_ver_2527.apk', project_id)
    # applications.upload_application_to_project('https://demoapplications.s3.amazonaws.com/com.experitest.ExperiBank_ver_4077.ipa', project_id)
    # print(user_id)
    # users.delete_user(3488897)
    # users.get_users()
    project_id = 3484499
    # user_id = users.create_user('opportunity2', 'opportunity', 'opportunity', 'opportunity@unlock.ai', project_id, 'User')
    # users.get_users_from_project_and_delete(project_id)


def prepocfullflow(name):
    print('hello')
    # deviceGroupId = device_groups.create_device_group(name)
    # projectId = projects.createProject(name, deviceGroupId)
    # projects.setMaxConcurrentBrowser(projectId)
    # applications.assignExperiBankApplicationToProject('https://demoapplications.s3.amazonaws.com/com.experitest.ExperiBank_.LoginActivity_ver_2527.apk', projectId)
    # applications.assignExperiBankApplicationToProject('https://demoapplications.s3.amazonaws.com/com.experitest.ExperiBank_ver_4077.ipa', projectId)
    # users.createUsersReadingCSVFile(projectId)


if __name__ == "__main__":
    main()
