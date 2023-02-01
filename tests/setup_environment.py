import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from api import device_groups
from api import projects
from api import applications
from api import devices
from api import users


def setup_environment_test(project_name):
    device_id = 4840738

    device_group_id = device_groups.create_device_group(project_name)
    project_id = projects.create_project(project_name, device_group_id)
    projects.set_notes(project_id, 'Created by Automated Script')

    apk = 'https://demoapplications.s3.amazonaws.com/com.experitest.ExperiBank_.LoginActivity_ver_2527.apk'
    ipa = 'https://demoapplications.s3.amazonaws.com/com.experitest.ExperiBank_ver_4077.ipa'

    applications.upload_application_to_project(apk, project_id)
    applications.upload_application_to_project(ipa, project_id)

    device_groups.assign_devices_to_device_group(device_id, device_group_id)

    users.create_user('raheetest', 'firstname', 'lastname', 'raheetest@gmail.com', project_id, 'User')


if __name__ == "__main__":
    setup_environment_test(sys.argv[1])
    