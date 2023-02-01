import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from api import device_groups
from api import projects
from api import applications
from api import devices
from api import users


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
    # project_id = 3484499
    # user_id = users.create_user('opportunity2', 'opportunity', 'opportunity', 'opportunity@unlock.ai', project_id, 'User')
    # users.get_users_from_project_and_delete(project_id)


def set_up_environment(project_name):
    device_id = 4840738

    device_group_id = device_groups.create_device_group(project_name)
    project_id = projects.create_project(project_name, device_group_id)
    projects.set_notes(project_id, 'Created by Rahee')

    apk = 'https://demoapplications.s3.amazonaws.com/com.experitest.ExperiBank_.LoginActivity_ver_2527.apk'
    ipa = 'https://demoapplications.s3.amazonaws.com/com.experitest.ExperiBank_ver_4077.ipa'

    applications.upload_application_to_project(apk, project_id)
    applications.upload_application_to_project(ipa, project_id)

    device_groups.assign_devices_to_device_group(device_id, device_group_id)

    users.create_user('raheetest', 'firstname', 'lastname', 'raheetest@gmail.com', project_id, 'User')


def tear_down_environment(project_name):
    # device_group_id = 3488932
    # project_id = 3488933
    device_id = 4840738

    device_group_id = device_groups.get_device_group_id(project_name)
    device_group_id = str(device_group_id)
    project_id = projects.get_project_id(project_name)

    device_groups.remove_devices_from_device_group(device_id, device_group_id)
    users.get_users_from_project_and_delete(project_id)
    device_groups.delete_device_group(device_group_id)
    projects.delete_project(project_id)


if __name__ == "__main__":
    print('debug')
    # set_up_environment('raheetest')
    # tear_down_environment('raheetest')
